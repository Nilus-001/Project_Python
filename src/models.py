# -------------------------------------------------------------------------------------------------
from src.exceptions import LibraryError


# ------------------------------------ Book ---------------------------------------------
class Book:


    def __init__(self, title:str, author:str, isbn="NA"):
        self._title = title
        self._author = author
        self._isbn = isbn

    def __str__(self)->str:
        return f'{self._title} by {self._author} with {self._isbn}'


    def get_data(self) -> dict:
        return {
            "title": self._title,
            "author": self._author,
            "isbn": self._isbn
        }


    def get_title(self):
        return self._title
    def get_author(self):
        return self._author
    def get_isbn(self):
        return self._isbn

# ------------------------------------ Digital Book ---------------------------------------------

class DigitalBook(Book):

    def __init__(self, title:str, author :str, file_scale:int, isbn="NA"):
        super().__init__(title, author, isbn)
        self._file_scale = file_scale

    def __str__(self)->str:
        return super().__str__() + f" -- {self._file_scale}MB"


    def get_data(self)->dict:
        data = super().get_data()
        data.update({
            "file_scale": int(self._file_scale)
        })
        return data
    def get_file_scale(self):
        return self._file_scale

# ------------------------------------ Library ---------------------------------------------

class Library:
    def __init__(self, name:str):
        self.name = name
        self.list_of_books = []



    def add_book(self,book):
        """Adds a book to the library's collection."""
        for ele in self.list_of_books:
            if book.get_isbn() == ele.get_isbn():
                raise LibraryError("Book with this ISBN already exists in the library.", 4089)

        self.list_of_books.append(book)


    def remove_book_by_isbn(self,isbn:str) ->bool:
        """Removes a book from the library's collection by its ISBN."""

        for book in self.list_of_books:
            if book.get_isbn() == isbn:
                self.list_of_books.remove(book)
                print(f'Book {book.get_title()} removed successfully.')
                return True
        print("Book not found.")
        return False


    def research_by_title(self,title:str) ->list:
        """Searches for books by title."""
        result = []

        for book in self.list_of_books:
            if book.get_title().upper().find(title.upper()) != -1:
                result.append(book.get_title())
        return result


    def research_by_author(self,author:str) ->list:
        """Searches for books by author."""
        result = []

        for book in self.list_of_books:
            if book.get_author().upper().find(author.upper()) != -1:
                result.append(f"{book.get_title()} by {book.get_author()}")
        return result


    def get_list_of_books(self)->list:
        """Returns a list of all books in the library."""
        return [book.__str__() for book in self.list_of_books]

