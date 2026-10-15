#Before starting: define the file paths
#Windows paths contain backslashes.
#In Python, use a raw string (r"...") to avoid backslash escape problems.

folder = r"C:\Users\user\Documents\Python\data"

text_file = folder + r"\students.txt"
csv_file = folder + r"\students.csv"
json_file = folder + r"\students.json"
excel_file = folder + r"\students.xlsx"

print(text_file)
print(csv_file)

#What is file handling?
#A variable stores data temporarily while a program is running.
#A file allows data to be stored on a disk and used again later.
#For example, a student management program may need to store student names and marks
#even after the program terminates.


#A file can preserve the information:

file = open("student1.txt", "w")
file.write("Amit,85")
file.close()

#Important: mode "w" creates a file if it does not exist, but it overwrites existing content.

#Check whether your dataset files exist


#


#What does os.listdir(folder) do?
#It returns a list containing the names of the entries directly inside the specified directory. These #entries can be files or subdirectories

import os
#os is a built-in Python module.
#It provides functions to interact with the operating system.
#We can use it to check directories, list files, create folders,
#and work with file paths.
folder = r"C:\Users\user\Documents\Python\data"
#Component	Meaning
#folder	Variable that stores the folder path
#r	Makes the string a raw string
#Why do we use r before the string?
#In Python, the backslash (\) can introduce special escape sequences.
print("Folder exists:", os.path.isdir(folder))
#The function os.path.isdir() checks whether the given path refers
#to an existing directory.
#It returns a Boolean value: True or False.
if os.path.isdir(folder):
    print("Files available:")
    for filename in os.listdir(folder):
        print(filename)
#Expected result: Python prints whether the folder exists and,
#if it does, lists its contents.
#You should see the dataset files that is what the folder contains.
        
#Open and close a file
#The open() function opens a file and returns a file object.
#That object provides methods to read or write data.

file = open(text_file, "r", encoding="utf-8")

content = file.read()

print(content)

file.close()

#Here:
#- text_file is the path to your student text file.
#- "r" means read mode.
#- encoding="utf-8" supports common Unicode text.
#- read() reads the contents.
#- close() releases the file resource.

#File opening modes
#Mode	Purpose	        Important behaviour
#"r"	Read	        Fails if the file does not exist
#"w"	Write	        Creates or overwrites a file
#"a"	Append	        Adds data at the end; creates if missing
#"x"	Create	        Fails if the file already exists
#"r+"	Read and write	Existing file required
#"w+"	Read and write	Overwrites or creates
#"a+"	Read and append	Creates if missing; writes at the end

#Reading text files
#read(): read the entire file

file = open(text_file, "r", encoding="utf-8")
content = file.read()
print(content)
file.close()

#Read a limited number of characters 
#In Our Demo ,This reads up to the first 10 characters, not 10 lines or 10 words.
file = open(text_file, "r", encoding="utf-8")

print(file.read(10))

file.close()

#readline(): read one line at a time
#Each call reads the next line. If the file has reached the end, readline() returns an empty string.
print("readline(): read one line at a time")
file = open(text_file, "r", encoding="utf-8")

line1 = file.readline()
line2 = file.readline()

print("First line:", line1)
print("Second line:", line2)
file.close()
#readlines(): read all lines into a list
#If the file has three lines, lines will normally be a list of three strings.

print("Demo of readlines(): read all lines into a list ")


file = open(text_file, "r", encoding="utf-8")

lines = file.readlines()

print(lines)
print("Number of lines:", len(lines))

file.close()


#Compare the three methods

#Method	        Returns	                Typical use
#read()	        One string	        Read all text or a specified number of characters
#readline()	One string per call	Process lines individually
#readlines()	List of strings	        Work with all lines as a collection

#Writing, appending and the with statement

#write() and writelines()

practice_file = folder + r"\practice_notes.txt"

with open(practice_file, "w", encoding="utf-8") as file:
    file.write("Python File Handling\n")
    file.write("Working with student data\n")

print("\n\nPractice file created.")

#The write() method writes a string.
#It does not automatically add a newline, so include \n when required.

#Using writelines()
print("\n\nUsing writelines()")

lines = [
    "Read files\n",
    "Write files\n",
    "Handle exceptions\n"
]

with open(practice_file, "w", encoding="utf-8") as file:
    file.writelines(lines)
#writelines() writes the strings in the sequence without adding
#newline characters automatically.
#That is why each string above includes \n.

#Append without replacing existing content

with open(practice_file, "a", encoding="utf-8") as file:
    file.write("CSV processing\n")

print("New line appended.")

#Run the append program twice. The line will appear twice,
#because append mode adds content each time it runs.
#"w" replaces existing content; "a" preserves existing content and adds to it.

