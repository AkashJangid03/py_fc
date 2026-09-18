books = [
    {
        "title": "Prithviraj Raso",
        "author": "Chand Bardai",
        "checked_out": True,
        "due_date": "2026-09-01",
        "borrow_count": 15
    },
    {
        "title": "Five Point Someone",
        "author": "Chetan Bhagat",
        "checked_out": False,
        "due_date": "",
        "borrow_count": 20
    },
    {
        "title": "Rich Dad Poor Dad",
        "author": "Robert Kiyosaki",
        "checked_out": True,
        "due_date": "2026-09-10",
        "borrow_count": 25
    },
    {
        "title": "Surrounded by Idiots",
        "author": "Thomas Erikson",
        "checked_out": True,
        "due_date": "2026-09-03",
        "borrow_count": 50
    }
]

# 1. Total No of  books
def total_books(books):
    return len(books)

# 2. Avaulable books
def available_books(books): 
    count =0
    for i in books: 
        if i["checked_out"] == True: 
            count +=1
    return count

# 3. Checked-out books
def checked_out_books(books): 
    names = []
    for i in books:
        if i["checked_out"] == True:
            names.append(i["title"])
    return names

# 4. most borrowed book
def most_borrowed_book(books): 
    most = books[0]
    for i in books: 
        if i["borrow_count"] > most["borrow_count"]:
            most = i
    return most["title"]

# 5. overdue books  
from datetime import datetime
def overdue_books(books):
    today = datetime.today().date()
    overdue = []
    for book in books:
        if book["checked_out"] == True:
            due_date = datetime.strptime(book["due_date"], "%Y-%m-%d").date()
            if due_date < today:
                overdue.append(book["title"])
    return overdue
    
print("Total books: ", total_books(books))
print("Available Books: ", available_books(books))
print("Check-out books names: ", checked_out_books(books))
print("Most borrowed Book: ", most_borrowed_book(books))
print("Overdue Books:", overdue_books(books))