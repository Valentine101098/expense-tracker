# 💸 CLI Expense Tracker

A command-line personal expense tracker built with Python, SQLite, and SQLAlchemy. Add, list, summarize, and search your expenses easily from the terminal. Includes a data seeding script with fake data using the `Faker` library.

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone git@github.com:Valentine101098/expense-tracker.git

cd expense-tracker-valentine-wanjiru
```

### 2. Set Up the Virtual Environment

Using `pipenv`:

```bash
pipenv install
```

This will install:
- `sqlalchemy`
- `tabulate`
- `faker`
- `python-dateutil`

> Make sure you have Python 3.8 installed as specified in the `Pipfile`.

---

## 📊 Seed the Database

To populate your database with sample expense data:

```bash
pipenv run seed-db
```

This will:
- Clear existing records
- Generate 20 fake expenses with random categories, descriptions, and amounts between 50 and 250

---

## 🚀 Run the Tracker

### ✅ Interactive Mode

Run this to launch an interactive menu:

```bash
pipenv run tracker
```

You'll see:

```
1. Add expense
2. List expenses
3. Summary
4. Search
5. Exit
```

Each option will walk you through the process.

---

### 🛠 Command Mode

You can also run individual commands directly without the menu:

| Command                         | Description                      |
|----------------------------------|----------------------------------|
| `pipenv run tracker add`        | Add a new expense                |
| `pipenv run tracker list`       | List all expenses                |
| `pipenv run tracker summary`    | Show grouped spending stats      |
| `pipenv run tracker search`     | Search by category, date, or description |

---

## 📁 Project Structure

```
.
├── db/
│   └── database.py           # DB engine & session
├── models/
│   └── expense.py            # SQLAlchemy model definition
├── commands/
│   ├── add.py                # Add new expense
│   ├── list.py               # View expenses
│   ├── summary.py            # Monthly/category totals
│   ├── search.py             # Filtered search
├── tracker.py                # CLI entry point
├── seed.py                   # Seed file with fake data
├── Pipfile                   # Pipenv dependencies
├── Pipfile.lock
└── README.md
```

---

## 🧪 Features

- ✅ Add new expenses
- 📋 List all recorded expenses
- 📊 Summarize expenses by **category** and **month**
- 🔍 Search by **date**, **category**, or **description**
- 🧪 Seed with fake data using `Faker`

---

## 🧼 Tips for Better Terminal Output

- Uses ANSI escape codes for underlining and formatting
- Tabulates data using `tabulate` for clean column views
- Use `colorama` (optional) for colored outputs

---

## 📝 Notes

- Expense amounts are constrained between **50 and 250**
- Categories are limited to:
  - Food, Transport, Shopping, Health, Entertainment, Utilities
- Uses a local **SQLite database** stored in `expenses.db`

---

## 👨‍💻 Author

Built with ❤️ by Valentine