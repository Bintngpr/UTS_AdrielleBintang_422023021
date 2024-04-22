from Library import Library
from load_books import LoadBooks
from display_books import DisplayBooks
from issue_books import IssueBooks
from add_books import AddBooks
from return_book import ReturnBooks
from authenticator import Authenticator

authenticator = Authenticator()

authenticator.add_user("422023021", "422023021")
authenticator.add_user("422023001", "422023001")

username = input("Masukkan username: ")
password = input("Masukkan password: ")

if authenticator.login(username, password):
    print("\n***Login berhasil!***")
else:
    print("\n***Login gagal! Username atau password salah.***")
    

if __name__ == "__main__":
    try:
        my_library = Library("Python's")
        my_library.books = LoadBooks.load_books("list_of_books.txt")
        press_key_list = {"D": "Display Books", "I": "Issue Books", "A": "Add Books", "R": "Return Books", "Q": "Quit"}

        key_press = False
        while not (key_press == "q"):
            print(f"\n----------Welcome To {my_library.library_name}'s Library Management System---------\n")
            for key, value in press_key_list.items():
                print("Press", key, "To", value)
            key_press = input("Press Key: ").lower()
            if key_press == "i":
                print("\nCurrent Selection: ISSUE BOOK\n")
                IssueBooks.issue_book(my_library.books)

            elif key_press == "a":
                print("\nCurrent Selection: ADD BOOK\n")
                AddBooks.add_book(my_library.books)

            elif key_press == "d":
                print("\nCurrent Selection: DISPLAY BOOKS\n")
                DisplayBooks.display_books(my_library.books)

            elif key_press == "r":
                print("\nCurrent Selection: RETURN BOOK\n")
                ReturnBooks.return_book(my_library.books)

            elif key_press == "q":
                break

            else:
                continue
            
    except Exception as e:
        print("Something went wrong. Please check!")
