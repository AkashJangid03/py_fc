# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
#1. Write a program to determine all the Pythagorean triplets in the range of 100 to 1000. A Pythagorean triplet is a set of three integers I, j, k such that (i^2 + j^2 = k^2)  
for i in range(100, 1001):
    for j in range(i, 1001):
        for k in range(j, 1001):
            if i * i + j * j == k * k:
                print(i, j, k)

# %%
#3. write a program to print integers from 40 to 124 in decimal, octal, binary and hexadecimal using appropriate format specifiers. 
for i in range(40, 125):
    print("{:d}  {:o}  {:b}  {:x}".format(i, i, i, i))

# %%
#4. Write a Python program to calculate the sum of the first 10 prime numbers. 
count = 0
num = 2
total = 0
while count < 10:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        total = total + num
        count = count + 1
    num = num + 1
print("Sum of first 10 prime numbers =", total)

# %%
# 5. Write a program to read a set of numbers and calculate their average. The program should first ask the user for number of values to be entered and then prompt for each number. Maintain a running total; there is no need to store all the individual numbers. 
n = int(input("Enter the number of values "))
total = 0
for i in range(n): 
    num = float(input("enter number: "))
    total = total + num 
avg = total / n 
print("Average: ", avg)


# %%
# 6. Write a python program to find all the Armstrong numbers within a given range.
def armstrong_number(start, end):
    for i in range(start, end + 1):
        order = len(str(i))
        temp = i
        digit_sum = 0
        while temp > 0:
            digit = temp % 10
            digit_sum += digit ** order
            temp //= 10
        if i == digit_sum:
            print(i, end=" ")
start = int(input("starting number: "))
end = int(input("ending number: "))
armstrong_number(start, end)


# %%
# 7. Write a python program to find all the Strong numbers within a given range.
def strongnum(start, end): 
    for i in range(start, end+1): 
        temp = i
        total = 0
        while temp > 0:
            digit = temp %10
            tota += math.factorial(digit)
