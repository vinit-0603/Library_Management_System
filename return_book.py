<<<<<<< HEAD
from utils import issue_books, books

def return_book():
    book_name = input("Enter book name: ").upper()
    if book_name in issue_books:
        issue_books.remove(book_name)
        books.append(book_name)
        print("Book returned")
    else:
=======
from utils import issue_books, books

def return_book():
    book_name = input("Enter book name: ").upper()
    if book_name in issue_books:
        issue_books.remove(book_name)
        books.append(book_name)
        print("Book returned")
    else:
>>>>>>> 0d0591410b0ddd3baf686d4c2787a8566ce69a23
        print("blablabla")