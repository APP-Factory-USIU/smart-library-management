"""
This file will handle;
    1. All classes and inherences
    2. The library functionality.
    3. For instant mentods you need use self because it exposes the attributes.
    4. __init__ : It makes the attribute avalilabe to the objects.
"""
"""
Further improvements:
1. Add a book count that is deducted once a book has been borrowed.
2. Add a json file for storing book properties.
3. Prompt the user to add the quantity of books.
4. Check wheather book is available in the shelf first.
5. The user searches for the book using the title.
6. The ISBN is important to the  librarian.
Note: Books with the same title and writen by the same author have a similar ISBN.


"""


class Book:
    #class book captures the books metadata
    def __init__(self, title, author, book_id ): # further improvements one can add category
        self.title = title
        self.author = author
        self.book_id = book_id
        self.available = True
        self.count = 0
        
        #display books
    def __str__(self):
        return f"{self.title} by {self.author}, {self.book_id}"# further development add an if statement to check the book status
    
class Users:
    # Captures users/memebers information
    def __init__ (self, name, email, user_ID):
        self.name = name
        self.email = email
        self.user_ID = user_ID
    
    def display_users(self):
        header = f"|{'Name':<10}|{'Email':<30}|{'ID':<7}|"
        print(header)
        table = f"|{self.name:<10}|{self.email:<30}|{self.user_ID:<7}|"
        print(table)
        
class Library_system(Book, Users):
    def __init__(self):
        #super().__init__(self, available)
        self.Books = []
        self.User = []
        self.Borrowed_books = []
        self.book_count = 0
        
    def add_book(self, books):
        self.Books.append(books)
        print(f"Book '{books}' added.")    
       
    def add_users(self, users):
        self.User.append(users)
        print(f"'{users}' has been added")
        
    
    def borrow(self, book_choice):
        if book_choice in self.Borrowed_books:
            return f"'{book_choice}'is not available"           
        else:
            for i in self.Books:               
                if book_choice ==  i:
                    self.Books.remove(book_choice)
                    self.Borrowed_books.append(book_choice)
                    return f"You have borrowed '{book_choice}'"      
            return(f"{book_choice} not in the library")
                
                
    def return_book(self, book_choice):
        if book_choice in self.Borrowed_books:
            self.Borrowed_books.remove(book_choice)
            self.Books.append(book_choice)
        
            
            
            
               
        
            
        
            
            
        
        
    #     '''
    #     book (book_id)-> Availabily
    #     user (id) -> is the user registered
    #     book = (i-> book_id  if i == not  available) none)
    #     status = "available" if available == True else "borrow"
    #     '''
        
            
    
       
    
    
    
    
    
    
    
        
    