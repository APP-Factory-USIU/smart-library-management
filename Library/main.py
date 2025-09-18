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
library.add_book("Confess")
print(library.Books)
library.borrow("alice in wonderland")
print(library.Borrowed_books)
print(library.Books) 

print("Returning Books.")
library.return_book("alice in wonderland")
if not library.Borrowed_books:
    print("No borrowed Books available.")
else:
    print("Borrowed Books: ")
    print(library.Borrowed_books)

print("\nBooks available in the Library.")
for index, books in enumerate(library.Books, 1):
    print(f"\t{index}. {books}") 