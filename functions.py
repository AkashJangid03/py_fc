Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def cal_area(length, breadth):
    return length * breadth

cal_area(5,2)
10
cal_area(10, 5)
50
#-- difference between paramter and argument
#-- different ways of passing arguments 1. Positional argument, 2. Keyword argument, 3. Default Argument
def add(*number):
    total = 0
    for n in number:
        total += n
    return total

add(10, 20, 30, 40)
100
add(10, akash, 20.2)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    add(10, akash, 20.2)
NameError: name 'akash' is not defined. Did you mean: 'hash'?
def add(**number):
    total = 0
    for n in number:
        total += n
    return total

add(10, akash, 20.2)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    add(10, akash, 20.2)
NameError: name 'akash' is not defined. Did you mean: 'hash'?
def add(*number):
    total = 0
    for n in number:
        total += n
    return total

def std_details(**details):
    print(details)

    
std_deatails(
    name="Akash",
    age=22,
    course="M.Sc.CA")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    std_deatails(
NameError: name 'std_deatails' is not defined. Did you mean: 'std_details'?
std_details(
    name="Akash",
    age=22,
    course="M.Sc.CA")
{'name': 'Akash', 'age': 22, 'course': 'M.Sc.CA'}
std_deatils(
    name="Ajay
    
SyntaxError: unterminated string literal (detected at line 2)
std_deatils(
    name="Ajay",
    RollNo="256307")
    
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    std_deatils(
NameError: name 'std_deatils' is not defined. Did you mean: 'std_details'?
std_details(
    name="Ajay",
    RollNo="256307")
{'name': 'Ajay', 'RollNo': '256307'}
# multiple return values are allowed, returns tuple
def calculate:
    
SyntaxError: expected '('
def calculate(a, b):
    return a+b, a-b, a*b

calculate(10, 5)
(15, 5, 50)
a,b,c = calcualte(10,5)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a,b,c = calcualte(10,5)
NameError: name 'calcualte' is not defined. Did you mean: 'calculate'?
a,b,c = calculate(10,5)
print(a,b,c)
15 5 50



#-- types of variable
# local var , global var


# list passing in fucntion
def use_list (e):
    for e in even:
        print(e)

        
even = (0, 2, 4, 6, 8)
def use_list (e):
    for e in even:
        print(e)

        
use_list(even)
0
2
4
6
8
#-----
#dict passing in function
dic={"aaa":111, "bbb"=222, "ccc"=333, "ddd"=444}
SyntaxError: ':' expected after dictionary key
dic={"aaa":111, "bbb":222, "ccc":333, "ddd":444}
def use_dict (d):
    for d in dic:
        print(d)

        
use_dict(dic)
aaa
bbb
ccc
ddd
def use_dict (d):
    for d in dic:
        print(ddic[i])

        
use_dict(dic)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    use_dict(dic)
  File "<pyshell#73>", line 3, in use_dict
    print(ddic[i])
NameError: name 'ddic' is not defined. Did you mean: 'dic'?
def use_dict (d):
    for d in dic:
        print(d, dic[i])

        
use_dict(dic)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    use_dict(dic)
  File "<pyshell#76>", line 3, in use_dict
    print(d, dic[i])
NameError: name 'i' is not defined. Did you mean: 'id'?
def use_dict (d):
    for d in dic:
        print(d, d[i])

        
use_dict(dic)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    use_dict(dic)
  File "<pyshell#79>", line 3, in use_dict
    print(d, d[i])
NameError: name 'i' is not defined. Did you mean: 'id'?
def use_dict (d):
    for d in dic:
        print(d, dic[d])

        
use_dict(dic)
aaa 111
bbb 222
ccc 333
ddd 444




#-- function calling fucntion
def func1():
    print("Bye wolrd")

    
def func2():
    print("Leave the wolrd")

    
def f1():
    print("Bye wolrd")
    def f2():
        print("see you
              
SyntaxError: unterminated string literal (detected at line 4)
def f1():
    print("Bye wolrd")
    def f2():
        print("see you")

        
f2()
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    f2()
NameError: name 'f2' is not defined. Did you mean: 'f1'?
f1
<function f1 at 0x0000022B07B49580>
f1()
Bye wolrd



#--- recussion function
#--- factorial function
n=int(input("number": )
      
SyntaxError: invalid syntax
n=int(input("number :" ))
      
number :5
def fact(n):
    for i range(1,n):
        
SyntaxError: invalid syntax
def fact(n):
    for i in range(1,n)
    
SyntaxError: expected ':'
def fact(n):
    for i in range(1,n):
        sum=n*i

        
def fact(n):
    for i in range(1,n):
        sum=n*i
    return sum

>>> fact(5)
20
>>> def fact(n):
...     for i in range(1,n+1):
...         sum=n*i
...     return sum
... 
>>> fact(5)
25
>>> #---
>>> 
>>> #--
>>> def fact(n):
...     if n == 0:
...         fact = i*fact(n-1)
...     return fact
... 
>>> fact(5)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    fact(5)
  File "<pyshell#135>", line 4, in fact
    return fact
UnboundLocalError: cannot access local variable 'fact' where it is not associated with a value
>>> def fact(n):
...     if n == 0:
...         fact = i*fact(n-1)
...     return fact
... 
>>> # lambda function
>>> # what is the need of anonymous funciton
>>> # what is the need of lambda fucntion justify when to use it
>>> 
>>> 
>>> 
>>> # case study
>>> '''
... A company wants to develop a simmple employee management system using py
... 
