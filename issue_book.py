<<<<<<< HEAD
from utils import books, issue_books

def issue():
    book_name = input("Enter book name: ").upper()
    if book_name in books:
        books.remove(book_name)
        issue_books.append(book_name)
        print("Book assigned successfully")
    else:
=======
from utils import books, issue_books

def issue():
    book_name = input("Enter book name: ").upper()
    if book_name in books:
        books.remove(book_name)
        issue_books.append(book_name)
        print("Book assigned successfully")
    else:
>>>>>>> 0d0591410b0ddd3baf686d4c2787a8566ce69a23
        print("Book not available")