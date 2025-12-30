from expense_manager import get_all_expenses


def calculate_member_totals():
    expenses = get_all_expenses()
    summary = {}

    for e in expenses:
        parts = e.split("|")
        if len(parts) < 5:
            continue

        member = parts[4]
        try:
            amount = float(parts[2])
        except ValueError:
            continue

        summary[member] = summary.get(member, 0) + amount

    return summary
