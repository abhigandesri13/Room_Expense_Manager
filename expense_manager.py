from file_handler import load_data, save_data

EXPENSE_FILE = "expenses_data.txt"

def add_expense(expense):
    expenses = load_data(EXPENSE_FILE)
    expenses.append(expense)
    save_data(EXPENSE_FILE, expenses)

def expense_id_exists(expense_id):
    expenses = load_data(EXPENSE_FILE)
    for e in expenses:
        if e.startswith(expense_id + "|"):
            return True
    return False

def update_expense(expense_id, new_amount=None, new_member=None):
    expenses = load_data(EXPENSE_FILE)
    updated_expenses = []

    for e in expenses:
        parts = e.split("|")
        if parts[0] == expense_id:
            if new_amount is not None:
                parts[2] = str(new_amount)
            if new_member is not None:
                parts[4] = new_member
            e = "|".join(parts)
        updated_expenses.append(e)

    save_data(EXPENSE_FILE, updated_expenses)

def delete_expense(expense_id):
    expenses = load_data(EXPENSE_FILE)
    updated = [e for e in expenses if not e.startswith(expense_id + "|")]
    save_data(EXPENSE_FILE, updated)

def get_all_expenses():
    return load_data(EXPENSE_FILE)
