"""
This main.py handles;
    - Creation of objects & instanciating classes
    - AoB
"""
from Library_system import Users , Book , Library_system

# user1 = Users("Alice", "alice.ac.ke", "2")
# print(user1)
library = Library_system ()
# library.add_book("alice in wonderland")
# #library.add_book("Confess")
# print(library.Books)
# library.borrow("alice in wonderland")
# print(library.Borrowed_books)
# print(library.Books)
while True:
    choice = input("Enter \n1. to add book\n2. to add user, \n3 to borrow book,\n4 to return book:\n5. to exit\n")
    if choice == '1':
        book_name = input("Enter book name: ")
        library.add_book(book_name)
    elif choice == '2':
        user_name = input("Enter user name: ")
        user_email = input("Enter user email: ")
        user_id = input("Enter user ID: ")
        user1 = Users(user_name, user_email, user_id)
        library.add_users(user1)
        print(library.User[0].name)
    elif choice == '3':
        book_name = input("Enter book name to borrow: ")
        print(library.borrow(book_name))
      
    elif choice == '4':
        pass
    elif choice == '5':
        exit()
    else:
        print("Invalid choice")


    
