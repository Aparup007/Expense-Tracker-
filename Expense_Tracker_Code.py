import pickle
import os

# Initialize expenses dictionary or load existing data
expenses = {}

def load_expenses():
    global expenses
    if os.path.exists("expenses.pkl"):
        with open("expenses.pkl", "rb") as file:
            expenses = pickle.load(file)

def save_expenses():
    with open("expenses.pkl", "wb") as file:
        pickle.dump(expenses, file)

def show_menu():
    print("\nExpense Tracker Menu:")
    print("1. Add an Expense")
    print("2. View Expenses")
    print("3. Delete an Expense")
    print("4. View Expense Summary")
    print("5. Exit")

def add_expense():
    description = input("Enter a brief description of the expense: ")
    amount = float(input("Enter the amount spent: $"))
    category = input("Enter a category (e.g., Food, Transportation, Rent): ")
    
    if category not in expenses:
        expenses[category] = []
    
    expenses[category].append({"description": description, "amount": amount})
    save_expenses()
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    for category, items in expenses.items():
        print(f"{category} Expenses:")
        for idx, item in enumerate(items):
            print(f"{idx + 1}. Description: {item['description']}, Amount: ${item['amount']:.2f}")

def delete_expense():
    category = input("Enter the category to delete an expense from: ")
    if category in expenses:
        view_expenses()
        try:
            item_index = int(input("Enter the number of the expense to delete: ")) - 1
            if 0 <= item_index < len(expenses[category]):
                removed_item = expenses[category].pop(item_index)
                print(f"Expense deleted: {removed_item}")
                save_expenses()
            else:
                print("Invalid expense number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid expense number.")
    else:
        print(f"No expenses found in the category: {category}")

def view_summary():
    if not expenses:
        print("No expenses recorded yet.")
        return

    summary = {}
    for category, items in expenses.items():
        total_amount = sum(item["amount"] for item in items)
        summary[category] = total_amount
    
    print("\nExpense Summary:")
    for category, total_amount in summary.items():
        print(f"{category}: ${total_amount:.2f}")
    total_expenses = sum(summary.values())
    print(f"Total Expenses: ${total_expenses:.2f}")

if __name__ == "__main__":
    load_expenses()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            view_summary()
        elif choice == "5":
            save_expenses()
            print("Exiting Expense Tracker. Your data has been saved.")
            break
        else:
            print("Invalid choice. Please try again.")