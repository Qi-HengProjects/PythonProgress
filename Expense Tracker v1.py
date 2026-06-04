import json
import sys

def save(data):
    with open("expenses.json", "w") as file:
        json.dump(data, file)
        print("Data Saved")

def load():
    with open("expenses.json", "r") as file:
        print("Data Loaded")
        return json.load(file)

expenses = {
        "name" : [],
        "amount" : [],
        "date" : [],
        "type" : []
}

def add(name, amount, date, type):
    expenses["name"].append(name)
    expenses["amount"].append(amount)
    expenses["date"].append(date)
    expenses["type"].append(type)
    save(expenses)

def remove(index):
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
        for data in load_data.values():
           print(data)




while True:
    print("Welcome to Expense Tracker")
    option = int(input("Select an option:\n1. add an expense \n2. Delete an expense\n3. Exit\n4. Display expenses \nYour option: "))
    match option:
        case 1:
            name = input("Please enter your expense name: ")
            amount = input("Please enter your expense amount: ")
            date = input("Please enter your expense date: ")
            type = input("Please enter your expense type: ")
            add(name, amount, date, type)


        case 2:
            select = int(input("Please enter the expense index you want to delete: "))
            remove(select)
        case 3:
            sys.exit(1)
        case 4:
            display()
        case _:
            print("Invalid option")
