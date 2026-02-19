import json
import os
from datetime import datetime

class Book:
    def __init__(self, title, quantity):
        self.title = title
        self.quantity = quantity

    def to_dict(self):
        return {"title": self.title, "quantity": self.quantity}

class Library:
    def __init__(self, filename="library_v4.json"):
        self.filename = filename
        self.books = self.load_data()
        self.log_file = "library_activity.log"

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return [Book(b['title'], b['quantity']) for b in data]
        # Default starting stock
        return [Book("Python Basics", 3), Book("Jenkins CI/CD", 1)]

    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump([b.to_dict() for b in self.books], f, indent=4)

    def log_action(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as f:
            f.write(f"[{timestamp}] {message}\n")

    def display_books(self):
        print(f"\n{'ID':<5} {'Title':<20} {'Stock':<10}")
        print("-" * 35)
        for idx, b in enumerate(self.books, 1):
            print(f"{idx:<5} {b.title:<20} {b.quantity:<10}")

    def lend_book(self, index):
        try:
            book = self.books[int(index) - 1]
            if book.quantity > 0:
                book.quantity -= 1
                print(f"✔ Borrowed: {book.title}")
                self.log_action(f"LENT: {book.title}")
                self.save_data()
            else:
                print("✘ Out of stock!")
        except (IndexError, ValueError):
            print("✘ Invalid ID.")

    def return_book(self, title):
        # Check if book exists, if not, add it
        found = False
        for b in self.books:
            if b.title.lower() == title.lower():
                b.quantity += 1
                found = True
                break
        if not found:
            self.books.append(Book(title, 1))
        
        print(f"✔ Returned: {title}")
        self.log_action(f"RETURNED: {title}")
        self.save_data()

def main():
    lib = Library()
    while True:
        print("\n=== SYSTEM V4: OBJECT-ORIENTED ===")
        print("1. View All\n2. Borrow (by ID)\n3. Return (by Name)\n4. Exit")
        choice = input("Action: ")

        if choice == '1':
            lib.display_books()
        elif choice == '2':
            lib.display_books()
            lib.lend_book(input("Enter Book ID: "))
        elif choice == '3':
            lib.return_book(input("Enter Book Title: "))
        elif choice == '4':
            break

if __name__ == "__main__":
    main()
