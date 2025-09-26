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
import json

filename1 = 'book_database.json'


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
        
        
class Book_Database:
    def __init__(self, content):
        self.content = content
        
    def fetch_content(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        return data
        
    def add_content(self, filename):
        with open(filename, 'a') as file_obj:
            # content = filename[0]
            data = json.dump(file_obj)
        return data 
               
        
class Library_system(Book, Users, Book_Database):
       
    def add_book(self, book_title, book_author, copies):
        data = self.fetch_content(filename1)
        
        try:
            with open(filename1, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
            
        # specific_key = data['available_books']
        content = {"title": book_title, "author": book_author, "copies": copies}
        data['available_books'].append(content)
        
        with open(filename1, 'w') as file:
            json.dump(data, file, indent=4)
        
        
        print(f"Book '{book_title}' added.") 
        
    def update_books(self, book_title, copies):
        data = self.fetch_content(filename1)
        
        for index in range(len(data["available_books"])):
            if book_title in data['available_books'][index]['title']:
                print("Book Found")
                count = data['available_books'][index]
                current_count = data['available_books'][index]['copies']
                count.update({
                    "copies": current_count + copies
                })
                print(data['available_books'][index]['copies'])
                
            with open(filename1, 'w') as file:
                json.dump(data, file, indent=4)
        
        return f"'{book_title}' has been updated."
        
           
    def add_users(self, users):
        self.User.append(users)
        print(f"'{users}' has been added")
        
        
    def show_available_books(self):
        data = self.fetch_content(filename1)
        print('\n')
        
        test = []
        
        content = data["available_books"]
        for i in range(len(content)):
            info = content[i]["title"]
            test.append(info)
            # print(f"{i + 1}. {info}")
        return test
        
        
    def show_borrowed_books(self):
        data = self.fetch_content(filename1)
        print('\n')
        
        test = []
        
        content = data["borrowed_books"]
        for i in range(len(content)):
            info = content[i]["title"]
            test.append(info)
            # print(f"{i + 1}. {info}")
        return test        
    
                
    def borrow(self, book_choice):
        data = self.fetch_content(filename1)
        borrow_content = data['borrowed_books']
        available_content = data['available_books']
        
        if book_choice in self.show_borrowed_books():
            return f"'{book_choice}' is not available"           
        else:
            for index in range(len(available_content)):
                # i = available_content[index]
                if book_choice == available_content[index]["title"]:
                    i = available_content[index]
                    print(i)
                    available_content.remove(i)
                    
                    # Add content to borrowed books
                    borrow_content.append(i)
                    
                    # Updated the JSON File
                    with open(filename1, 'w') as file:
                        json.dump(data, file, indent=4)
                        
                    return f"You have borrowed '{book_choice}'"      
            return(f"{book_choice} not in the library")    
    
       
    def return_book(self, book_choice):
        data = self.fetch_content(filename1)
        borrow_content = data['borrowed_books']
        available_content = data['available_books']
        
        # if book_choice in self.show_borrowed_books():
        for index in range(len(borrow_content)):
            if book_choice == borrow_content[index]['title']:
                i = borrow_content[index]
                
                borrow_content.remove(i)
                
                available_content.append(i)
                
                with open(filename1, 'w') as f:
                    json.dump(data, f, indent=4)
                
                return f"You have returned '{book_choice}'"
        
            
        
            
            
        
        
    #     '''
    #     book (book_id)-> Availabily
    #     user (id) -> is the user registered
    #     book = (i-> book_id  if i == not  available) none)
    #     status = "available" if available == True else "borrow"
    #     '''
        
            
    