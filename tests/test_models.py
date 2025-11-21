from src.exceptions import LibraryError, LibraryErrors
from src.models_book import Book
from src.models_library import Library

from src.models_digital_book import DigitalBook
import pytest


# ------------------------------------ Library TEST ---------------------------------------------
@pytest.mark.parametrize("name,expected", [
    ("TestLib", None),
    ("Test.Lib", None),
    ("Test/Lib", LibraryErrors.INVALID_LIBRARY_NAME),
])
def test_creation_library(name, expected):
    if expected is None:
        lib = Library(name)
        assert lib.name == name
    else:
        with pytest.raises(LibraryError) as exc_info:
            Library(name)

        assert exc_info.value.code == expected.value.code




def test_add_book_to_library(empty_library, simple_book, simple_ebook):
    lib = empty_library

    lib.add_book(simple_book)
    books = lib.list_of_books

    assert len(books) == 1
    assert simple_book in books

    lib.add_book(simple_ebook)
    books = lib.list_of_books

    assert len(books) == 2
    assert simple_book in books
    assert simple_ebook in books


def test_add_duplicate_book_raises_error(simple_library, simple_book):
    lib = simple_library
    lib.add_book(simple_book)
    with pytest.raises(LibraryError) as exc_info:
        lib.add_book(simple_book)

    assert exc_info.value == LibraryErrors.ISBN_ALREADY_EXISTS.value


def test_remove_book_by_isbn(simple_library, simple_book):
    lib = simple_library
    lib.add_book(simple_book)

    lib.remove_book_by_isbn("0000000000001")

    assert len(lib.list_of_books) == 0


def test_remove_nonexistent_book_raises_error(simple_library,simple_book):
    lib = simple_library
    lib.add_book(simple_book)

    with pytest.raises(LibraryError) as excinfo:
        lib.remove_book_by_isbn("9999999999999")

    assert excinfo.value == LibraryErrors.BOOK_NOT_FOUND.value


def test_research_by_title(simple_library, simple_book, simple_ebook):
    lib = simple_library
    lib.add_book(simple_book)
    lib.add_book(simple_ebook)

    results = lib.research_by_title("Python")
    assert len(results) == 2
    assert "Python" in results[0]
    assert "Python e-book" in results[1]

def test_research_by_author(simple_library, simple_book, simple_ebook):
    lib = simple_library
    lib.add_book(simple_book)
    lib.add_book(simple_ebook)

    results = lib.research_by_author("A. Dev")
    assert len(results) == 2
    assert "Python by A. Dev" in results[0]
    assert "Python e-book by A. Dev" in results[1]









# ------------------------------------ Book TEST ---------------------------------------------
@pytest.mark.parametrize("title,author,isbn,expected", [
 ("Bonjour", "moi", "0000000000001",None),
 ("Bonjour, Le Retour", "moi", "0090072040001",None),
 ("Bonjour, Le Retour", "moi", "0090072040001",None),
 ("", "moi", "0000000000001", LibraryErrors.INVALID_BOOK_TITLE),
 (0, "moi", "0000000000001", LibraryErrors.INVALID_BOOK_TITLE),
 ("Il etait une fois", "", "1579632156756", LibraryErrors.INVALID_BOOK_AUTHOR),
 ("Heey", "un mec", "12345", LibraryErrors.INVALID_BOOK_ISBN),
 ("Heey", "un mec", "12345", LibraryErrors.INVALID_BOOK_ISBN),
 ])

def test_book_creation(title,author,isbn,expected):
    if expected is None:
        book = Book(title,author,isbn)
        assert book.get_title() == title
        assert book.get_author() == author
        assert book.get_isbn() == isbn
    else:
        with pytest.raises(LibraryError) as exc_info:
            Book(title,author,isbn)
        assert exc_info.value.code == expected.value.code










# ------------------------------------ E-Book TEST ---------------------------------------------
@pytest.mark.parametrize("title,author,file_scale,isbn,expected", [
    ("E-book 1", "Author 1", 3,"6666666666660", None),
    ("E-book 2", "Author 2",568, "0000000000001", None),
    (5, "Author 2", 568,"0007007500401", LibraryErrors.INVALID_BOOK_TITLE),
    ("Files ", "moi", -1,"0070000000001", LibraryErrors.INVALID_DIGITAL_BOOK_FILE_SCALE),
    ("Les Lois ", "Albert","568", "0200000900831", LibraryErrors.INVALID_DIGITAL_BOOK_FILE_SCALE),
])
def test_ebook_creation(title,author,file_scale,isbn,expected):
    if expected is None:
        ebook = DigitalBook(title,author,file_scale,isbn)
        assert ebook.get_title() == title
        assert ebook.get_author() == author
        assert ebook.get_isbn() == isbn
        assert ebook.get_file_scale() == file_scale
    else:
        with pytest.raises(LibraryError) as exc_info:
            DigitalBook(title,author,file_scale,isbn)
        assert exc_info.value.code == expected.value.code
















