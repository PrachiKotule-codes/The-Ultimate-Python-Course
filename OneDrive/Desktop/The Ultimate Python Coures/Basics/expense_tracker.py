# Daily Expense Tracker
# This program helps users record and manage daily expenses.

expenses = []

# Function to get a valid expense amount
def get_amount():
    while True:
        try:
            amount = float(input("Enter expense amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            return amount

        except ValueError:
            print("Please enter a valid numeric amount.")

# Function to add a new expense
def add_expense():
    name = input("Enter expense name: ")
    amount = get_amount()
    category = input("Enter category (Food/Travel/Shopping/Other): ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense added successfully!")

# Function to display all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\\nYour Expenses:")

    for index, expense in enumerate(expenses, start=1):
        print(
            index, ".", expense["name"],
            "|", expense["category"],
            "| Rs.", expense["amount"]
        )

# Function to calculate total expenses
def calculate_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total expenses: Rs.", total)

# Function to delete an expense
def delete_expense():
    view_expenses()

    if not expenses:
        return

    try:
        number = int(input("Enter expense number to delete: "))

        # Check whether the selected number is valid
        if 1 <= number <= len(expenses):
            removed = expenses.pop(number - 1)
            print(removed["name"], "expense deleted successfully!")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")

# Main menu
while True:
    print("\\n===== DAILY EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice. Please try again.")
