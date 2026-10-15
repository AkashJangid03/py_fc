# ============================================================
# CASE STUDY: STUDENT RECORD ANALYSIS SYSTEM
# Text File Handling
# File: students.txt
#
# Format:
# StudentID,Name,Department,Marks,Attendance,City
# ============================================================


# ------------------------------------------------------------
# 1. READ COMPLETE FILE USING read()
# File Opening Modes:
# r  -> Read
# w  -> Write / Overwrite
# a  -> Append
# x  -> Create a new file
# ------------------------------------------------------------

print("========== COMPLETE STUDENT DATA ==========")

file = open("students.txt", "r")

data = file.read()

print(data)

file.close()


# ------------------------------------------------------------
# 2. READ AND PROCESS RECORDS LINE-BY-LINE
# ------------------------------------------------------------

print("\n========== STUDENT DETAILS ==========")

file = open("students.txt", "r")

for line in file:

    # Remove newline character
    line = line.strip()

    # Separate fields
    data = line.split(",")

    student_id = data[0]
    name = data[1]
    department = data[2]
    marks = int(data[3])
    attendance = int(data[4])
    city = data[5]

    print("ID:", student_id)
    print("Name:", name)
    print("Department:", department)
    print("Marks:", marks)
    print("Attendance:", attendance)
    print("City:", city)
    print("----------------------------")

file.close()


# ------------------------------------------------------------
# 3. STUDENTS WHO SCORED MORE THAN 80
# ------------------------------------------------------------

print("\n========== STUDENTS WITH MARKS > 80 ==========")

file = open("students.txt", "r")

for line in file:

    data = line.strip().split(",")

    name = data[1]
    marks = int(data[3])

    if marks > 80:
        print(name, ":", marks)

file.close()


# ------------------------------------------------------------
# 4. STUDENTS WITH ATTENDANCE BELOW 75%
# ------------------------------------------------------------

print("\n========== ATTENDANCE BELOW 75% ==========")

file = open("students.txt", "r")

for line in file:

    data = line.strip().split(",")

    name = data[1]
    attendance = int(data[4])

    if attendance < 75:
        print(name, ":", attendance)

       
file.close()


# ------------------------------------------------------------
# 5. TOTAL NUMBER OF STUDENTS
# ------------------------------------------------------------

count = 0

file = open("students.txt", "r")

for line in file:
    count = count + 1

file.close()

print("\n========== TOTAL STUDENTS ==========")
print("Total Students:", count)


# ------------------------------------------------------------
# 6. CALCULATE AVERAGE MARKS
# ------------------------------------------------------------

total_marks = 0
count = 0

file = open("students.txt", "r")

for line in file:

    data = line.strip().split(",")

    marks = int(data[3])

    total_marks = total_marks + marks
    count = count + 1

file.close()

average_marks = total_marks / count

print("\n========== AVERAGE MARKS ==========")
print("Average Marks:", average_marks)


# ------------------------------------------------------------
# 7. FIND HIGHEST AND LOWEST MARKS
# ------------------------------------------------------------

highest_marks = -1
lowest_marks = 101

highest_student = ""
lowest_student = ""

file = open("students.txt", "r")

for line in file:

    data = line.strip().split(",")

    name = data[1]
    marks = int(data[3])

    if marks > highest_marks:
        highest_marks = marks
        highest_student = name

    if marks < lowest_marks:
        lowest_marks = marks
        lowest_student = name

file.close()

print("\n========== HIGHEST AND LOWEST MARKS ==========")
print("Highest:", highest_student, "-", highest_marks)
print("Lowest :", lowest_student, "-", lowest_marks)


# ------------------------------------------------------------
# 8. DEPARTMENT-WISE STUDENT COUNT
# ------------------------------------------------------------

mca_count = 0
msc_count = 0

file = open("students.txt", "r")

for line in file:

    data = line.strip().split(",")

    department = data[2]

    if department == "MCA":
        mca_count = mca_count + 1

    elif department == "MSc":
        msc_count = msc_count + 1

file.close()

print("\n========== DEPARTMENT-WISE COUNT ==========")
print("MCA Students:", mca_count)
print("MSc Students:", msc_count)


# ------------------------------------------------------------
# 9. SEARCH STUDENT BY ID
# ------------------------------------------------------------

print("\n========== SEARCH STUDENT ==========")

search_id = input("Enter Student ID: ")

found = False

file = open("students.txt", "r")

for line in file:

    data = line.strip().split(",")

    if data[0] == search_id:

        print("Student ID :", data[0])
        print("Name       :", data[1])
        print("Department :", data[2])
        print("Marks      :", data[3])
        print("Attendance :", data[4])
        print("City       :", data[5])

        found = True
        break

file.close()

if found == False:
    print("Student not found.")


# ------------------------------------------------------------
# 10. SEARCH STUDENTS BY CITY
# ------------------------------------------------------------

print("\n========== SEARCH BY CITY ==========")

search_city = input("Enter City: ")

found = False

file = open("students.txt", "r")

for line in file:

    data = line.strip().split(",")

    if data[5].lower() == search_city.lower():

        print(
            data[0],
            data[1],
            data[2],
            data[3],
            data[4]
        )

        found = True

file.close()

if found == False:
    print("No students found from this city.")


# ------------------------------------------------------------
# 11. ADD A NEW STUDENT
# ------------------------------------------------------------

print("\n========== ADD NEW STUDENT ==========")

student_id = input("Enter Student ID: ")
name = input("Enter Name: ")
department = input("Enter Department: ")
marks = input("Enter Marks: ")
attendance = input("Enter Attendance: ")
city = input("Enter City: ")

file = open("students.txt", "a")

file.write(
    student_id + "," +
    name + "," +
    department + "," +
    marks + "," +
    attendance + "," +
    city + "\n"
)

file.close()

print("Student added successfully.")



