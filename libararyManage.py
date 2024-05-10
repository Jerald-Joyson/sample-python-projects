class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False

    def check_out(self):
        self.checked_out = True

    def return_book(self):
        self.checked_out = False

    def __str__(self):
        status = "Checked out" if self.checked_out else "Available"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                return

    def checkout_book(self, isbn, member_id):
        for book in self.books:
            if book.isbn == isbn and not book.checked_out:
                book.check_out()
                for member in self.members:
                    if member.member_id == member_id:
                        member.check_out_book(book)
                        return

    def return_book(self, isbn, member_id):
        for member in self.members:
            if member.member_id == member_id:
                for book in member.checked_out_books:
                    if book.isbn == isbn:
                        book.return_book()
                        member.return_book(book)
                        return

    def __str__(self):
        book_list = "\n".join([str(book) for book in self.books])
        member_list = "\n".join([str(member) for member in self.members])
        return f"Library: {self.name}\nBooks:\n{book_list}\nMembers:\n{member_list}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.checked_out_books = []

    def check_out_book(self, book):
        self.checked_out_books.append(book)

    def return_book(self, book):
        self.checked_out_books.remove(book)

    def __str__(self):
        checked_out_books_str = "\n".join([f"- {book.title}" for book in self.checked_out_books])
        return f"Member ID: {self.member_id}, Name: {self.name}\nChecked out books:\n{checked_out_books_str}"


# Demo
if __name__ == "__main__":
    # Create books
    book1 = Book("Book 1", "Author 1", "123456")
    book2 = Book("Book 2", "Author 2", "234567")
    book3 = Book("Book 3", "Author 3", "345678")

    # Create members
    member1 = Member(1, "John")
    member2 = Member(2, "Alice")

    # Create library
    library = Library("My Library")

    # Add books and members to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_member(member1)
    library.add_member(member2)

    # Checkout books
    library.checkout_book("123456", 1)
    library.checkout_book("234567", 2)

    # Return books
    library.return_book("123456", 1)

    # Display library status
    print(library)
