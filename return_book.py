class ReturnBooks:
    @staticmethod
    def return_book(books):
        books_id = int(input("Enter Book ID: ")) - 1
        if 0 <= books_id < len(books):
            book = books[books_id]
            if book.status == 'Available':
                print("This book is already available in the library.")
            else:
                book.lender_name = ''
                book.lend_date = ''
                book.status = 'Available'
                print("Book returned successfully!")
        else:
            print("Invalid Book ID!")
