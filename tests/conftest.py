import pytest

from src.file_manager import LibraryWithFile
from src.models_library import Library
from src.models_book import Book
from src.models_digital_book import DigitalBook



@pytest.fixture
def simple_library():
     """Fixture for a simple library."""
     return Library("lib Test")

@pytest.fixture
def simple_library_with_file():
     """Fixture for a simple library."""
     return LibraryWithFile("lib File Test")

@pytest.fixture
def simple_book():
     """Fixture for a simple book 'Python'."""
     return Book("Python", "A. Dev", "0000000000001")

@pytest.fixture
def simple_ebook():
     """Fixture for a simple e-book 'Python'."""
     return DigitalBook("Python e-book", "A. Dev", file_scale=10)


@pytest.fixture
def empty_library():
     """Fixture for an empty library."""
     return Library("")

@pytest.fixture
def empty_book():
     """Fixture for an empty book."""
     return Book("", "", "")

@pytest.fixture
def empty_ebook():
     """Fixture for an empty e-book."""
     return DigitalBook("", "", 0)












