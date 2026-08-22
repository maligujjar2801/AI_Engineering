def add_expense():
    category = input("Catogary: ")
    amount = int(input("Amount: "))
    description = input("Description: ")
    with open("Expense.txt","a") as file:
        file.write(f"2026-08-19 | {category} | {amount} | {description}"'\n')

def veiw_expenses():
    with open("Expense.txt","r") as file:
        lines = file.readlines()
        print("========== EXPENSES ==========\n")
        i = 1
        for line in lines:
            parts = line.split("|")
            catogary = parts[1]
            amount = parts[2]
            description = parts[3]
            catogary = catogary.strip()
            amount = amount.strip()
            description = description.strip()
            print(f"{i}. {catogary:<15} Rs.{amount:<6} {description}")
            i += 1

def calculate_total():
    with open("Expense.txt","r") as file:
            lines = file.readlines()
            total = 0
            print("========== EXPENSES ==========\n")
            for line in lines:
                parts = line.split("|")
                amount = parts[2]
                amount = amount.strip()
                total += int(amount)
            print("Total Expenses: ",total)

def search_expenses():
    category = input("Enter Category: ")
    category = category.capitalize()
    with open("Expense.txt","r") as file:
        lines = file.readlines()
        total = 0
        i = 1
        print("========== SEARCH RESULTS ==========\n")
        for line in lines:
            parts = line.split("|")
            amount = parts[2]
            description = parts[3]
            parts = [part.strip() for part in parts]
            if parts[1] == category :
                print(f"{i}. {category:<15} Rs.{amount:<6} {description}")
                i += 1
        if parts[1].strip() != category :
            print("No expenses found for category: ",category)

def delete_expense():
    veiw_expenses()
    n = int(input("Enter expense number to delete: "))
    n -= 1
    try:
        with open("Expense.txt","r") as file :
            lines = file.readlines()
            del lines[n]
            end = len(lines)
            with open("Expense.txt",'w') as file:
                for i in range(end):
                        file.write(lines[i])
        print("Expense deleted succesfully..!")
    except IndexError:
        print("Enter an existing index...!")

while True:

    print('''========================================
            PERSONAL EXPENSE TRACKER
    ========================================''')
    print('''
    1. Add Expense
    2. View Expenses
    3. Calculate Total
    4. Search Expenses
    5. Delete Expense
    6. Exit''')

    choice = int(input("\nEnter your choice:"))

    if choice == 1 :
        add_expense()

    elif choice == 2 :
        veiw_expenses()

    elif choice == 3 :
        calculate_total()

    elif choice == 4 :
        search_expenses()

    elif choice == 5 :
        delete_expense()

    elif choice == 6 :
        print("Exited succesfully...!")
        break

    else :
        print("Enter a valid choice(1-6) !")