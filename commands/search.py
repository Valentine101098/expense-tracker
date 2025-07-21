from models.expense import Expense
from db.database import Session
from tabulate import tabulate
from colorama import init, Fore,Back,Style
init(autoreset=True)

def run():
    session = Session()
    query = session.query(Expense)

    print(Fore.CYAN + Style.DIM + "\n1. By category \n2. By date \n3. By description keyword \n4. Back to menu")

    choice = input("\nChoose search type: ")

    if choice == "1":
        keyword = input("\nEnter category name: \n").strip()
        results = query.filter(Expense.category.like(f"%{keyword}%")).all()

    elif choice == "2":
        date = input("\nEnter date (YYYY-MM-DD):\n ").strip()
        results = query.filter(Expense.date.like(f"%{date}%")).all()

    elif choice == "3":
        keyword = input("\nEnter description keyword: \n").split()
        results = query.filter(Expense.description.like(f"%{keyword}%")).all()

    elif choice == "4":
        session.close()
        return

    else:
        print("\nInvalid choice!")
        session.close()
        return

    if results:
        rows = [
            [expense.date.date(), expense.category, f"${expense.amount}", expense.description]
            for expense in results
        ]
        print(Fore.YELLOW + Style.DIM + tabulate(rows, tablefmt="fancy_grid", colalign= ("center", "center", "left", "right"), headers=["DATE", "CATEGORY", "AMOUNT", "DESCRIPTION"]))
    else:
        print(Fore.RED + Style.NORMAL + "No expenses found")


    session.close()