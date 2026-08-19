# Expense Tracker

expenses = []


def add_expense():
    print("\n--- Add Expense ---")

    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)

    print("Expense added successfully!")


def view_expenses():
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses found.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(f"\nExpense {i}")
        print("Date:", expense["date"])
        print("Category:", expense["category"])
        print("Amount: ₹", expense["amount"])
        print("Description:", expense["description"])


def total_expenses():
    total = sum(expense["amount"] for expense in expenses)

    print("\n--- Total Expenses ---")
    print(f"Total Spending: ₹{total:.2f}")


def category_expenses():
    category = input("\nEnter category to search: ")

    found = False
    total = 0

    print(f"\n--- Expenses in {category} ---")

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print(
                expense["date"],
                "| ₹" + str(expense["amount"]),
                "|", expense["description"]
            )

            total += expense["amount"]
            found = True

    if found:
        print(f"\nTotal spent on {category}: ₹{total:.2f}")
    else:
        print("No expenses found in this category.")


def main():
    while True:

        print("\n==============================")
        print("       EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Search by Category")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            try:
                add_expense()
            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            category_expenses()

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
