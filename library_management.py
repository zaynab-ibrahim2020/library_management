class Book:
    """Store the details and availability of one book."""

    def __init__(self, title, author):
        # These attributes store information about this Book object.
        self.title = title
        self.author = author
        self.available = True


class Member:
    """Store the name of a library member."""

    def __init__(self, name):
        self.name = name


class Library:
    """Manage books and members in one library."""

    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self):
        # Create a Book object and add it to the library list.
        title = input("Enter book title: ")
        author = input("Enter author: ")
        self.books.append(Book(title, author))
        print(f"{title} successfully added")

    def add_member(self):
        # Create a Member object and add it to the member list.
        name = input("Enter member name: ")
        self.members.append(Member(name))
        print(f"{name} successfully registered")

    def borrow_book(self):
        title = input("Enter book title: ")

        # Search the collection until the requested title is found.
        for book in self.books:
            if book.title == title:
                # The available attribute tells us if the book can be borrowed.
                if not book.available:
                    print("That book is already borrowed.")
                else:
                    book.available = False
                    print("Book borrowed")
                return

        print("Entered book doesn't exist in the library.")

    def return_book(self):
        title = input("Enter book title: ")

        # Returning a book changes only that book's availability.
        for book in self.books:
            if book.title == title:
                book.available = True
                print("Book returned")
                return

        print("Entered book doesn't exist in the library.")

    def display_books(self):
        for book in self.books:
            availability = "Yes" if book.available else "No"
            print(f"Title: {book.title} - Author: {book.author} - Available: {availability}")


def run_library_menu():
    """Run the text menu used to interact with the library."""
    # This function reads the user's choice and calls a Library method.
    library = Library()

    while True:
        print("\n1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display Books")
        print("6. Exit")

        choice = input("Choose: ")

        # Each choice calls a method that performs one library action.
        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.add_member()
        elif choice == "3":
            library.borrow_book()
        elif choice == "4":
            library.return_book()
        elif choice == "5":
            library.display_books()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Please choose a number from 1 to 6.")


if __name__ == "__main__":
    # The menu runs only when this file is started directly.
    run_library_menu()