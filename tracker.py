import sys
from commands import add, list, summary, search
from colorama import init, Fore,Back,Style
init(autoreset=True)

def main():
    if len(sys.argv) == 1: #Checks that the script was run without any extra command-line arguments ie just pipenv run tracker
        # Interactive Mode
        while True:
            print(Fore.CYAN + Style.BRIGHT + "\n1.Add expense \n2.List expenses \n3.Summary \n4.Search \n5.Exit")
            choice = input("\nSelect option:")
            if choice == "1":
                print("➕ Adding New Expense...\n")
                add.run()
            elif choice == "2":
                print("📋 Listing Expenses...\n")
                list.run()
            elif choice == "3":
                print("📊 Summary...\n")
                summary.run()
            elif choice == "4":
                print("🔎 Search by date, category or description...\n")
                search.run()
            elif choice == "5":
                print("See you next time! \n")
                break
            else:
                print("✖️ Invalid option. Please put a number from 1-5\n")
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
            print("⚠️ Unknown command. Try add, list or summary")

if __name__ == "__main__":
    main()
