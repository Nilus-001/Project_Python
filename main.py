from time import sleep

from src.file_manager import LibraryWithFile
from src.gui import AppLibrary
from src.models_book import Book, Category
from src.models_user import User, Subscription

# app = AppLibrary("library")
# app.run()

lib = LibraryWithFile("library")
client = User("nils", "123",subscription=Subscription.BASIC)
client2 = User("Come", "985",subscription=Subscription.PREMIUM)
b1 = Book("test","moi",Category.ROMAN,"0000000000005")
b2 = Book("test n2","encore moi",Category.SCIENCES,"0000000000008")
b3 = Book("test n3","encore moi",Category.FANTASY,"0000000700008")
b4 = Book("test n4","encore moi",Category.ART,"0045000700008")


lib.add_user(client)
lib.add_user(client2)
lib.add_book(b1)
lib.add_book(b2)

client.borrow_book(b1)
sleep(0.5)
client.borrow_book(b2)
sleep(0.5)
client2.borrow_book(b1)
sleep(0.5)
client.return_book(b1,10,"tres bon livre")
sleep(0.5)
client2.borrow_book(b1)
sleep(0.5)
client2.borrow_book(b2)
sleep(0.5)
client2.borrow_book(b3)
sleep(0.5)
client2.borrow_book(b4)

# lib.check_date()

lib.export_data()


print(lib.list_of_books[0])
print(lib.list_of_users)
# lib.export_csv("export")


# client.connect("localhost",12345)

# lib.export_data()






















# lib = Library("zzzz")
# print(lib.name)
# lib.add_book(b1)
# lib.add_book(b2)
# lib.add_book(b3)
# lib.add_book(b4)
# lib.add_book(b5)
# lib.remove_book_by_isbn("9780261102217")
#
# # lib.remove_book_by_isbn("9780261102217")
#
# # lib = LibraryWithFile("Library")
#
#
#
#
# try :
#
#     print(b5.get_data())
#     # lib.import_data()
#     # print(lib.get_data())
#     print(lib.get_list_of_books())
#     # lib.export_csv("books_export.csv")
#
#     print(lib.research_by_author("j."))
#     print(lib.research_by_title("a"))
#





#
#
#
# except LibraryError as e:
#     print(f"Library Error [{e.code}]: {e}")