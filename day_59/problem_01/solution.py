books = []

while True:
    print("1. Add book")
    print("2. Remove book")
    print("3. View books")
    print("4. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added!")
    
    elif choice == "2":
        book = input("Enter book to remove: ")
        if book in books:
            books.remove(book)
            print("Book removed!")
        else:
            print("Book not found!")
    
    elif choice == "3":
        print("Your books:")
        for book in books:
            print("-", book)
    
    elif choice == "4":
        break