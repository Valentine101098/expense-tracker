import sys
from commands import add, list, summary, search

def main():
    if len(sys.argv) == 1: #Checks that the script was run without any extra command-line arguments ie just pipenv run tracker
        # Interactive Mode
        while True:
            print("\n1. Add expense \n2. List expenses \n3. Summary \n4. Search \n5. Exit")
            choice = input("Select option: ")
            if choice == "1":
                print("Adding New Expense...")
                add.run()
            elif choice == "2":
                print("Listing Expenses...")
                list.run()
            elif choice == "3":
                print("Summary...")
                summary.run()
            elif choice == "4":
                print("Search by date, category or description...")
                search.run()
            elif choice == "5":
                print("Goodbye")
                break
            else:
                print("Invalid option. Please try again")
    else:
        # Command Mode
        command = sys.argv[1] #checks what command is after pipenv run tracker
        if command == "add": # pipenv run tracker add
            add.run()
        elif command == "list": # pipenv run tracker list
            list.run()
        elif command == "summary": # pipenv run tracker summary
            summary.run()
        elif command == "search": # pipenv run tracker search
            search.run()
        else:
            print("Unknown command. Try add, list or summary")

if __name__ == "__main__":
    main()
