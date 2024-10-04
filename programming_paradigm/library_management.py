class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False 

    def check_out(self):
        """Mark the book as checked out"""
        if not self.__is_checked_out: 
            self.__is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as not checked out"""
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is available, False if checked out"""
        return not self.__is_checked_out

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class Library:
    def __init__(self):
        self._books = [] 
    def add_book(self, book):
        """Add a book to the library"""
        self._books.append(book)

    def check_out_book(self, title):
        """Attempt to check out a book by title. Returns a success message."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f"You have successfully checked out {book}."
                return f"{book} is already checked out."
        return f"Book titled '{title}' not found in the library."

    def return_book(self, title):
        """Attempt to return a book by title. Returns a success message."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return f"You have successfully returned {book}."
                return f"{book} was not checked out."
        return f"Book titled '{title}' not found in the library."

    def list_available_books(self):
        """Lists all available books in the library."""
        available_books = [str(book) for book in self._books if book.is_available()]
        if available_books:
            return "Available books:\n" + "\n".join(available_books)
        return "No books available in the library."



if __name__ == "__main__":

    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

   
    print("Available books after setup:")
    print(library.list_available_books())

    
    print("\n" + library.check_out_book("1984"))
    print("\nAvailable books after checking out '1984':")
    print(library.list_available_books())

    print("\n" + library.return_book("1984"))
    print("\nAvailable books after returning '1984':")
    print(library.list_available_books())
