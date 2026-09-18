# 1. Write a program to determine all the Pythagorean triplets in the range of 100 to 1000. A Pythagorean triplet is a set of three integers i, j, k such that i² + j² = k²
for i in range(100, 1001):
    for j in range(i, 1001):
        for k in range(j, 1001):
            if i*i + j*j == k*k:
                print(i, j, k)

print("----------------------------------------------------")
print("----------------------------------------------------")

# 2. Write a program that accepts a number from the user and adds 1 to each digit
n = input("Enter a number: ")
result = ""
for digit in n: 
    d = int(digit)
    d = (d+1)%10
    result = result + str(d)
print(result)

print("----------------------------------------------------")
print("----------------------------------------------------")

# 3. Write a program to print integers from 40 to 127 in decimal, octal, binary and hexadecimal using appropriate format specifiers.
for i in range (40, 128):
    print("{:d} {:o} {:b} {:x}".format(i, i, i, i))

print("----------------------------------------------------")
print("----------------------------------------------------")

# 4. Write a program to calculate sum of first 10 prime numbers 
count=0
num = 2
sum = 0
while count < 10:
    prime = True
    for i in range (2, num):
        if num%i==0:
            prime = False
            break
    if prime: 
        print(num)
        sum = sum + num 
        count = count + 1
    num = num + 1
print("Sum:: ", sum)

print("----------------------------------------------------")
print("----------------------------------------------------")

# 5. Write a program to read a set of numbers and calcualte their average. Thr program shoudl first ask the user for number of values to be enetred and then prompt for each number. Maintain a runnign total; there is no need to store all the individual numbers
n = int(input("Enter a number: "))
total = 0
for i in range(n):
    num = float(input("Enter the values: "))
    total = total + num 
average = total / n
print("Average: ", average)

print("----------------------------------------------------")
print("----------------------------------------------------")

# 6. Find all the Armstrong numbers within given range
def is_armstrong(start, end):
    for num in range(start, end+1):
        temp = num 
        sum = 0
        digits = len(str(num))
        while temp > 0:
            digit = temp % 10
            sum = sum + digit ** digits
            temp = temp // 10
        if sum == num: 
            print(num)
start= int(input("Enter starting number: "))
end = int(input("Enter the ending number: "))
is_armstrong(start, end)

print("----------------------------------------------------")
print("----------------------------------------------------")

# 7. Find all the Strong numbers within a given range
def is_strong(start, end):
    for num in range (start, end+1):
        temp = num 
        sum = 0
        while temp > 0: 
            digit = temp % 10
            fact = 1
            for i in range(1, digit+1):
                fact = fact * i 
            sum = sum + fact
            temp = temp // 10
        if sum == num: 
            print(num)
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
is_strong(start, end)

print("----------------------------------------------------")
print("----------------------------------------------------")

# 8. Square star pattern 
def square(n):
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1 or j==0 or j==n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
square(5)

# 9. print all integers between 1 and n that are not divisible by either 2 or 3. The program should also count and display the number of such integers. 
def div2n3(n):
    count = 0
    for i in range(1, n+1):
        if i%2!=0 and i%3!=0:
            print(i, end=", ")
            count += 1
    print("\nCount= ", count)
n = int(input("Enter a number: "))
div2n3(n)

print("----------------------------------------------------")
print("----------------------------------------------------")

# 10. Print the pattern
def pattern(n):
    for i in range(n):
        for j in range(n):
            if i==n//2 and j==n//2:
                print("@", end=" ")
            else:
                print("*", end=" ")
        print()
pattern(5)

print("----------------------------------------------------")
print("----------------------------------------------------")

# 11. Pascal Tree
def pascal(n):
    for i in range(n):
        num = 1
        for j in range(i+1):
            print(num, end=" ")
            num = num * (i-j)//(j+1)
        print()
n = int(input("Enter a number: "))
pascal(n)

print("----------------------------------------------------")
print("----------------------------------------------------")

# 12. Calculate the sum of the following series Sum=1+ 1/2! + 1/3! + 1/4! ... + 1/n!
def sum_of_series(n):
    sum = 1
    fact = 1
    for i in range(2, n+1):
        fact = fact * i
        sum = sum + 1/fact
    print(sum)
n=int(input("Enter a number: "))
sum_of_series(n)

print("----------------------------------------------------")
print("----------------------------------------------------")

# 13. Table of odd numbers in given range
def mul_table(start, end):
    for num in range(start, end+1):
        if num % 2 != 0:
            print("\nTable of ", num)
            for i in range(1, 11):
                print(num, "x", i, "=", num*i)
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
mul_table(start, end)

print("----------------------------------------------------")
print("----------------------------------------------------")

# 14. Print the triangle
def triangle(n):
    for i in range(1, n+1):
        print(" " *(n-i), end="")
        for j in range(i):
            print("*", end=" ")
        print()
n = int(input("Enter number of rows: "))
triangle(n)
