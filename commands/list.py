from models.expense import Expense
from db.database import Session
from tabulate import tabulate
from colorama import init, Fore,Back,Style
init(autoreset=True)


def run(cat_filter = None, date_filter = None):
    session = Session()

    query = session.query(Expense)

    if cat_filter:
        query = query.filter(Expense.category.like(f"%{cat_filter}%"))

    if date_filter:
        query = query.filter(Expense.date.like(f"%{date_filter}%"))

    expenses = query.order_by(Expense.date).all()


    if expenses:
        rows = [
            [expense.date.date(), expense.category, f"${expense.amount}", expense.description]
            for expense in expenses
        ]
        print(Fore.YELLOW + Style.DIM + tabulate(rows, tablefmt="fancy_grid", colalign= ("center", "center", "left", "right"), headers=["DATE", "CATEGORY", "AMOUNT", "DESCRIPTION"]))
    else:
        print(Fore.RED + Style.NORMAL + "No expenses found")

    session.close()

if __name__=='__main__':
    run()

