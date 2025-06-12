"""
Library Management System

This module implements a basic library management system using OOP principles.
It includes classes for managing books and library operations such as checking
books in and out, and tracking availability.
"""


class Book:
    """
    Represents a book in the library system.
    
    This class encapsulates book information and tracks whether the book
    is currently checked out or available.
    """
    
    def __init__(self, title, author):
        """
        Initialize a new book.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability
    
    def check_out(self):
        """
        Mark the book as checked out.
        
        Returns:
            bool: True if book was successfully checked out, False if already checked out
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """
        Mark the book as returned (available).
        
        Returns:
            bool: True if book was successfully returned, False if already available
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """
        Check if the book is available for checkout.
        
        Returns:
            bool: True if book is available, False if checked out
        """
        return not self._is_checked_out
    
    def __str__(self):
        """
        String representation of the book.
        
        Returns:
            str: Formatted string with title and author
        """
        return f"{self.title} by {self.author}"


class Library:
    """
    Represents a library that manages a collection of books.
    
    This class provides functionality to add books, check them out,
    return them, and list available books.
    """
    
    def __init__(self):
        """Initialize a new library with an empty collection of books."""
        self._books = []  # Private list to store Book instances
    
    def add_book(self, book):
        """
        Add a new book to the library collection.
        
        Args:
            book (Book): A Book instance to add to the library
        """
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print("Error: Only Book instances can be added to the library.")
    
    def check_out_book(self, title):
        """
        Check out a book by title.
        
        Args:
            title (str): The title of the book to check out
            
        Returns:
            bool: True if book was found and checked out successfully, False otherwise
        """
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                    return True
                else:
                    print(f"'{title}' is already checked out.")
                    return False
        
        print(f"Book '{title}' not found in the library.")
        return False
    
    def return_book(self, title):
        """
        Return a book by title.
        
        Args:
            title (str): The title of the book to return
            
        Returns:
            bool: True if book was found and returned successfully, False otherwise
        """
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                    return True
                else:
                    print(f"'{title}' was not checked out.")
                    return False
        
        print(f"Book '{title}' not found in the library.")
        return False
    
    def list_available_books(self):
        """
        Display all available books in the library.
        
        Prints each available book's title and author to the console.
        If no books are available, prints an appropriate message.
        """
        available_books = [book for book in self._books if book.is_available()]
        
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books are currently available.")
    
    def list_all_books(self):
        """
        Display all books in the library with their status.
        
        Shows both available and checked out books with their current status.
        """
        if not self._books:
            print("The library has no books.")
            return
        
        print("All books in the library:")
        for book in self._books:
            status = "Available" if book.is_available() else "Checked Out"
            print(f"{book} - {status}")
    
    def get_book_count(self):
        """
        Get the total number of books in the library.
        
        Returns:
            int: Total number of books in the library
        """
        return len(self._books)
    
    def get_available_count(self):
        """
        Get the number of available books in the library.
        
        Returns:
            int: Number of available books
        """
        return sum(1 for book in self._books if book.is_available())
