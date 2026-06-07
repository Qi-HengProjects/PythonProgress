import json
import sys
import pandas as pd

expenses = {
        "name" : [],
        "amount" : [],
        "date" : [],
        "type" : []
}

def save(data):
    with open("expenses.json", "w") as file:
        json .dump(data, file)
        print("Data Saved")

def load():
    with open("expenses.json", "r") as file:
        print("Data Loaded")
        return json.load(file)

def export_csv():
    pd.read_json("expenses.json").to_csv("expenses.csv", index=False)

def add(name, amount, date, type):
    expenses = load()
    expenses["name"].append(name)
    expenses["amount"].append(amount)
    expenses["date"].append(date)
    expenses["type"].append(type)
    save(expenses)

def remove(index):
    expenses = load()
    expenses["name"].pop(index)
    expenses["amount"].pop(index)
    expenses["date"].pop(index)
    expenses["type"].pop(index)
    save(expenses)

def display():
    load_data = load()
    if not load_data.values():
        print("No expenses found")
    else:
        count = 1
        for data in load_data.values():
            match count:
                case 1:
                    print(f"Name: {data}")
                    count += 1
                case 2:
                    print(f"Amount: {data}")
                    count += 1
                case 3:
                    print(f"Date: {data}")
                    count += 1
                case 4:
                    print(f"Type: {data}")
                    count += 1
                case 5:
                    count = 1


while True:
    print("\nWelcome to Expense Tracker")
    option = int(input("Select an option:\n1. add an expense \n2. Delete an expense\n3. Exit\n4. Display expenses \n5. Export to CSV \nYour option: "))
    match option:
        case 1:

            name = input("\nPlease enter your expense name: ")
            amount = input("Please enter your expense amount: ")
            date = input("Please enter your expense date: ")
            type = input("Please enter your expense type: ")
            add(name, amount, date, type)

        case 2:
            display()
            select = int(input("\nPlease enter the expense index you want to delete: "))
            remove(select)
        case 3:
            sys.exit(1)
        case 4:
            display()
        case 5:
            export_csv()
        case _:
            print("\nInvalid option")
