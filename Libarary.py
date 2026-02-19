class Library:
    def __init__(self, book_list):
        self.books = book_list

    def display_books(self):
        print("\nAvailable Books:")
        if not self.books:
            print("The library is currently empty.")
        for index, book in enumerate(self.books, 1):
            print(f"{index}. {book}")

    def lend_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"Success: You have borrowed '{book_name}'.")
        else:
            print(f"Error: '{book_name}' is not in stock.")

    def return_book(self, book_name):
        # Prevent adding duplicates if the library already has it
        if book_name not in self.books:
            self.books.append(book_name)
            print(f"Success: You have returned '{book_name}'.")
        else:
            print(f"Note: '{book_name}' was already in the library.")

    # --- NEW: Search Feature ---
    def search_book(self, query):
        results = [b for b in self.books if query.lower() in b.lower()]
        if results:
            print(f"\nFound {len(results)} match(es):")
            for b in results: print(f"- {b}")
        else:
            print(f"No books found matching '{query}'.")

def main():
    my_library = Library(["Python Basics", "Jenkins CI/CD", "Data Science 101"])
    
    while True:
        print("\n--- Library Menu ---")
        print("1. Display\n2. Borrow\n3. Return\n4. Search\n5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            my_library.display_books()
        elif choice == '2':
            book = input("Enter book name: ")
            my_library.lend_book(book)
        elif choice == '3':
            book = input("Enter book name: ")
            my_library.return_book(book)
        elif choice == '4':
            query = input("Search for: ")
            my_library.search_book(query)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
