import tkinter as tk
from tkinter import ttk
from src.file_manager import LibraryWithFile
from src.models_book import Book


class AppLibrary:
    def __init__(self, name: str):
        self.library = LibraryWithFile(name)
        self.library.import_data()

        # Fenêtre principale
        self.window = tk.Tk()
        self.window.title("Pro Library App")
        self.window.geometry("1100x650")
        self.window.configure(bg="#1B1C20")

        # Styles
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Label style
        self.style.configure("TLabel", background="#1B1C20", foreground="#E0E0E0", font=("Helvetica", 12))
        # Button style
        self.style.configure("TButton",
                             background="#3AB0FF",
                             foreground="#FFFFFF",
                             font=("Helvetica", 11, "bold"),
                             padding=6)
        self.style.map("TButton",
                       background=[('active', '#2D9CDB')])
        # Entry style
        self.style.configure("TEntry", font=("Helvetica", 11), fieldbackground="#2A2C33", foreground="#E0E0E0")

        # Treeview style
        self.style.configure("Treeview",
                             background="#22252B",
                             foreground="#E0E0E0",
                             fieldbackground="#22252B",
                             rowheight=28,
                             font=("Helvetica", 11))
        self.style.configure("Treeview.Heading",
                             font=("Helvetica", 12, "bold"),
                             foreground="#3AB0FF",
                             background="#1F2125")

        # Scrollbar style
        self.style.configure("Vertical.TScrollbar",
                             troughcolor="#1B1C20",
                             background="#3AB0FF",
                             arrowcolor="#FFFFFF",
                             bordercolor="#1B1C20",
                             lightcolor="#3AB0FF",
                             darkcolor="#3AB0FF")

        self.style.configure("Custom.Treeview",
                             background="#242629",
                             foreground="#E0E0E0",
                             fieldbackground="#242629",
                             rowheight=23,
                             font=("Segoe UI", 11))

        # Headings
        self.style.configure("Custom.Treeview.Heading",
                             font=("Segoe UI", 12, "bold"),
                             foreground="#3AB0FF",
                             background="#1F2024",
                             relief="flat")

        # Scrollbar verticale
        self.style.configure("Custom.Vertical.TScrollbar",
                             gripcount=0,
                             background="#1E90FF",
                             troughcolor="#1B1C20",
                             bordercolor="#1B1C20",
                             arrowcolor="#E0E0E0",
                             lightcolor="#1E90FF",
                             darkcolor="#1E90FF")

        self.create_widgets()
        self.update_to_app(self.library.list_of_books)

    def create_widgets(self):
        # TITRE PRINCIPAL
        title = ttk.Label(self.window, text="📚 Library App", font=("Helvetica", 26, "bold"), foreground="#3AB0FF")
        title.pack(pady=15)

        main_frame = tk.Frame(self.window, bg="#1B1C20")
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # ---- Barre latérale gauche ----
        side_frame = tk.Frame(main_frame, bg="#1B1C20")
        side_frame.pack(side="left", fill="y", padx=(0, 20))

        # Recherche
        search_frame = tk.LabelFrame(side_frame, text="Search Book 🔍", bg="#1B1C20", fg="#3AB0FF",
                                     font=("Helvetica", 14, "bold"), labelanchor="n")
        search_frame.pack(fill="x", pady=(0, 20))

        self.get_entry_research = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.get_entry_research, width=28)
        search_entry.pack(pady=5, padx=10)
        search_button = ttk.Button(search_frame, text="Search", command=self.search_button)
        search_button.pack(pady=5, padx=10, fill="x")

        # Ajout livre
        add_frame = tk.LabelFrame(side_frame, text="Add New Book ➕", bg="#1B1C20", fg="#3AB0FF",
                                  font=("Helvetica", 14, "bold"), labelanchor="n")
        add_frame.pack(fill="x")

        self.get_entry_title = tk.StringVar()
        ttk.Label(add_frame, text="Title:", foreground="#E0E0E0").pack(anchor="w", pady=2, padx=10)
        self.inf_entry_add_title = ttk.Entry(add_frame, textvariable=self.get_entry_title, width=28)
        self.inf_entry_add_title.pack(pady=2, padx=10)

        self.get_entry_author = tk.StringVar()
        ttk.Label(add_frame, text="Author:", foreground="#E0E0E0").pack(anchor="w", pady=2, padx=10)
        self.inf_entry_add_author = ttk.Entry(add_frame, textvariable=self.get_entry_author, width=28)
        self.inf_entry_add_author.pack(pady=2, padx=10)

        self.get_entry_isbm = tk.StringVar()
        ttk.Label(add_frame, text="ISBN:", foreground="#E0E0E0").pack(anchor="w", pady=2, padx=10)
        self.inf_entry_add_isbm = ttk.Entry(add_frame, textvariable=self.get_entry_isbm, width=28)
        self.inf_entry_add_isbm.pack(pady=2, padx=10)

        add_button = ttk.Button(add_frame, text="Add Book", command=self.add_book_button)
        add_button.pack(pady=10, padx=10, fill="x")

        # ---- Zone principale droite ----
        right_frame = tk.Frame(main_frame, bg="#1B1C20")
        right_frame.pack(side="left", fill="both", expand=True)

        # Treeview
        # ttk.Label(right_frame, text="Library 📖", font=("Helvetica", 14, "bold"), foreground="#3AB0FF").pack(pady=(0, 10))

        self.tree = ttk.Treeview(right_frame, columns=("Title", "Author", "ISBN"), show='headings', height=16,style="Custom.Treeview")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Author", text="Author")
        self.tree.heading("ISBN", text="ISBN")
        self.tree.column("Title", width=350, anchor="center")
        self.tree.column("Author", width=250, anchor="center")
        self.tree.column("ISBN", width=180, anchor="center")

        # Scrollbar
        scrollbar = ttk.Scrollbar(right_frame, orient="vertical", command=self.tree.yview,style="Custom.Vertical.TScrollbar")
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right",fill="y",padx=(0,2))
        self.tree.pack(fill="x", expand=False)

        # Lignes alternées
        self.tree.tag_configure('evenrow', background="#22252B", foreground="#E0E0E0")
        self.tree.tag_configure('oddrow', background="#1F2125", foreground="#E0E0E0")


        # ---- Zone info du livre sélectionné ----
        self.info_frame = tk.LabelFrame(right_frame, text="Book Details", bg="#1F2125", fg="#3AB0FF",
                                        font=("Helvetica", 12, "bold"), labelanchor="n")
        self.info_frame.pack(fill="both", expand=True, pady=10)

        self.info_label = tk.Label(self.info_frame, text="Select a book to see details here.",
                                   bg="#1F2125", fg="#E0E0E0", font=("Helvetica", 12), justify="left", anchor="nw")
        self.info_label.pack(fill="both", expand=True, padx=10, pady=10)

        # Bind selection
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

    def on_tree_select(self, event):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0])['values']
            # if values[3] in values:
            #     self.info_label.config(text=f"E-Book\nTitle: {values[0]}\nAuthor: {values[1]}\nISBN: {values[2]}\nFileScale: {values[2]}")

            self.info_label.config(text=f"Book\nTitle: {values[0]}\nAuthor: {values[1]}\nISBN: {values[2]}")
        else:
            self.info_label.config(text="Select a book to see details here.")

    def search_button(self):
        entry = self.get_entry_research.get()
        if "author:" in entry.lower():
            entry = entry.replace("author:", "").strip()
            self.update_to_app(self.library.research_by_author(entry))
        elif "title:" in entry.lower():
            entry = entry.replace("title:", "").strip()
            self.update_to_app(self.library.research_by_title(entry))
        else:
            self.update_to_app(self.library.research_by_title(entry))

    def add_book_button(self):
        self.library.add_book(Book(
            self.get_entry_title.get(),
            self.get_entry_author.get(),
            self.get_entry_isbm.get()
        ))
        self.update_to_app(self.library.list_of_books)

        # Reset entries
        self.inf_entry_add_title.delete(0, tk.END)
        self.inf_entry_add_author.delete(0, tk.END)
        self.inf_entry_add_isbm.delete(0, tk.END)

    def update_to_app(self, list_books):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for idx, book in enumerate(list_books):
            tag = 'evenrow' if idx % 2 == 0 else 'oddrow'
            self.tree.insert('', 'end', values=(book.get_title(), book.get_author(), book.get_isbn()), tags=(tag,))

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = AppLibrary("library_data.json")
    app.run()
