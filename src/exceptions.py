class LibraryError(Exception):
    """Custom exception class for library-related errors."""

    def __init__(self, message:str,code_error:int = 0):
        super().__init__(message)
        self.code = code_error
