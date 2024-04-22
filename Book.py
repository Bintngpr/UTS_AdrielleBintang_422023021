class Book:
    def __init__(self, title):
        self.title = title
        self.lender_name = ''
        self.lend_date = ''
        self.status = 'Available'

    def is_available(self):
        return self.status == 'Available'
