global ID
global allExpenses
budget = 0

def generateID():
    ID = 1000
    ID += 1
    return ID


monthlyExpenses = {
        "Utility": [],
        "Grocery": [],
        "Investment": [],
        "Entertainment": [],
        "Others": []
    }

class Expenses:
    def __init__(self, name, date, amount, purpose, ID, category, desc):
        self.name = name
        self.date = date
        self.amount = amount
        self.purpose = purpose
        self.ID = ID
        self.category = category
        self.desc = desc

    def generateID(self):
        self.ID = ID + 1

    def searchID(self, ID):
        if ID in self.ID:
            return True
        else:
            return False

    def removeFromList(self, array, ID):
        searchID = self.searchID(ID)
        if searchID:
            array.remove(self)
        else:
            return "No expense found"

    def totalExpenses(self, array):
        total = 0
        for i in array:
            total += i.amount
            return total


class Utility(Expenses):
    def __init__(self, name, date, amount, purpose, ID, category, desc, paymentStatus):
        super().__init__(self, name, date, amount, purpose, ID, category, desc)
        self.paymentStatus = paymentStatus

class Grocery(Expenses):
    def __init__(self, name, date, amount, purpose, ID, category, desc, store):
        super().__init__(self, name, date, amount, purpose, ID, category, desc)
        self.store = store

class Investment(Expenses):
    def __init__(self, name, date, amount, purpose, ID, category, desc, platform, type):
        super().__init__(self, name, date, amount, purpose, ID, category, desc)
        self.platform = platform
        self.type = type

class Entertainment(Expenses):
    def __init__(self, name, date, amount, purpose, ID, category, desc, type):
        super().__init__(self, name, date, amount, purpose, ID, category, desc)
        self.type = type

if __name__ == "__main__":
    print("Welcome to Expense Tracker")
    if budget == 0:
        budget = float(input("Please enter your monthly budget"))
    else:
        print(f"Your monthly budget: {budget}")

    option = int(input("Select an option:\n1. add an expense \n2. Delete an expense \n3. Modify an expense \n 4. Exit\n"))
    match option:
        case 1:
            name = input("Please enter your expense name:")
            date = input("Please enter your expense date:")
            amount = input("Please enter your expense amount:")
            purpose = input("Please enter your expense purpose:")
            ID = generateID()
            category = input("Please enter your expense category:\n1. Utility\n2. Grocery\n3. Investment\n4. Entertainment\n5. Others")
            desc = input("Please enter your expense description:")
            match category:
                case 1:
                    paymentStatus = input("Please enter your expense payment status:")
                    monthlyExpenses["Utility"].append(Utility(name, date, amount, purpose, ID, category, desc, paymentStatus))
                case 2:
                    store = input("Please enter store  you bought from:")
                    monthlyExpenses["Grocery"].append(Grocery(name, date, amount, purpose, ID, category, desc, store))
                case 3:
                    platform = input("Please enter your expense platform:")
                    type = input("Please enter your investment type:")
                    monthlyExpenses["Investment"].append(Investment(name, date, amount, purpose, ID, category, desc, platform, type))
                case 4:
                    type = input("Please enter your entertainment type:")
                    monthlyExpenses["Entertainment"].append(Entertainment(name, date, amount, purpose, ID, category, desc, type))
                case 5:
                    Expenses(name, date, amount, purpose, ID, category, desc)
                    monthlyExpenses["Others"].append(Expenses(name, date, amount, purpose, ID, category, desc))















