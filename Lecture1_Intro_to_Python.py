Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
help
Type help() for interactive help, or help(object) for help about object.
help()
Welcome to Python 3.12's help utility! If this is your first time using
Python, you should definitely check out the tutorial at
https://docs.python.org/3.12/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To get a list of available
modules, keywords, symbols, or topics, enter "modules", "keywords",
"symbols", or "topics".

Each module also comes with a one-line summary of what it does; to list
the modules whose name or summary contain a given string such as "spam",
enter "modules spam".

To quit this help utility and return to the interpreter,
enter "q" or "quit".

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
print("bye python")
bye python
name = "akash"
print(name)
akash
age = 18
print(name, age)
akash 18
print("Name: ", name, ", Age : ", age)
Name:  akash , Age :  18
name = input("Enter your name: ")
Enter your name: Akash
age = int(intput("Enter your age: ")
          )
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    age = int(intput("Enter your age: ")
NameError: name 'intput' is not defined. Did you mean: 'input'?
age = int(intput("Enter your age: "))
              
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    age = int(intput("Enter your age: "))
NameError: name 'intput' is not defined. Did you mean: 'input'?
age = int(input("Enter your age: "))
              
Enter your age: 22
print("Name: ",name,", Age: ",age)
              
Name:  Akash , Age:  22
print("Akash"\"22"\"MScCA")
              
SyntaxError: unexpected character after line continuation character
print("Akash", \"22", \"MScCA"
      
SyntaxError: unexpected character after line continuation character
print("Akash", \"22", \"MScCA")
      
SyntaxError: unexpected character after line continuation character
print("Akash",\"22", \"MScCA")
      
SyntaxError: unexpected character after line continuation character
print("akash", \
      "22",\
      "MScCA
      
SyntaxError: unterminated string literal (detected at line 3)
print("akash", \
      "22",\
      "MScCA")
      
akash 22 MScCA
list = [1,2,3,
        4,5,
        6
        ,7,8]
      
list
      
[1, 2, 3, 4, 5, 6, 7, 8]
    print('0')
      
SyntaxError: unexpected indent
''' indent -> mark the start of new code
dedent-> mark the end of the student '''
      
' indent -> mark the start of new code\ndedent-> mark the end of the student '
# Variable: is an identifier that refers to an obvject value in memory
      
# Dynamic and Static typed
      

x=10
      
print(x)
      
10
print(id(x))
      
140721468345048
y=x
      
print(id(y))
      
140721468345048
j=10
      
print(id(j))
      
140721468345048
x=12
      
print(id(x)); print(id(y)); print(id(j))
      
140721468345112
140721468345048
140721468345048
140721468345048
      
140721468345048
y=18
      
print(id(x)); print(id(y)); print(id(j))
      
140721468345112
140721468345304
140721468345048
x=x+4
      
print(id(x)); print(id(y)); print(id(j))
      
140721468345240
140721468345304
140721468345048
>>> x=x+2
...       
>>> print(id(x)); print(id(y)); print(id(j))
...       
140721468345304
140721468345304
140721468345048
>>> j=16
...       
>>> print(id(x)); print(id(y)); print(id(j))
...       
140721468345304
140721468345304
140721468345240
>>> del (j)
...       
>>> print(id(x)); print(id(y)); print(id(j))
...       
140721468345304
140721468345304
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print(id(x)); print(id(y)); print(id(j))
NameError: name 'j' is not defined
>>> print(j)
...       
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(j)
NameError: name 'j' is not defined
>>> j=16
...       
>>> print(id(x)); print(id(y)); print(id(j))
...       
140721468345304
140721468345304
140721468345240
