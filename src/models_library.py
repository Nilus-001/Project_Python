import datetime

from src.exceptions import LibraryErrors
from src.models_book import Book
from src.models_user import User


# ------------------------------------ Library ---------------------------------------------


class Library:
    def __init__(self, name:str):

        if not isinstance(name, str) or name.strip() == "" or any(c in name for c in ['<', '>', ':', '/', '\\', '|', '?', '*']):
            raise LibraryErrors.INVALID_LIBRARY_NAME.value

        self.name = name
        self.list_of_books = []
        self.list_of_users = []

    def add_user(self,user:User):
        if not isinstance(user,User):
            raise LibraryErrors.INVALID_USER_TYPE.value

        for ele in self.list_of_users:
            if user.username == ele.username:
                raise LibraryErrors.USER_ALREADY_EXISTS.value

        self.list_of_users.append(user)
        return True



    def add_book(self,book:Book):
        """Adds a book to the library's collection."""
        if not isinstance(book,Book):
            raise LibraryErrors.INVALID_BOOK_TYPE.value

        for ele in self.list_of_books:
            if book.get_isbn() == ele.get_isbn():
                raise LibraryErrors.ISBN_ALREADY_EXISTS.value

        self.list_of_books.append(book)
        return True


    def remove_book_by_isbn(self,isbn:str) ->bool:
        """Removes a book from the library's collection by its ISBN."""
        if not isinstance(isbn, str) or isbn.strip() == "" or len(isbn) != 13:
            raise LibraryErrors.INVALID_BOOK_ISBN.value

        for book in self.list_of_books:
            if book.get_isbn() == isbn:
                self.list_of_books.remove(book)
                print(f'Book {book.get_title()} removed successfully.')
                return True
        raise LibraryErrors.BOOK_NOT_FOUND.value



    def research_by_title(self,title:str) ->list:
        """Searches for books by title."""


        result = []

        for book in self.list_of_books:
            if book.get_title().upper().find(title.upper()) != -1:
                result.append(book)
        return result


    def research_by_author(self,author:str) ->list:
        """Searches for books by author."""

        result = []

        for book in self.list_of_books:
            if book.get_author().upper().find(author.upper()) != -1:
                result.append(book)
        return result

    def check_date(self): #do not work (no time to finish)
        for user in self.list_of_users:
            for key,value in user.book_borrow.items():
                print(value)
                if value > datetime.datetime.now():
                    print((value - datetime.datetime.now()).days)

                    user.debt = 0.5 * (value - datetime.datetime.now()).days


