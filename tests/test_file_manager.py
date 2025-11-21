import json

import pytest
from src.exceptions import LibraryError,LibraryErrors
from src.file_manager import LibraryWithFile
from tests.conftest import simple_book


# ------------------------------------ File management test TEST ---------------------------------------------


@pytest.mark.parametrize("name,expected", [
    ("TestLib", None),
    ("Test.Lib", None),
    ("Test/Lib", LibraryErrors.INVALID_LIBRARY_NAME),
])

def test_creation_library_with_file(name, expected):
    if expected is None:
        lib = LibraryWithFile(name)
        assert lib.name == name
        assert lib._filepath == f"./data/{name.lower().replace(' ', '_')}.json"
    else:
        with pytest.raises(LibraryError) as exc_info:
            LibraryWithFile(name)

        assert exc_info.value.code == expected.value.code



def test_export_data(simple_library_with_file, simple_book):
    lib = LibraryWithFile("test_export_data")
    lib.add_book(simple_book)

    lib.export_data()
    with open(f"./data/{"test_export_data"}.json") as file:
        data = file.read()
        assert '"title": "Python"' in data
        assert '"author": "A. Dev"' in data
        assert '"isbn": "0000000000001"' in data


def test_get_data_file_not_found(simple_book):
    lib = LibraryWithFile("test_data_file_n0t_f0und")
    book = simple_book
    lib.add_book(book)

    data = {"books": [book.get_data()]}
    with open(f"./data/{"test_data_file_not_found"}.json", 'w') as file:
        json.dump(data, file, indent=4)
    file.close()

    with pytest.raises(LibraryError) as exc_info:
        lib.get_data()

    assert exc_info.value.code == LibraryErrors.FILE_NOT_FOUND.value.code

def test_get_syntax_error(simple_book):
    lib = LibraryWithFile("test_syntax_error")
    book = simple_book
    lib.add_book(book)

    data = {"books": [book.get_data()]}
    with open(f"./data/{"test_syntax_error"}.json", 'w') as file:
        json.dump(data, file, indent=4)
    file.close()

    try:
        lib.get_data()
    except LibraryError as exc_info:
        assert exc_info.code != LibraryErrors.JSON_DECODE_ERROR.value.code

def test_get_data(simple_book):
    lib = LibraryWithFile("test_get_data")
    book = simple_book
    lib.add_book(book)

    data = {"books": [book.get_data()]}
    with open(f"./data/{"test_get_data"}.json", 'w') as file:
        json.dump(data, file, indent=4)
    file.close()


    data = lib.get_data()


    assert "books" in data
    assert data["books"][0]["title"] == "Python"
    assert data["books"][0]["author"] == "A. Dev"
    assert data["books"][0]["isbn"] == "0000000000001"


def test_import_data(simple_book):

    book = simple_book
    data = {"books": [book.get_data()]}
    with open(f"./data/{"test_import_data"}.json", 'w') as file:
        json.dump(data, file, indent=4)
    file.close()

    lib = LibraryWithFile("test_import_data")
    lib.import_data()

    books = lib.list_of_books
    assert len(books) == 1
    assert books[0]._title == "Python"
    assert books[0]._author == "A. Dev"
    assert books[0]._isbn == "0000000000001"

def test_export_csv(simple_library_with_file, simple_book):
    lib = LibraryWithFile("test_export_csv")
    lib.add_book(simple_book)
    lib.export_data()


    lib.export_csv("test_export_csv")

    with open("docs/test_export_csv", 'r') as file:
        content = file.read()
        assert "title,author,isbn" in content
        assert "Python,A. Dev,0000000000001" in content