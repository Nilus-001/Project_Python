import pytest
from models import Library ,Book, DigitalBook


@pytest.fixture
def empty_library():
     """Fixture for an empty library."""
     return Library("lib Test")

@pytest.fixture
def simple_book():
     """Fixture for a simple book 'Python'."""
     return Book("Python", "A. Dev", "0000000000001")

@pytest.fixture
def simple_ebook():
     """Fixture for a simple e-book 'Python'."""
     return DigitalBook("Python e-book", "A. Dev", file_scale=10)












