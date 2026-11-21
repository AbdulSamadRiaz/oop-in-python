
class Book:

    def __init__(self, title, author, availability):
        self.title = title
        self.author = author
        self.availability = availability

    def display_book(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

        if self.availability:
            print("Availability: Available")
        else:
            print("Availability: Borrowed")

    def borrow_book(self):
        if self.availability:
            self.availability = False
            print("Book borrowed successfully!")
        else:
            print("Book is already borrowed.")

    def return_book(self):
        if not self.availability:
            self.availability = True
            print("Book returned successfully!")
        else:
            print("Book is already available.")


book1 = Book("Math", "Newton", True)

book1.display_book()
print()

book1.borrow_book()
book1.display_book()
print()

book1.return_book()
book1.display_book()
