import datetime
import json
import socket
import threading
from enum import Enum
from xmlrpc.client import DateTime

from src.exceptions import LibraryErrors
from src.models_book import Book


class Subscription(Enum):

    BASIC = 'basic'
    BASIC_NB_BORROW = 1

    PREMIUM = 'premium'
    PREMIUM_NB_BORROW = 3

    VIP = 'vip'
    VIP_NB_BORROW = 10


class User:


    def __init__(self,username:str,mdp:str,admin=False ,subscription =Subscription.BASIC):
        self.username = username
        self._mdp = hash(mdp)

        self.id = id(self)

        self._admin = admin
        self.subscription = subscription

        self.book_borrow = {}
        self.data_history = {}
        self.month_max_borrow_achieve = False
        self.month_max_borrow_reset = None
        self.wanted = []
        self.debt = 0

    def get_data(self):
        return{
            'id':self.id,
            'username': self.username,
            'mdp': self._mdp,
            'admin': self._admin,
            'subscription': self.subscription.value,
            'book_borrow': self.book_borrow,
            'data_history': self.data_history,
            'month_max_borrow_achieve': self.month_max_borrow_achieve,
            'month_max_borrow_reset': self.month_max_borrow_reset,
            'wanted': self.wanted,
            'debt':self.debt
        }


    def borrow_book(self,book:Book):
        if book.get_isbn() in self.wanted :
            self.wanted.remove(book.get_isbn())

        nb_borrow = 0
        if self.subscription.value == Subscription.BASIC.value:
            nb_borrow = Subscription.BASIC_NB_BORROW.value
        elif self.subscription.value == Subscription.PREMIUM.value:
            nb_borrow = Subscription.PREMIUM_NB_BORROW.value
        elif self.subscription.value == Subscription.VIP.value:
            nb_borrow = Subscription.VIP_NB_BORROW.value
        else:
            raise LibraryErrors.SUBSCRIPTION_ERROR.value

        if nb_borrow > len(self.book_borrow) :
            if len(book.borrow_by) == 0 : # (a changer pour le muliti-exemplaires)
                self.add_book_to_borrow(book)
                return True
            self.add_book_to_wanted(book)
            return None
        print("You can't do that : buy a better subscription to do that")
        return False


    def return_book(self,book:Book,note=None,comment=None): # ajout commentaire et note apres
        if book.get_isbn() in self.book_borrow:

            self.book_borrow.pop(book.get_isbn())
            book.return_to_library(self)
            if note is not None:
                book.add_note(self,note)
            if comment is not None:
                book.add_comment(self,comment)


            return True
        raise LibraryErrors.BOOK_NOT_FOUND.value



    def add_book_to_borrow(self,book:Book):
        self.book_borrow[book.get_isbn()]=f"{datetime.datetime.now()+datetime.timedelta(days=14)}"
        book.add_borrow_by(self)

        self.data_history[f"{datetime.datetime.now()}"]=f"{(book.get_title(),book.get_author(),book.get_isbn())} was borrowed"



    def add_book_to_wanted(self,book:Book):
        self.wanted.append(book.get_isbn())
        book.add_borrow_queue(self)

        self.data_history[f"{datetime.datetime.now()}"]=f"{(book.get_title(), book.get_author(), book.get_isbn())} was put in wanted list"






class UserBasic(User):
    def __init__(self,username:str,mdp:str):
        pass

class UserPremium(User):
    def __init__(self,username:str,mdp:str):
        pass

class UserVIP(User):
    def __init__(self,username:str,mdp:str):
        pass

class Admin(User):
    def __init__(self,username:str,mdp:str):
        pass



