import csv
import json

from src.exceptions import LibraryError, LibraryErrors
from src.models_book import Book
from src.models_digital_book import DigitalBook
from src.models_library import Library
from src.models_user import User


class LibraryWithFile(Library):

    def __init__(self, name: str):
        super().__init__(name)
        self._filepath = f"./data/{self.name.lower().replace(' ', '_')}.json"


    def export_data(self):
        """Exports the library's book data to a JSON file."""
        data = {
            "books":[book.get_data() for book in self.list_of_books],
            "users":[user.get_data() for user in self.list_of_users]
        }
        with open(self._filepath, 'w') as file:
            json.dump(data, file, indent=4)



    def get_data(self)->dict:
        """Retrieves the library's book data from a JSON file."""
        try:
            with open(self._filepath, 'r') as file:
                  return json.load(file)

        except FileNotFoundError:
            raise LibraryErrors.FILE_NOT_FOUND.value

        except json.decoder.JSONDecodeError:
            raise LibraryErrors.JSON_DECODE_ERROR.value

        except PermissionError:
            raise LibraryErrors.PERMISSION_DENIED.value


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
            book.borrow_by=book_data['borrow_by']
            book.data_history=book_data['data_history']
            book.borrow_queue=book_data['borrow_queue']
            book.comment_list=book_data['comment_list']
            book.note=book_data['note']
            book.category=book_data['category']
            book.book_number=book_data['book_number']
            self.add_book(book)

        for user_data in data['users']:
            user = User(
                username=user_data['username'],
                mdp=user_data['mdp'],
                admin=user_data['admin'],
            )
            user.subscription=user_data['subscription'],
            user.book_borrow=user_data['book_borrow'],
            user.data_history=user_data['data_history'],
            user.mouth_max_borrow_achieve=user_data['month_max_borrow_achieve'],
            user.mouth_max_borrow_reset = user_data['month_max_borrow_reset'],
            user.wanted=user_data['wanted']
            user.id=user_data['id']
            user.debt=user_data['debt']

            self.add_user(user)


    def export_csv(self, csv_filepath: str):
        """Exports the library's book data to a CSV file."""
        if not isinstance(csv_filepath, str) or csv_filepath.strip() == "" or any(c in csv_filepath for c in ['<', '>', ':', '"', '/', '\\', '|', '?', '*']):
            raise LibraryErrors.INVALID_FILE_PATH.value

        new_csv_filepath = f"./docs/{csv_filepath}books.csv"
        with open(new_csv_filepath, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["title", "author", "isbn", "file_scale","borrow_by","data_history","borrow_queue","comment_list","note","category","book_number"])

            writer.writeheader()
            writer.writerows(self.get_data()["books"])
            file.close()

        new_csv_filepath = f"./docs/{csv_filepath}users.csv"
        with open(new_csv_filepath, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["id","username", "mdp", "admin", "subscription","book_borrow","data_history","month_max_borrow_achieve","month_max_borrow_reset","wanted","debt"])

            writer.writeheader()
            writer.writerows(self.get_data()["users"])
            file.close()
