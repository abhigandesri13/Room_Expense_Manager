import os

EXPENSE_FILE = "expenses_data.txt"
MEMBER_FILE = "members_data.txt"
ARCHIVE_FILE = "archive/month_backup.txt"

CONFIG_FILE = "config.txt"


def load_config():
    try:
        with open(CONFIG_FILE, "r") as f:
            lines = f.readlines()
            if len(lines) != 2:
                return None, None
            budget = float(lines[0].strip())
            month = int(lines[1].strip())
            return budget, month
    except:
        return None, None


def save_config(budget, month):
    with open(CONFIG_FILE, "w") as f:
        f.write(str(budget) + "\n")
        f.write(str(month) + "\n")

def load_data(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_data(filename, data):
    with open(filename, "w") as file:
        for line in data:
            file.write(line + "\n")

def archive_month(expenses):
    with open(ARCHIVE_FILE, "a") as file:
        file.write("\n--- New Month Archive ---\n")
        for exp in expenses:
            file.write(exp + "\n")
