from db.database import Session
from models.expense import Expense
from datetime import datetime

#list of expense categories to pick from
CATEGORIES = ['Food', 'Transport', 'Shopping', 'Health', 'Entertainment', 'Utilities']

UNDERLINE= "\033[1;4m"
RESET = "\033[0m"

def run():
    session = Session()
    try:
        #get date
        date = input("Enter date (YYYY-MM-DD):").strip()
        date = datetime.strptime(date, "%Y-%m-%d")

        #show category list
        print(f"\n{UNDERLINE}Select a category{RESET}")
        for index, cat in enumerate(CATEGORIES, start=1):
            print(f"{index}. {cat}")
        category = input("Enter category number: ").strip()

        try:
            cat_index = int(category) #convert the input which is a string to an integer
            if 1 <= cat_index <= len(CATEGORIES):
                category = CATEGORIES[cat_index - 1]#get corresponding item from CATEGORIES list
            else:#if the user enters a number outside the valid range
                print("Invalid category number")
        except ValueError:#if the user enters a character that cant be converted to an integer
            print("Please enter a valid number")
            return#if it fails,it exits

        #get amount
        amount = input("Enter amount: ")
        #get description
        description = input("Enter description(optional): ")


        expense = Expense(
            date = date,
            category = category,
            amount = amount,
            description = description or None
        )

        session.add(expense)
        session.commit()
        print(" ✅ Expense added successfully")
        session.close()
    except Exception as e:
        print("Error", e)
    finally:
        session.close()

if __name__ == '__main__':
    run()