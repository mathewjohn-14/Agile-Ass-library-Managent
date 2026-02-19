class Library:
    def __init__(self, book_list):
        self.books = book_list

    def display_books(self):
        print("\nAvailable Books:")
        for index, book in enumerate(self.books, 1):
            print(f"{index}. {book}")

    def lend_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"Success: You have borrowed '{book_name}'.")
        else:
            print("Error: Book not available.")

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"Success: You have returned '{book_name}'.")

def main():
    my_library = Library(["Python Basics", "Jenkins CI/CD", "Data Science 101"])
    
    while True:
        print("\n--- Library Menu ---")
        print("1. Display Books\n2. Borrow Book\n3. Return Book\n4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            my_library.display_books()
        elif choice == '2':
            book = input("Enter book name to borrow: ")
            my_library.lend_book(book)
        elif choice == '3':
            book = input("Enter book name to return: ")
            my_library.return_book(book)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
