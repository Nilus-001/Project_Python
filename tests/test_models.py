from src.models import Library, Book, DigitalBook


def test_with_fixtures(empty_library, simple_book, simple_ebook):
    lib = empty_library
    assert lib.name == "lib Test"
    assert len(lib.get_list_of_books()) == 0

    book = simple_book
    assert book.get_title() == "Python"
    assert book.get_author() == "A. Dev"
    assert book.get_isbn() == "0000000000001"

    ebook = simple_ebook
    assert ebook.get_title() == "Python e-book"
    assert ebook.get_author() == "A. Dev"
    assert ebook.get_isbn() == "NA"
    assert ebook.get_file_scale() == 10

    result = lib.add_book(book)
    assert result is True
    assert len(lib.list_of_books) == 1
    assert book in lib.list_of_books





