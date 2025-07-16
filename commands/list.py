from models.expense import Expense
from db.database import Session

def run(cat_filter = None, date_filter = None):
    session = Session()

    query = session.query(Expense)

    if cat_filter:
        query = query.filter(Expense.category.like(f"%{cat_filter}%"))

    if date_filter:
        query = query.filter(Expense.date.like(f"%{date_filter}%"))

    expenses = query.order_by(Expense.date).all()

    for expense in expenses:
        print(f"{expense.date.date()} | {expense.category:<15} | ${expense.amount:<6} | {expense.description}")

    session.close()

if __name__=='__main__':
    run()

