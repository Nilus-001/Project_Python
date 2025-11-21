# ------------------------------------ Book ---------------------------------------------
import datetime
from enum import Enum

from src.exceptions import LibraryErrors

class Category(Enum):
    ROMAN = 'roman'
    SCIENCE_FICTION = 'science_fiction'
    FANTASY = 'fantasy'
    POLICIER = 'policier'
    THRILLER = 'thriller'
    HORREUR = 'horreur'
    BIOGRAPHIE = 'biographie'
    AUTOBIOGRAPHIE = 'autobiographie'
    HISTOIRE = 'histoire'
    PHILOSOPHIE = 'philosophie'
    DEVELOPPEMENT_PERSONNEL = 'developpement_personnel'
    ENTREPRENEURIAT = 'entrepreneuriat'
    SCIENCES = 'sciences'
    ART = 'art'
    POESIE = 'poesie'
    THEATRE = 'theatre'
    ESSAI = 'essai'
    CUISINE = 'cuisine'
    VOYAGE = 'voyage'
    JEUNESSE = 'jeunesse'


class Book:



    def __init__(self, title:str, author:str,category:Category, isbn="NA"):

        if not isinstance(title, str) or title.strip() == "":
            raise LibraryErrors.INVALID_BOOK_TITLE.value
        if not isinstance(author, str) or author.strip() == "":
            raise LibraryErrors.INVALID_BOOK_AUTHOR.value
        if not isinstance(isbn, str) or isbn.strip() == "" or len(isbn) != 13 and not isbn == "NA":
            raise LibraryErrors.INVALID_BOOK_ISBN.value


        self._title = title
        self._author = author

        self._isbn = isbn



        self.borrow_by = {}
        self.data_history = {}
        self.borrow_queue = [] #[0]-> premier // [-1] dernier
        self.comment_list = []
        self.note = {}
        self.category = category.value
        self.book_number = None

    def __str__(self)->str:
        return f'{self._title} by {self._author} with {self._isbn}'


    def get_data(self) -> dict:
        return {
            "title": self._title,
            "author": self._author,
            "isbn": self._isbn,
            "borrow_by":self.borrow_by,
            "data_history":self.data_history,
            "borrow_queue":self.borrow_queue,
            "comment_list":self.comment_list,
            "note":self.note,
            "category":self.category,
            "book_number":self.book_number,

        }


    def add_borrow_by(self,user):
        self.borrow_by[user.id] = f"{datetime.datetime.now()+datetime.timedelta(days=14)}"

        self.data_history[f"{datetime.datetime.now()}"]=f" borrowed by {(user.username,user.id)}"

    def add_borrow_queue(self,user):
        self.borrow_queue.append(user.id)

        self.data_history[f"{datetime.datetime.now()}"]= f" wanted by {(user.username,user.id)}"

    def return_to_library(self,by_user):
        self.borrow_by.pop(by_user.id)

        self.data_history[f"{datetime.datetime.now()}"]=f" returned by {(by_user.username, by_user.id)}"
        if len(self.borrow_queue) > 0:
            self.send_mail_to(self.borrow_queue[0])

    def send_mail_to(self,user_id):
        print(
            f"MESSAGE for {user_id}:\n"
            f"Your wanted book {self._title} is available now !"
        )

    def add_note(self,user,note:int):
        if note < 0 or note > 10:
            raise LibraryErrors.NOTE_FORMAT_ERROR.value
        self.note[f"{(user.username,user.id)}"] = note


    def add_comment(self,user,comment:str):
        comment_info = user.username,f"{datetime.datetime.now()}", comment
        self.comment_list.append(comment_info)


    def get_title(self):
        return self._title
    def get_author(self):
        return self._author
    def get_isbn(self):
        return self._isbn
