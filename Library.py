from load_books import LoadBooks
from display_books import DisplayBooks
from issue_books import IssueBooks
from add_books import AddBooks
from return_book import ReturnBooks

class Library:
    def __init__(self, library_name):
        self.library_name = 'UKRIDA'
        self.books = []
        self.load_books("list_of_books.txt")
        id = 101

    def load_books(self, file_path):
        self.books = LoadBooks.load_books(file_path)

    def display_books(self):
        DisplayBooks.display_books(self.books)

    def issue_book(self):
        IssueBooks.issue_book(self.books)

    def add_book(self):
        AddBooks.add_book(self.books)

    def return_book(self):
        ReturnBooks.return_book(self.books)
