"""
This main.py handles;
    - Creation of objects & instanciating classes
    - AoB
"""
from Library_system import Users , Book , Library_system

# user1 = Users("Alice", "alice.ac.ke", "2")
# print(user1)
library = Library_system ()
library.add_book("alice in wonderland")
#library.add_book("Confess")
print(library.Books)
library.borrow("alice in wonderland")
print(library.Borrowed_books)
print(library.Books)

    
