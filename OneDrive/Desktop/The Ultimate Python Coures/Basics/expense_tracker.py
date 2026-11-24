# Daily Expense Tracker
# This program helps users record and manage daily expenses.

expenses = []

# Function to add a new expense
def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter category (Food/Travel/Shopping/Other): ")

    # Store all expense details
    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense added successfully!")

# Function to display expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\\nYour Expenses:")

    for expense in expenses:
        print(
            expense["name"],
            "|", expense["category"],
            "| Rs.", expense["amount"]
        )

# Function to calculate total expenses
def calculate_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total expenses: Rs.", total)

# Main menu
while True:
    print("\\n===== DAILY EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice. Please try again.")
