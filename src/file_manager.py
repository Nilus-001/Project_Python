import csv
import json

from src.exceptions import LibraryError
from src.models import Library, DigitalBook, Book


class LibraryWithFile(Library):

    def __init__(self, name: str):
        super().__init__(name)
        self._filepath = f"./data/{self.name.lower().replace(' ', '_')}.json"


    def export_data(self):
        """Exports the library's book data to a JSON file."""
        data = {"books":[book.get_data() for book in self.get_list_of_books()]}
        with open(self._filepath, 'w') as file:
            json.dump(data, file, indent=4)


    def get_data(self)->dict:
        """Retrieves the library's book data from a JSON file."""
        try:
            with open(self._filepath, 'r') as file:
                  return json.load(file)

        except FileNotFoundError:
            raise LibraryError("File not found. Or invalid format.",4040)

        except json.decoder.JSONDecodeError:
            raise LibraryError("Invalid syntaxe in JSON file",4050)

        except PermissionError:
            raise LibraryError("Permission denied",4100)





    def import_data(self):
        """Imports book data from a JSON file into the library."""
        data = self.get_data()
        for book_data in data['books']:
            if 'file_scale' in book_data:
                book = DigitalBook(
                    title=book_data['title'],
                    author=book_data['author'],
                    file_scale=book_data['file_scale'],
                    isbn=book_data['isbn']
                )
            else:
                book = Book(
                    title=book_data['title'],
                    author=book_data['author'],
                    isbn=book_data['isbn']
                )
            self.add_book(book)


    def export_csv(self, csv_filepath: str):
        """Exports the library's book data to a CSV file."""

        csv_filepath = f"./docs/{csv_filepath}"
        with open(csv_filepath, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["title", "author", "isbn", "file_scale"])

            writer.writeheader()
            writer.writerows(self.get_data()["books"])