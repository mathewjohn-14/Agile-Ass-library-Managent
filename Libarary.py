import json
import os

class Library:
    def __init__(self, filename="library_data.json"):
        self.filename = filename
        self.books = self.load_data()

    def load_data(self):
        """Task: Load library from a file or create default if missing."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return {"Python Basics": 3, "Jenkins CI/CD": 1, "Data Science 101": 2}

    def save_data(self):
        """Task: Save current inventory to file."""
        with open(self.filename, 'w') as f:
            json.dump(self.books, f, indent=4)

    def display_books(self):
        print("\n--- Current Inventory ---")
        if not self.books:
            print("Library is empty.")
        else:
            for book, count in self.books.items():
                status = "Available" if count > 0 else "OUT OF STOCK"
                print(f"- {book} [{count} copies] ({status})")

    def lend_book(self, book_name):
        if self.books.get(book_name, 0) > 0:
            self.books[book_name] -= 1
            print(f"✔ Success: '{book_name}' borrowed.")
            self.save_data()
        else:
            print(f"✘ Error: '{book_name}' is unavailable.")

    def return_book(self, book_name):
        self.books[book_name] = self.books.get(book_name, 0) + 1
        print(f"✔ Success: '{book_name}' returned.")
        self.save_data()

    def search_book(self, query):
        results = [b for b in self.books if query.lower() in b.lower()]
        if results:
            print(f"\nResults for '{query}':")
            for b in results: print(f"- {b} ({self.books[b]} left)")
        else:
            print("No matches found.")

def main():
    my_library = Library()
    
    menu = {
        '1': ("Display Books", my_library.display_books),
        '2': ("Borrow Book", lambda: my_library.lend_book(input("Book name: "))),
        '3': ("Return Book", lambda: my_library.return_book(input("Book name: "))),
        '4': ("Search", lambda: my_library.search_book(input("Keyword: "))),
        '5': ("Exit", exit)
    }

    while True:
        print("\n=== LIBRARY SYSTEM V3 ===")
        for key, value in menu.items():
            print(f"{key}. {value[0]}")
        
        choice = input("Select option: ")
        if choice in menu:
            if choice == '5': break
            menu[choice][1]()
        else:
            print("Invalid Option.")

if __name__ == "__main__":
    main()
