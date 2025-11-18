from src.exceptions import LibraryError
from src.file_manager import LibraryWithFile
from src.models import Book, DigitalBook, Library

b1 = Book("86","Asato Asato","4384646984123")
b2 = Book("Maze Runner","James Dashner","9780439023528")
b3 = DigitalBook("Harry Potter ","J.K. Rowling",1652,"9780747532699")
b4 = Book("The Hobbit","J.R.R. Tolkien","9780261102217")
b5 = Book("Fahrenheit 451","Ray Bradbury","9781451673319")

libi = Library("LIBERARITY")
# lib.add_book(b1)
# lib.add_book(b2)
# lib.add_book(b3)
# lib.add_book(b4)
# lib.add_book(b5)

# lib.remove_book_by_isbn("9780261102217")

lib = LibraryWithFile("Library")


try :

    lib.import_data()
    print(lib.get_data())
    print(lib.get_list_of_books())
    lib.export_csv("books_export.csv")

    print(lib.research_by_author("j."))
    print(lib.research_by_title("a"))









except LibraryError as e:
    print(f"Library Error [{e.code}]: {e}")