#Why use with?
#The with statement manages the file resource and closes it automatically when the block finishes,
#even if an exception occurs inside the block.

with open(text_file, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# The file is automatically closed here.
#Both patterns can close the file safely, but with is generally simpler and
#is the preferred approach for ordinary file access.

#File pointers: tell() and seek()
#A file pointer tracks the current position from which the next read or write operation occurs.

#tell() reports the current stream position.
#seek(0) moves the position back to the beginning for this text-file example
#repr() makes newline characters and other special characters easier to see.

with open(practice_file, "r", encoding="utf-8") as file:
    print("Initial position:", file.tell())

    print("Read:", repr(file.read(6)))
    print("Position now:", file.tell())

    file.seek(0)
    print("After seek:", file.tell())

    print("Read again:", repr(file.read(6)))

#Exceptions in file handling

#A program should not crash unexpectedly when a file is missing or inaccessible.
#Python provides exceptions to handle these situations.

missing_file = folder + r"\does_not_exist.txt"

try:
    with open(missing_file, "r", encoding="utf-8") as file:
        print(file.read())

except FileNotFoundError:
    print("Error: The requested file does not exist.")

except PermissionError:
    print("Error: Permission denied while accessing the file.")

#This program handles two specific errors:
#- FileNotFoundError: the file cannot be found at the specified path.
#- PermissionError: the operating system denies the requested access.

#Count lines, words and characters
#This combines reading, iteration and string processing.

try:
    with open(text_file, "r", encoding="utf-8") as file:
        content = file.read()

    lines = content.splitlines()
    words = content.split()
    characters = len(content)

    print("Number of lines:", len(lines))
    print("Number of words:", len(words))
    print("Number of characters:", characters)

except FileNotFoundError:
    print("Student text file was not found.")

except PermissionError:
    print("Permission denied.")

#How the counts work:
#- splitlines() separates the text into lines.
#- split() separates text using whitespace.
#- len(content) counts characters, including spaces and newline characters present in the string.


#Search for a word in a text file

search_word = "Pune"

try:
    with open(text_file, "r", encoding="utf-8") as file:
        content = file.read()

    count = content.lower().count(search_word.lower())

    print("Word searched:", search_word)
    print("Number of occurrences:", count)

except FileNotFoundError:
    print("File not found.")

#This counts case-insensitive substring occurrences, not necessarily whole words.
#For example, searching for "data" may also match "database".
#Whole-word searching requires a more precise approach.


#CSV files and your student dataset
#CSV means Comma-Separated Values. It is a text format commonly used to store tabular data,
#such as student IDs, names, marks, attendance and cities.
#We will use students.csv for the next demonstrations.

import csv

with open(csv_file, "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

#Each row is a list of strings. The first row may contain column headings,
#depending on how your file is structured.
#encoding="utf-8-sig" helps Python read UTF-8 CSV files that contain a byte-order mark.


#Read column names and student records

#If the CSV has a header row such as:
#StudentID,Name,Department,Marks,Attendance,City
#use csv.DictReader() to access fields by name.
#csv.DictReader() reads each row as a dictionary, using the column headings as dictionary keys.

import csv

with open(csv_file, "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    print("Columns:", reader.fieldnames)

    for student in reader:
        print(student["Name"], student["Marks"])

#Each student is represented by a dictionary-like row.
#The field names must match the actual column headers in your CSV.

#csv.reader() versus csv.DictReader()
        
#Feature	                csv.reader()	            csv.DictReader()
#Row representation	        List	                    Dictionary-like object
#Access	                        row[1]	                    row["Name"]
#Header handling	        Usually handled manually    Uses the first row as field names by default
#Useful when	                Column positions matter	    Column names improve readability



#Filter students by marks
#The dataset stores CSV values as strings.
#Convert numeric fields to int or float before performing numeric comparisons.


import csv

try:
    with open(csv_file, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for student in reader:
            marks = float(student["Marks"])

            if marks >= 75:
                print(student["Name"], marks)

except FileNotFoundError:
    print("CSV file not found.")

except KeyError as error:
    print("Required column is missing:", error)

except ValueError:
    print("A marks value is not numeric.")



#Count students by department

import csv

department_count = {}

with open(csv_file, "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for student in reader:
        department = student["Department"]

        department_count[department] = (
            department_count.get(department, 0) + 1
        )

print(department_count)







#Working with JSON and Excel
#Read JSON with the built-in json module
#The structure returned by json.load() depends on the file.
#If it contains a JSON array of student objects, it will normally return a list of dictionaries.

import json

try:
    with open(json_file, "r", encoding="utf-8") as file:
        students = json.load(file)

    print(type(students))
    print(students)

except FileNotFoundError:
    print("JSON file not found.")

except json.JSONDecodeError:
    print("The JSON file contains invalid JSON.")


#Read Excel with pandas


