from datetime import datetime
import calendar
from expense_manager import get_all_expenses


import calendar
from expense_manager import get_all_expenses


def remaining_days_in_month(month, today_date):
    total_days = calendar.monthrange(2025, month)[1]

    if today_date < 1 or today_date > total_days:
        return None

    return total_days - today_date

def total_expense():
    expenses = get_all_expenses()
    total = 0.0

    for e in expenses:
        parts = e.split("|")
        if len(parts) < 3:
            continue
        try:
            total += float(parts[2]) 
        except ValueError:
            continue

    return total
def remaining_balance(budget):
    return budget - total_expense()


def budget_warning(budget):
    used = total_expense()

    if budget == 0:
        return "No budget set."

    percent = (used / budget) * 100

    if percent >= 90:
        return "CRITICAL WARNING: Budget almost exhausted!"
    elif percent >= 70:
        return "WARNING: Budget usage above 70%"
    else:
        return "Budget usage under control."
