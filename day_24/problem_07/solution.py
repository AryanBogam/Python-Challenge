students_books = {
    "Alice": ["Python Guide", "Data Structures", "Web Development"],
    "Bob": ["Java Basics", "Database Design"],
    "Charlie": ["Machine Learning", "AI Guide", "Statistics", "Python Guide", "Algorithms"],
    "Diana": ["Web Development", "JavaScript"]
}

print("Books borrowed by each student:")
for student, books in students_books.items():
    print(f"{student}: {len(books)} books")

max_books = 0
top_borrower = ""

for student, books in students_books.items():
    if len(books) > max_books:
        max_books = len(books)
        top_borrower = student

print(f"\nWho borrowed the most books: {top_borrower} with {max_books} books")