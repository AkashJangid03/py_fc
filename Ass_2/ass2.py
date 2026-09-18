# Control Structure in Python - Assignment

# ======================================================================
# Problem 1: Sales Data Analysis for a Retail Store
# Question:
# Create a Python program that reads sales data, processes it, and provides insights such as total sales,
# average sales per product, top-selling products, and sales by category. The program should use appropriate
# data types and control structures (loops, conditionals, etc.) to accomplish these tasks.

# ======================================================================

sales = [
    {"product_name": "Laptop", "category": "Electronics", "units_sold": 50, "unit_price": 50000},
    {"product_name": "Phone", "category": "Electronics", "units_sold": 20, "unit_price": 20000},
    {"product_name": "Shirt", "category": "Clothing", "units_sold": 30, "unit_price": 1000},
    {"product_name": "Shoes", "category": "Clothing", "units_sold": 15, "unit_price": 2000}
]

# 1. Total Sales
total_sales = 0
for i in sales: 
    total_sales += i["units_sold"] * i["unit_price"]
print("Total Sales: ", total_sales)

# 2. Average Sales 
avg = total_sales / len(sales)
print("Average Sales per Prodcut: ", avg)

# 3. TOp Selling product 
top_product = sales[0]
for i in sales: 
    if i["units_sold"] > top_product["units_sold"]: 
        top_product = i 
print("The top sellong product: ", top_product["product_name"])

# 4. Sales by category
category_sales = {}
for i in sales: 
    category = i['category']
    amt = i["units_sold"] * i["unit_price"]
    if category in category_sales: 
        category_sales[category] += amt 
    else: 
        category_sales[category] = amt 
print("Sales by category: ")
for category in  category_sales: 
    print(category, ':', category_sales[category])


# ======================================================================
# Problem 2: Student Grades Management System
# Question:
# Create a Python program that manages student grades, performs various calculations, and provides insights
# such as the average grade, the top-performing students, and grade distribution. The student data is stored
# in a list of dictionaries, where each dictionary contains "student_name" and "grades" (a dictionary with
# course names as keys and grades as values).

# ======================================================================

students = [
    {"student_name": "Akash", "grades": {"Math": 85, "Science": 92, "English": 78}},
    {"student_name": "Ajay", "grades": {"Math": 75, "Science": 80, "English": 70}},
    {"student_name": "Rutik", "grades": {"Math": 90, "Science": 88, "English": 95}}
]

# 1. avg grade 
def avg_grade(student): 
    grades = student["grades"]
    total = 0
    for i in grades.values():
        total+=i
    average = total / len(grades)
    return average

# 2. Highest and lowest 
def high_low(student): 
    grades = student['grades']
    highest = max(grades.values())
    lowest = min(grades.values())
    return highest, lowest

# 3. Find top-performning student 
def top_student(student):
    top = student[0]
    for student in students: 
        if avg_grade(student) > avg_grade(top): 
            top = student
    return top["student_name"]

# 4. Categorize Student 
def cat_student(avg): 
    if avg >= 80:
        return "A"
    elif avg>=60:
        return "B"
    elif avg>=40:
        return 'C'
    else: 
        return "D"
        
for student in students: 
    avg = avg_grade(student)
    high, low = high_low(student)

    print("Student: ", student["student_name"])
    print("Average: ", avg) 
    print("Highest: ", high)
    print("Lowest: ", low)
    print("Grade: ", cat_student(avg))
print("Top student: ", top_student(students))


# ======================================================================
# Problem 3: Library Management System
# Question:
# Create a Python program that manages a library's book collection, tracks checkouts, and provides summaries
# such as the total number of books available, the most borrowed books, and overdue books. The book data is
# stored in a list of dictionaries containing "title", "author", "checked_out", and "due_date".

# ======================================================================

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


# ======================================================================
# Problem 4: Employee Attendance Tracker
# Question:
# Create a Python program that records and analyzes employee attendance, providing insights such as total
# hours worked, employees with perfect attendance, and those with the most absences. The attendance data is
# stored in a list of dictionaries containing "employee_name" and "attendance", where attendance is a
# dictionary with dates as keys and tuples of clock-in and clock-out times as values (strings in HH:MM format).

# ======================================================================

from datetime import datetime

employees = [
    {
        "employee_name": "Kishor Nand",
        "attendance": {
            "2026-09-01": ("09:00", "17:00"),
            "2026-09-02": ("09:15", "17:10"),
            "2026-09-03": ("09:00", "17:00")
        }
    },
    {
        "employee_name": "Shaam Kuru",
        "attendance": {
            "2026-09-01": ("09:00", "17:00"),
            "2026-09-02": ("09:00", "17:00")
        }
    }
]

#1. total hours worked 
def total_hours(employee): 
    total = 0 
    for date, times in employee["attendance"].items(): 
        clock_in = datetime.strptime(times[0], "%H:%M")
        clock_out = datetime.strptime(times[1], "%H:%M")
        hours = (clock_out - clock_in).seconds / 3600
        total += hours
    return total

# 2. absence
def absence(employee, total_days): 
    present_days = len(employee["attendance"])
    return total_days - present_days 



for employee in employees: 
    print("\nEmployee: ", employee["employee_name"])
    print("Total hours of working: ", total_hours(employee)) 
    print("Absence: ", absence(employee, 5))

