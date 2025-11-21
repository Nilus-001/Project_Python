from enum import Enum


class LibraryError(Exception):
    """Custom exception class for library-related errors."""

    def __init__(self, message: str, code_error: int = 0):
        super().__init__(message)
        self.code = code_error


class LibraryErrors(Enum):
    ISBN_ALREADY_EXISTS = LibraryError("Book with this ISBN already exists in the library.", 4089)
    BOOK_NOT_FOUND = LibraryError("Book not found in the library.", 4090)
    INVALID_BOOK_TITLE = LibraryError("The book title provided is invalid.", 4091)
    INVALID_BOOK_AUTHOR = LibraryError("The book author provided is invalid.", 4092)
    INVALID_BOOK_ISBN = LibraryError("The book ISBN provided is invalid.", 4093)
    INVALID_LIBRARY_NAME = LibraryError("The library name provided is invalid.", 4094)
    INVALID_BOOK_TYPE = LibraryError("The provided book is not of type Book.", 4095)
    INVALID_DIGITAL_BOOK_FILE_SCALE = LibraryError("The digital book file scale provided is invalid.", 4098)
    FILE_NOT_FOUND = LibraryError("File not found. Or invalid format.", 4040)
    JSON_DECODE_ERROR = LibraryError("Invalid syntax in JSON file", 4050)
    PERMISSION_DENIED = LibraryError("Permission denied", 4100)
    INVALID_FILE_PATH = LibraryError("The provided file path provided is invalid.", 4101)
    INVALID_USER_TYPE = LibraryError("The provided user is not of type User.", 4095)
    USER_ALREADY_EXISTS = LibraryError("User with this username already exists in the library.", 4089)
    SUBSCRIPTION_ERROR = LibraryError("Subscription error : Unknow subscription", 4098)
    NOTE_FORMAT_ERROR = LibraryError("Note is not between 0 and 10 or not int format",4099)




