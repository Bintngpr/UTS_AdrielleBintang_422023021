class DisplayBooks:
    @staticmethod
    def display_books(books):
        print("------------------------List of Books---------------------")
        print("Books ID", "\t", "Title")
        print("----------------------------------------------------------")
        for i, book in enumerate(books, start=1):
            print(i, "\t\t", book.title, "- [", book.status, "]")
