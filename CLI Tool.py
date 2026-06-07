import csv
import sys
from pathlib import Path

def rename(old_name, new_name):
    file = Path(old_name)
    if file.exists():
        file.rename(new_name)
        print(f"File renamed from { old_name } to { new_name}")
    else:
        print(f"File {old_name} not found")

def export(filename, data, fieldnames):
    with open(filename, "w", newline="", encoding = "utf-8") as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"File {filename} exported to CSV")

while True:
    print("CLI Tool:\n")
    print("Functions:\n1. rename files \n2. export file to CSV \n3. Exit \n")
    option = int(input("Your choice: "))
    match option:
        case 1:
            old_name = str(input("Enter file name: ").strip())
            new_name = str(input("Enter new file name: ").strip())
            rename(old_name, new_name)
        case 2:
            filename = str(input("Enter file name: "))
            fields_input = input("Enter headers/fieldnames (separated by comma): ")
            fieldnames = [field.strip() for field in fields_input.split(",")]

            data =  []
            print("\nNow enter the row data ( type 'done' when finished): ")
            while True:
                row = {}
                for field in fieldnames:
                    val = input("Enter the value for field (type 'done' when finished): ")
                    row[field] = val
                data.append(row)

                cont = input("Add another row? (y/n): ").lower()
                if cont != "y":
                    break
            export(filename, data, fieldnames)

        case 3:
            sys.exit(1)
        case _:
            print("Invalid choice")