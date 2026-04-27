<<<<<<< HEAD
from datetime import datetime

library = {
    "Python Basics": {"available": True},
    "Data Structures": {"available": True},
    "AI Fundamentals": {"available": True}
}

issued_books = {}

def calculate_fine(days_late):
    fine = 0
    week = 1
    
    while days_late > 0:
        if week == 1:
            rate = 10
        elif week == 2:
            rate = 10 * 2
        else:
            rate = 10 * 2 * 3
        
        fine += rate
        days_late -= 1
        week += 1
    
    return fine

def issue_book():
    print("\nAvailable Books:")
    for book, info in library.items():
        if info["available"]:
            print("-", book)

    book = input("\nEnter book name: ")

    if book in library and library[book]["available"]:
        student = input("Enter student name: ")
        days = int(input("Enter number of days: "))
        
        issue_date = datetime.now()
        
        issued_books[book] = {
            "student": student,
            "issue_date": issue_date,
            "days": days
        }
        
        library[book]["available"] = False

        print("\n✅ Book Issued Successfully!")
    else:
        print("\n❌ Book not available!")

def return_book():
    book = input("\nEnter book name to return: ")

    if book in issued_books:
        data = issued_books[book]
        return_date = datetime.now()

        days_used = (return_date - data["issue_date"]).days
        allowed_days = data["days"]

        if days_used > allowed_days:
            late_days = days_used - allowed_days
            fine = calculate_fine(late_days)
            print(f"\n⚠ Late return! Fine = ₹{fine}")
        else:
            print("\n✅ Book returned on time!")

        library[book]["available"] = True
        del issued_books[book]

    else:
        print("\n❌ Book not found!")

def menu():
    while True:
        print("\n===== LIBRARY MENU =====")
        print("1. View Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            for book, info in library.items():
                status = "Available" if info["available"] else "Issued"
                print(f"{book} → {status}")

        elif choice == "2":
            issue_book()

        elif choice == "3":
            return_book()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

menu()
=======
from add_books import add
from issue_book import issue
from show_books import show
from return_book import return_book

def library():
    while True:
        print("\n1. Add Book")
        print("2. Show Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice==1:   add()
        elif choice==2: show()
        elif choice==3: issue()
        elif choice==4: return_book()
        elif choice==5: 
            print("Thank you")
            break
        else:
            print("Invalid choice")
            
library()
>>>>>>> 0d0591410b0ddd3baf686d4c2787a8566ce69a23
