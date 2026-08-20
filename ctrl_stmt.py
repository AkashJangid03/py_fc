Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# if stmt
# control stmt
age  = 20
if age >= 18:
    print("Eligible")
else:
    print("not eligible")

    
Eligible
# ---
salary = 50000
if salary>=80000:
    print("A")
elif salary >= 60000:
    print("B")
elif salary >= 40000:
    print("C")
else:
    print("D")

C
# ---
username = "admin"
password = "12234"

if username=="admin":
    if password=="12234":
        print("Login Successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")

Login Successful
# -- foor loop
skills = ['Pyhton', 'Power BI', 'Excel', 'SQl']
for x in skills:
    print(skills)

['Pyhton', 'Power BI', 'Excel', 'SQl']
['Pyhton', 'Power BI', 'Excel', 'SQl']
['Pyhton', 'Power BI', 'Excel', 'SQl']
['Pyhton', 'Power BI', 'Excel', 'SQl']
for x in skills:
    print(x)

    
Pyhton
Power BI
Excel
SQl

# -- range
for i in range(5):
    print(i)

    
0
1
2
3
4
for i in range(1, 6):
    print(i)

...     
1
2
3
4
5
>>> # range (start, stop, step)
>>> for i in range (2, 11, 2):
...     print (i)
... 
...     
2
4
6
8
10
>>> for i in range (10, 0, -1)
SyntaxError: expected ':'
>>> for i in range (10, 0, -1):
...     print(i)
... 
...     
10
9
8
7
6
5
4
3
2
1
>>> for i in range (1, 10, 3):
...     print(i)
... 
...     
1
4
7


while True: 
	Name=input("Enter the name : ")
	Marks=int(input("Enter the mareks: "))
	print(Name, Marks)
	c = input("Enter you choice y/n: ")
	if c=="n": 
		exit()


---
attendance = [50, 40, 90, 80, 76, 75, 12, 61, 73, 10] 
for x in attendance: 
	if (x >= 75): 
		print("eligible")
	else: 
		print("not eligible")


for x in attendance: 
	if (x >= 75):
		count+=1
print(count)