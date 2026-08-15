
books = [
    {"id": 1, "title": "Python Basics", "author": "John Smith", "available": True},
    {"id": 2, "title": "SQL Fundamentals", "author": "David Lee", "available": True},
    {"id": 3, "title": "Data Analytics", "author": "Sarah Brown", "available": True}
]

def display_books():
    print("\n--- Library Books ---")
    for book in books:
        status = "Available" if book["available"] else "Issued"
        print(f"{book['id']} | {book['title']} | {book['author']} | {status}")


def search_book():
    keyword = input("Enter book title to search: ").lower()

    found = False

    for book in books:
        if keyword in book["title"].lower():
            status = "Available" if book["available"] else "Issued"
            print(f"{book['id']} | {book['title']} | {book['author']} | {status}")
            found = True

    if not found:
        print("Book not found.")


def issue_book():
    book_id = int(input("Enter book ID to issue: "))

    for book in books:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                print("Book issued successfully.")
            else:
                print("Book is already issued.")
            return

    print("Book ID not found.")


def return_book():
    book_id = int(input("Enter book ID to return: "))

    for book in books:
        if book["id"] == book_id:
            if not book["available"]:
                book["available"] = True
                print("Book returned successfully.")
            else:
                print("This book was not issued.")
            return

    print("Book ID not found.")


while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Display Books")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_books()

    elif choice == "2":
        search_book()

    elif choice == "3":
        issue_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        print("Thank you for using the Library Management System.")
        break

    else:
        print("Invalid choice. Please try again.")