from models.expense import Expense
from db.database import Session

def run():
    session = Session()
    query = session.query(Expense)

    print("\n1. By category \n2. By date \n3. By description keyword \n4. Back to menu")

    choice = input("Choose search type: ")

    if choice == "1":
        keyword = input("Enter category name: ").split()
        results = query.filter(Expense.category.like(f"%{keyword}%")).all()

    elif choice == "2":
        date = input("Enter date (YYYY-MM-DD): ").strip()
        results = query.filter(Expense.date.like(f"%{date}%")).all()

    elif choice == "3":
        keyword = input("Enter description keyword: ").split()
        results = query.filter(Expense.description.like(f"%{keyword}%")).all()

    elif choice == "4":
        session.close()
        return

    else:
        print("Invalid choice")
        session.close()
        return

    for expense in results:
        print(f"{expense.date.date()} | {expense.category:<12} | ${expense.amount:<6} | {expense.description}")

    session.close()