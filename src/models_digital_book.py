from src.exceptions import LibraryErrors
from src.models_book import Book

# ------------------------------------ Digital Book ---------------------------------------------

class DigitalBook(Book):

    def __init__(self, title:str, author :str, file_scale:int, isbn="NA"):
        super().__init__(title, author, isbn)
        if not isinstance(file_scale, int) or file_scale < 0:
            raise LibraryErrors.INVALID_DIGITAL_BOOK_FILE_SCALE.value

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

