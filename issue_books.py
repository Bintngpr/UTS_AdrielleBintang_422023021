import datetime

class IssueBooks:
    @staticmethod
    def issue_book(books):
        books_id = int(input("Enter Book ID: ")) - 1
        if 0 <= books_id < len(books):
            book = books[books_id]
            if not book.is_available():
                print(f"This book is already issued to {book.lender_name} on {book.lend_date}")
            else:
                your_name = input("Enter Your Name: ")
                book.lender_name = your_name
                book.lend_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                book.status = 'Already Issued'
                print("Book Issued Successfully!")
        else:
            print("Invalid Book ID!")
