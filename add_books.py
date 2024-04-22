from Book import Book

class AddBooks:
    @staticmethod
    def add_book(books):
        new_book_title = input("Enter Book Title: ")
        if new_book_title == "":
            print("Book title cannot be empty!")
            return
        elif len(new_book_title) > 20:
            print("Books title length is too long! Title length limit is 20 characters.")
            return
        books.append(Book(new_book_title))
        with open("list_of_books.txt", "a") as file:
            file.write(new_book_title + "\n")
        print(f"The book '{new_book_title}' has been added successfully!")
