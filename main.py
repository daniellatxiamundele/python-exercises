#class Book:
    # Constructor
    #def __init__(self, title, author, genre):
        #self.title = title
        #self.author = author
        #self.genre = genre

    # Method
    #def printBookDetails(self):  # Adjusted indentation here
        #print(f"{self.title} by {self.author}, genre: {self.genre}")
        
# Usage of the class
#book1 = Book("It Ends With Us", "Colleen Hoover", "Romance Fiction")
#book1.printBookDetails()


from turtle import title


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # below is not in the brackets as it is not a function call, it is and instance attribute assignment
        self.is_available = True
        
    def borrow(self):
        if self.is_available:
            self.is_avaliable = False
            print(f"great! {self.title} has been borrowed")
        else:
            print(f"{self.title} is already borrowed")
    
    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"You have returned {self.title}")   
        else:
            print(f"{title} was not borrowed")      

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        
    def list_book(self):
        if not self.books:
            print(f"no books available")
        else:
            for book in self.books:
                availabilty = "yes" if book.is_available else "no"
            print(f"Title: {Book.title}, author: {Book.author}, Avaliable: {availabilty}")
    
    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(book)
        print (None)
        
    def borrow_book(self,title):
        book = self.find_book(title)
        if book:
                Book.borrow()
        else:
                print("f {title} is not avaliable to borrow")
                
    def return_book(self,title):
        book = self.find_book(title)
        if book:
            book.return_book()
        else:
            print("f {title} is not avalilable to return" )        
            
def main():
    library = library()
    
    library.add_book(Book("The fault in our stars, John green"))
    library.add_book(Book("The hunger games, Suzanne Collins"))
    library.add_book(Book("To Kill a Mockingbird, Harper Lee"))
    library.add_book(Book("The hate U give, Angie Thomas"))
    library.add_book(Book("Odyssey, Stephen Fry"))
    
    while True:
        print("Library menu")
        print("1. View all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit the program")
        
        choice = input("enter your choice (1-4): ")
        
        if choice == "1":
            library.list_books()
        
        elif choice == "2":
            title = input("Enter the title of the book you want to borrow: ")
            library.borrow_book(title)
            
        elif choice == "3":
            title = input("Enter the title of the book you want to return: ")    
            library.return_book(title)
            
        elif choice == "4":
            print("Exiting the library")
            
        else:
            print("Invalid choice. Please try again.")

if __name__ =="__main__":
    main()       
        
        
        
    