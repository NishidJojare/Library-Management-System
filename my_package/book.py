class Books:
    def __init__(self):
        self.books = {
            1001: "C++ programming",
            1002: "PHP programming",
            1003: "Python programming",
            1004: "Java programming",
            1005: "C programming"
        }
        
    def issue_book(self):
        book_id = int(input("Enter the Book Id to Issue :"))
        if book_id in self.books.keys():
            print(f"Book issued\nBook details : Name-{self.books[book_id]}, Id-{book_id}")
        else:
            print("Book is not available...")
            
    def return_book(self):
        book_id = int(input("Enter the Book Id to Submit :"))
        if book_id in self.books.keys():
            print(f"Book submitted\nBook details : Name-{self.books[book_id]}, Id-{book_id}")
        else:
            print("Book was not issued...")
            
