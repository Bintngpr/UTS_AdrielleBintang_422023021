from Book import Book

class LoadBooks:
    @staticmethod
    def load_books(file_path):
        books = []
        with open(file_path) as file:
            for line in file:
                title = line.strip()
                books.append(Book(title))
        return books
