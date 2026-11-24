# Daily Expense Tracker
# This program helps users record and manage daily expenses.

expenses = []
budget = 0

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
    total = sum(expense["amount"] for expense in expenses)
    print("Total expenses: Rs.", total)

# Function to delete an expense
def delete_expense():
    view_expenses()

    if not expenses:
        return

    try:
        number = int(input("Enter expense number to delete: "))

        if 1 <= number <= len(expenses):
            removed = expenses.pop(number - 1)
            print(removed["name"], "expense deleted successfully!")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to display category-wise totals
def category_summary():
    if not expenses:
        print("No expenses recorded yet.")
        return

    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount

    print("\\nCategory-wise Summary:")

    for category, total in totals.items():
        print(category, ":", "Rs.", total)

# Function to edit an expense
def edit_expense():
    view_expenses()

    if not expenses:
        return

    try:
        number = int(input("Enter expense number to edit: "))

        if not 1 <= number <= len(expenses):
            print("Invalid expense number.")
            return

        expense = expenses[number - 1]

        new_name = input("Enter new name (Enter to keep current): ")
        if new_name:
            expense["name"] = new_name

        new_amount = input("Enter new amount (Enter to keep current): ")
        if new_amount:
            try:
                amount = float(new_amount)
                if amount > 0:
                    expense["amount"] = amount
                else:
                    print("Amount must be greater than zero.")
            except ValueError:
                print("Invalid amount. Keeping old amount.")

        new_category = input("Enter new category (Enter to keep current): ")
        if new_category:
            expense["category"] = new_category

        print("Expense updated successfully!")

    except ValueError:
        print("Please enter a valid number.")

# Function to set a budget
def set_budget():
    global budget

    while True:
        try:
            amount = float(input("Enter your budget: "))

            if amount <= 0:
                print("Budget must be greater than zero.")
                continue

            budget = amount
            print("Budget set successfully!")
            break

        except ValueError:
            print("Please enter a valid amount.")

# Function to check budget usage
def check_budget():
    if budget <= 0:
        print("Please set your budget first.")
        return

    total = sum(expense["amount"] for expense in expenses)

    print("\\nBudget:", budget)
    print("Total spent:", total)
    print("Remaining budget:", budget - total)

    # Check whether expenses have exceeded the budget
    if total > budget:
        print("Warning: You have exceeded your budget!")
    elif total == budget:
        print("You have reached your budget limit.")
    else:
        print("You are within your budget.")

# Main menu
while True:
    print("\\n===== DAILY EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Delete Expense")
    print("5. Category Summary")
    print("6. Edit Expense")
    print("7. Set Budget")
    print("8. Check Budget")
    print("9. Exit")

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
        category_summary()
    elif choice == "6":
        edit_expense()
    elif choice == "7":
        set_budget()
    elif choice == "8":
        check_budget()
    elif choice == "9":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice. Please try again.")
