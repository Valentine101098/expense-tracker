from models.expense import Expense
from sqlalchemy import func, desc
from db.database import Session

UNDERLINE = "\033[4m"
RESET = "\033[0m"
def run():
    session = Session()

    #grouping total by category
    print(f"\n{UNDERLINE}Total spending by category:{RESET}")
    results = session.query(
        Expense.category,
        func.sum(Expense.amount)).group_by(Expense.category).all()

    for category, total in results:
        print(f"{category:<15} | ${round(total,2)}")

    #highlight top category
    top_category = session.query(
        Expense.category, func.sum(Expense.amount).label("total")).group_by(Expense.category).order_by(
        desc("total")).first()

    print(f"\nYou spent the most on {top_category}")

    #group total by month
    print(f"\n{UNDERLINE}Total spending by month:{RESET}")
    results = session.query(
        func.strftime('%Y-%m', Expense.date).label("month"),
        func.sum(Expense.amount)).group_by("month").all()

    for month,total in results:
        print(f"{month:<10} | ${round(total,2)}")

    #highlight top month
    top_month = session.query(
        func.strftime('%Y-%m', Expense.date).label("month"),
        func.sum(Expense.amount).label("total")).group_by("month").order_by(
        desc("total")).first()

    print(f"\n{top_month} had the highest spending")

    session.close()

if __name__ == '__main__':
        run()
