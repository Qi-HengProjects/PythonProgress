from dataclasses import dataclass
from decimal import Decimal
from datetime import date
from enum import Enum
import json

@dataclass(frozen=True)
class Expense:
    name: str
    date: date
    amount:Decimal
    category: Enum
    description: str
    id :int

class ExpenseCategory(Enum):
    UTILITIES = "Utilities"
    ENTERTAINMENT = "Entertainment"
    INVESTMENT = "Investment"
    SAVINGS = "Savings"
    OTHER = "Other"

class ExpenseRepository:
    def __init__(self):
        self._expenses = {}
        self._next_id = 1

    def add_expense(self, name, date, amount, category: ExpenseCategory, description :str):
        if not name.strip():
            raise ValueError("Expense name cannot be empty")

        if amount <= 0:
            raise ValueError("Expense amount cannot be negative")

        expense = Expense(name, date, amount, category, description, id=self._next_id)
        self._expenses[self._next_id] = expense
        self._next_id += 1

    def delete_expense(self, id):
        if id not in self._expenses:
            raise ValueError("Expense id does not exist")
        self._expenses.pop(id)

    def get_all_expenses(self):
        return list(self._expenses.values())

    def load(self, explicit_expenses: list[Expense]):
        for expense in explicit_expenses: #from dictionary in list to object
            self._expenses[expense.id] = expense
            if expense.id >= self._next_id:
                self._next_id = expense.id +1

class JSONStorageController:
    def __init__(self, filepath: str = "expenses.json"):
        self.filepath = filepath

    def serialize_expenses(self, expense: Expense):
       return {
           "id": expense.id,
           "name": expense.name,
           "date": str(expense.date),
           "amount": str(expense.amount),
           "category": expense.category.value,
           "description": expense.description
       }

    def deserialize_expenses(self, data: dict) -> Expense:
        expense = Expense(data["name"], date.fromisoformat(data["date"]), Decimal(data["amount"]), ExpenseCategory(data["category"]), data["description"], id=data["id"])
        return expense

    def save_to_file(self, all_expenses: list[Expense]):
        serialized_list = []
        for exp in all_expenses:
            serialized_list.append(self.serialize_expenses(exp))

        with open(self.filepath, "w") as file:
            json.dump(serialized_list, file, indent=4)

    def load_from_file(self) -> list[Expense]:
        try:
            with open(self.filepath, "r") as file:
                raw_data_list = json.load(file)

            hydrated_expenses = []
            for item in raw_data_list:
                hydrated_expenses.append(self.deserialize_expenses(item)) #translate from json to dictionary in list

            return hydrated_expenses
        except FileNotFoundError:
            return []


def main():
    repo = ExpenseRepository()
    storage = JSONStorageController("expenses.json")

    repo.load(storage.load_from_file())
    print("--- System Bootstrapped and Live ---")

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. List All Expenses")
        print("3. Delete Expense")
        print("4. Save & Exit")
        choice = (input("Enter your choice: "))

        match choice:
            case "1":
                name = input("Enter expense name: ").strip()
                date_str = input("Enter date (YYYY-MM-DD): ").strip()
                amount_str = input("Enter amount: ").strip()

                print("Available Categories:")
                for cat in ExpenseCategory:
                    print(f" - {cat.value}")
                cat_str = input("Select category: ").strip()
                desc = input("Enter description: ")

                try:
                    converted_date = date.fromisoformat(date_str)
                    converted_amount = Decimal(amount_str)
                    category = ExpenseCategory(cat_str)
                    repo.add_expense(name, converted_date,converted_amount, category, desc)
                    print("\n[SUCCESS] Expense securely logged in-memory.")
                except ValueError:
                    print("\n[INPUT ERROR] Invalid data formatting or constraint violation. Entry aborted.")

            case "2":
                expenses = repo.get_all_expenses()
                if not expenses:
                    print("No expenses logged.")
                for exp in expenses:
                    print(f"[{exp.id}] {exp.date} | {exp.name} (${exp.amount}) - Category: {exp.category.value}")

            case "3":
                try:
                    target = input("Enter expense id you want to delete: ")
                    repo.delete_expense(int(target))
                except ValueError:
                    print("\n[INPUT ERROR] Invalid data formatting or constraint violation. Entry aborted.")

            case "4":
                storage.save_to_file(repo.get_all_expenses())
                print("State committed to disk. Goodbye!")
                break

            case _:
                print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
