'''
Python Project

Write a program for implementing student library management system where students can borrow books from the list of book. Create a separate library and student class. You are free to choose methods and attributes of your choice to implement this functionality.


make student account for library 
book shelve (show list of books)

create library class,
       student class, & 
       books class

'''



from my_package.book import Books
from my_package.library import Library
from my_package.student import Student 


def book_shelve():
    books = {
        1001: "C++ programming",
        1002: "PHP programming",
        1003: "Python programming",
        1004: "Java programming",
        1005: "C programming"
    }
    
    for bookid,bookname in books.items():
        print(f"Book Id :{bookid} | Book Name : {bookname}")
        


def menus():
    print(f'''
    Choose menu :
    1. Create Student Account
    2. Remove Student Account
    3. Create Library Account
    4. Remove Library Account
    5. Show all available books in library
    6. Issue Book
    7. Submit Book
    8. Exit
          
    ''')
    
while True:    
    try:
        menus()
        print()
        menu=int(input("Enter menu option : "))
        if menu==1:
            print()
            std=Student(1002,"Nishid",'BCA 2nd yr')
            print(str(std))
        elif menu==2:
            std=Student(1002,"Nishid",'BCA 2nd yr')
            std.remove_student(1002)
            
        elif menu==3:
            lib=Library('L001','no')
            print(lib.create_library_account())
            
        elif menu==4:
            lib=Library('L001','no')
            print(lib.remove_library_account('L001'))
            
        elif menu==5:
            # b=Books()
            book_shelve()
            
        elif menu==6:
            b=Books()
            book_shelve()
            print()
            b.issue_book()
            
        elif menu==7:
            b=Books()
            b.return_book()
        else:
            print("Program ending...")
            break
    except Exception:
        print("Something went wrong...program ending...")

