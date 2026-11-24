# Daily Expense Tracker
# This program helps users record and manage daily expenses.

# Store all expenses in a list
expenses = []

# Function to add a new expense
def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))

    # Store expense details in a dictionary
    expense = {"name": name, "amount": amount}

    # Add the expense to the list
    expenses.append(expense)

    print("Expense added successfully!")

# Function to display all expenses
def view_expenses():
    # Check if the list is empty
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\\nYour Expenses:")

    # Display each expense
    for expense in expenses:
        print(expense["name"], "-", expense["amount"])

# Function to calculate total expenses
def calculate_total():
    total = 0

    # Add every expense amount
    for expense in expenses:
        total += expense["amount"]

    print("Total expenses:", total)

# Main menu of the program
while True:
    print("\\n===== DAILY EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Handle menu selection
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
