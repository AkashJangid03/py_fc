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