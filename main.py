class Library:
    def __init__(self):
        self.books = []       # ખાલી list initially
        self.no_of_books = 0  # count initially 0

    def add_book(self, book_name):
        self.books.append(book_name)
        self.no_of_books += 1

    def show_books(self):
        print("\nBooks in Library:", self.books)

    def get_no_of_books(self):
        return self.no_of_books


lib = Library()

print('++++++ Welcome to the Meet Library 📚 ++++++')

while True:
    print('\nPress 1. to Enter book to Library.')
    print('Press 2. to Exit Library.')

    choice = input("\nEnter your choice: ")

    if choice == "1":
        book_name = input("Enter book name: ")
        lib.add_book(book_name)
        print(f"'{book_name}' added successfully!")

        print("\nCurrent Books:", lib.books)
        print("Total Books:", lib.get_no_of_books())

    elif choice == "2":
        print("\nThank you for visiting Meet Library 📚")
        break

    else:
        print("\nInvalid Choice! Please press 1 or 2.")
