from expense_manager import (
    add_expense,
    delete_expense,
    get_all_expenses,
    expense_id_exists,
    update_expense
)
from member_manager import calculate_member_totals
from analytics import (
    total_expense,
    remaining_balance,
    budget_warning,
    remaining_days_in_month
)
from file_handler import archive_month

from file_handler import load_config, save_config

budget, month = load_config()

if budget is None or month is None:
    budget = float(input("Enter monthly budget: "))
    month = int(input("Enter month number (1-12): "))
    save_config(budget, month)


while True:
    print("\n--- Room Expense Manager ---")
    print("1. Add Expense")
    print("2. Delete Expense")
    print("3. View All Expenses")
    print("4. Remaining Balance")
    print("5. Member Contribution Summary")
    print("6. Update Expense")
    print("7. Monthly Reset")
    print("8. Exit")

    choice = input("Choose option: ")

    # 1. ADD EXPENSE
    if choice == "1":
        eid = input("Expense ID: ")

        if expense_id_exists(eid):
            print("⚠ Expense ID already exists.")
            print("Please delete the existing entry or use a new ID.")
            continue

        date = input("Date (dd-mm-yyyy): ")
        amount = input("Amount: ")
        category = input("Category: ")
        member = input("Paid by: ")

        expense = f"{eid}|{date}|{amount}|{category}|{member}"
        add_expense(expense)

        print("Expense added successfully.")
        print(budget_warning(budget))

    # 2. DELETE EXPENSE
    elif choice == "2":
        eid = input("Enter Expense ID to delete: ")
        delete_expense(eid)
        print("Expense deleted.")

    # 3. VIEW ALL EXPENSES
    elif choice == "3":
        expenses = get_all_expenses()
        if not expenses:
            print("No expenses recorded.")
        else:
            for e in expenses:
                print(e)

    # 4. REMAINING BALANCE + REMAINING DAYS
    elif choice == "4":
        print("Total Expense:", total_expense())
        print("Remaining Balance:", remaining_balance(budget))

        today = int(input("Enter today's date: "))
        days_left = remaining_days_in_month(month, today)

        if days_left is None:
            print("Invalid date entered.")
        else:
            print("Remaining days in month:", days_left)

    # 5. MEMBER CONTRIBUTION SUMMARY
    elif choice == "5":
        summary = calculate_member_totals()
        if not summary:
            print("No expenses recorded yet.")
        else:
            print("\n--- Member-wise Expense Summary ---")
            for member, amt in summary.items():
                print(f"{member} spent total: ₹{amt}")

    # 6. UPDATE EXPENSE
    elif choice == "6":
        eid = input("Enter Expense ID to update: ")

        if not expense_id_exists(eid):
            print("Expense ID not found.")
            continue

        print("1. Update Amount")
        print("2. Update Member Name")
        opt = input("Choose option: ")

        if opt == "1":
            new_amt = input("Enter new amount: ")
            update_expense(eid, new_amount=new_amt)
            print("Amount updated successfully.")

        elif opt == "2":
            new_member = input("Enter new member name: ")
            update_expense(eid, new_member=new_member)
            print("Member name updated successfully.")

        else:
            print("Invalid update option.")

    # 7. MONTHLY RESET
    elif choice == "7":
        archive_month(get_all_expenses())

        open("expenses_data.txt", "w").close()

        budget = float(input("Enter new month budget: "))
        month = int(input("Enter new month number (1-12): "))
        save_config(budget, month)
        print("New month initialized.")

    # 8. EXIT
    elif choice == "8":
        print("Exiting system.")
        break

    else:
        print("Invalid option.")
