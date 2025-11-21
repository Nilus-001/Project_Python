import tkinter as tk
from tkinter import ttk
from src.file_manager import LibraryWithFile
from src.models_book import Book


class AppLibrary:
    def __init__(self,name:str):

        self.library = LibraryWithFile(name)

        self.library.import_data()

        self.window = tk.Tk()
        self.window.title("App.wav")
        self.window.geometry("700x500")



        self.create_widgets()
        self.update_to_app(self.library.list_of_books)

    def create_widgets(self):

        title = ttk.Label(self.window, text="My Library App", font=("Helvetica", 16))
        title.pack(side="top")

        input_frame = tk.Frame(self.window)
        # {

        inf_title = ttk.Label(input_frame, text="Gestion", font=("Helvetica", 14))
        inf_title.pack(fill="x",padx=100,pady=10)

        #-----------------------X------------

        inf_research_frame = ttk.Frame(input_frame)

        inf_label_research = ttk.Label(inf_research_frame, text="Research")
        inf_label_research.pack(side="left",padx=2)
        self.get_entry_research = tk.StringVar(value="")
        inf_entry_research = ttk.Entry(inf_research_frame, textvariable=self.get_entry_research)
        inf_entry_research.pack(side="left",padx=2)
        inf_button_research = ttk.Button(inf_research_frame, text="Search",command= self.search_button) # button a def
        inf_button_research.pack(side="left",padx=2)

        inf_research_frame.pack(padx=10,pady=10,fill="x")

        #------------------------X-----------


        inf_add_frame = ttk.Frame(input_frame)

        inf_label_add = ttk.Label(inf_add_frame, text="Add Book")
        inf_label_add.pack(fill="x",padx=100,pady=10)

        #------------------------X-----------

        inf_entry_add_title_frame = ttk.Frame(inf_add_frame)

        inf_entry_add_title_label = ttk.Label(inf_entry_add_title_frame, text="Title:")
        inf_entry_add_title_label.pack(side="left")
        self.get_entry_title = tk.StringVar(value="")
        self.inf_entry_add_title = ttk.Entry(inf_entry_add_title_frame, width=25 , textvariable=self.get_entry_title)
        self.inf_entry_add_title.pack(side="left",padx=14)

        inf_entry_add_title_frame.pack(padx=10,pady=10,fill="x")

        #------------------------X-----------

        #------------------------X-----------

        inf_entry_add_author_frame = ttk.Frame(inf_add_frame)

        inf_entry_add_author_label = ttk.Label(inf_entry_add_author_frame, text="Author:")
        inf_entry_add_author_label.pack(side="left")
        self.get_entry_author = tk.StringVar(value="")
        self.inf_entry_add_author = ttk.Entry(inf_entry_add_author_frame, width=25 , textvariable=self.get_entry_author)
        self.inf_entry_add_author.pack(side="left")

        inf_entry_add_author_frame.pack(padx=10,pady=10,fill="x")

        #------------------------X-----------

        #------------------------X-----------

        inf_entry_add_isbm_frame = ttk.Frame(inf_add_frame)

        inf_entry_add_isbm_label = ttk.Label(inf_entry_add_isbm_frame, text="ISBM:")
        inf_entry_add_isbm_label.pack(side="left")
        self.get_entry_isbm = tk.StringVar(value="")
        self.inf_entry_add_isbm = ttk.Entry(inf_entry_add_isbm_frame, width=25, textvariable=self.get_entry_isbm)
        self.inf_entry_add_isbm.pack(side="left",padx=10)

        inf_entry_add_isbm_frame.pack(padx=10,pady=10,fill="x")

        #------------------------X-----------

        #! E-BOOK a faire plus tard

        inf_button_add = ttk.Button(inf_add_frame, text="Add Book",command=self.add_book_button)
        inf_button_add.pack(fill="x",padx=85,pady=10,side="left")


        inf_add_frame.pack(padx=10,pady=10,fill="x")

        input_frame.pack(side="left",padx=10,pady=10,fill="x",)
        # }

        output_frame = tk.Frame(self.window)

        outf_title = ttk.Label(output_frame, text="Info", font=("Helvetica", 14))
        outf_title.pack(fill="x", padx=165)

        outf_text_frame = ttk.Frame(output_frame)

        self.outf_text_book = tk.Listbox(output_frame, height=18, width=60,font=("Consolas", 8))
        self.outf_text_book.pack(fill="x",padx=0,pady=10,side="left")

        outf_text_frame.pack(fill="x", padx=20, pady=10)





        output_frame.pack(side="left")


    def search_button(self):
        entry = self.get_entry_research.get()
        if "author:" in entry.lower():
            entry = entry.replace("author:","").strip()
            self.update_to_app(self.library.research_by_author(entry))
        elif "title:" in entry.lower():
            entry = entry.replace("title:","").strip()
            self.update_to_app(self.library.research_by_title(entry))
        else:
            self.update_to_app(self.library.research_by_title(entry))




    def add_book_button(self):

        self.library.add_book(Book(self.get_entry_title.get(), self.get_entry_author.get(), self.get_entry_isbm.get()))
        self.update_to_app(self.library.list_of_books)

        self.inf_entry_add_isbm.delete(0, tk.END)
        self.inf_entry_add_author.delete(0, tk.END)
        self.inf_entry_add_title.delete(0, tk.END)



    def update_to_app(self,list_books):
        self.outf_text_book.delete(0, tk.END)
        for book in list_books:

            self.outf_text_book.insert(tk.END, f"{book.get_title().ljust(18)} | {book.get_author().ljust(18)} | {book.get_isbn().ljust(18)}")


    def run(self):
        self.window.mainloop()



if __name__ == "__main__":
    app = AppLibrary("library")
    app.run()