class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False  # Mark book as borrowed
            print(f"Great! {self.title} has been borrowed.")
        else:
            print(f"{self.title} is already borrowed.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True  # Mark book as available
            print(f"You have returned {self.title}.")
        else:
            print(f"{self.title} was not borrowed.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)  # Add book instance to the list

    def list_books(self):
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                availability = "Yes" if book.is_available else "No"
                print(f"Title: {book.title}, Author: {book.author}, Available: {availability}")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, title):
        book = self.find_book(title)
        if book:
            book.borrow()
        else:
            print(f"{title} is not available to borrow.")

    def return_book(self, title):
        book = self.find_book(title)
        if book:
            book.return_book()
        else:
            print(f"{title} is not available to return.")


def main():
    library = Library()

    # Add books to the library
    library.add_book(Book("The Fault in Our Stars", "John Green"))
    library.add_book(Book("The Hunger Games", "Suzanne Collins"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
    library.add_book(Book("The Hate U Give", "Angie Thomas"))
    library.add_book(Book("Odyssey", "Stephen Fry"))

    while True:
        print("\nLibrary Menu:")
        print("1. View all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit the program")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            library.list_books()

        elif choice == "2":
            title = input("Enter the title of the book you want to borrow: ")
            library.borrow_book(title)

        elif choice == "3":
            title = input("Enter the title of the book you want to return: ")
            library.return_book(title)

        elif choice == "4":
            print("Exiting the library. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
