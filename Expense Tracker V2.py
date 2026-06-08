from dataclasses import dataclass
from decimal import Decimal
from datetime import date
import json

@dataclass(frozen=True)
class Expense:
    name: str
    date: date
    amount:Decimal
    category: str
    description: str
    id :int

class ExpenseRepository:
    def __init__(self):
        self._expenses = {}
        self._next_id = 1

    def add_expense(self, name, date, amount, category, description):
        expense = Expense(name, date, amount, category, description, id=self._next_id)
        self._expenses[self._next_id] = expense
        self._next_id += 1

    def delete_expense(self, id):
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
           "category": expense.category,
           "description": expense.description
       }

    def deserialize_expenses(self, data: dict) -> Expense:
        expense = Expense(data["name"], date.fromisoformat(data["date"]), Decimal(data["amount"]), data["category"], data["description"], id=data["id"])
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


