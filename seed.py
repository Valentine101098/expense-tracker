from faker import Faker
from models.expense import Expense
from db.database import Session
from random import randint
from random import choice


session = Session()
fake = Faker()

print("Seeding expenses...")

#pick from this category list
CATEGORIES = ['Food', 'Transport', 'Shopping', 'Health', 'Entertainment', 'Utilities']

#delete all existing rows
session.query(Expense).delete()
session.commit()

#create new seed data
expenses = [
    Expense(
        date = fake.date_this_year(),
        category = choice(CATEGORIES),
        amount = randint(10, 2500),
        description = fake.sentence(nb_words=5)
    )
for _ in range(20)
]
#save new rows
session.add_all(expenses)
session.commit()
session.close()

print("Seeding complete!")