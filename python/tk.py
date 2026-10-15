"""1. What is Tkinter?
Tkinter is Python's standard library for creating Graphical User Interface (GUI) applications.
A GUI allows users to interact with a program through windows, buttons,
text boxes, labels and menus instead of typing every command in a terminal.
How does Tkinter work?

Python program
Defines the window and widgets

Tkinter creates the GUI
Window, labels, buttons and input fields

User interacts
Clicks a button or enters data

Python executes the required action
Calculates and displays the result
"""


"""
Demo 1: Create your first Tkinter window
Open Python IDLE, create a new file, and enter this code.
"""


import tkinter as tk

# Create the main window
root = tk.Tk()

# Set window properties
root.title("My First GUI")
root.geometry("400x250")

# Display a message
label = tk.Label(root, text="Welcome to Tkinter!")
label.pack()

# Keep the window running
root.mainloop()

"""
Line 1: Import Tkinter
import tkinter as tk


What does it do?
It imports the tkinter module, which provides the tools required to create GUI applications.
- import is a Python keyword used to load a module.
- tkinter is the module name.
- as tk creates a short alias for tkinter.



Line 3: Create the main window
root = tk.Tk()


This is one of the most important lines in the program.
Let's break it down:
Part	Meaning
root	Variable that refers to the main window object
=	Assignment operator
tk	Alias for the Tkinter module
Tk	Class used to create the main window
()	Calls the class to create an object
What happens internally?
1. Python calls tk.Tk().
2. Tkinter creates the main application window and initializes the GUI system.
3. The resulting window object is assigned to root.
We can use root later to set the window's title, size, background, and other properties.
Real-life analogy: Think of root as the empty frame of a house. We will add labels, buttons, and other widgets inside it.



Line 4: Set the window title
root.title("My First GUI")


This sets the title displayed in the window's title bar.
- root refers to the main window.
- title() is a method of the window object.
- "My First GUI" is the string passed as an argument.

You can change the title to:
root.title("Student Management System")

The title bar will display Student Management System.


Line 5: Set the window size
root.geometry("400x250")



This specifies the initial window dimensions.
- geometry() is a method used to set the window's geometry.
- "400x250" is a string representing width and height.
- 400 means 400 pixels wide.
- 250 means 250 pixels high.

The format is:
root.geometry("widthxheight")

For example:
root.geometry("800x600")

This creates a window with an initial size of 800 × 600 pixels.


Line 7: Create a Label widget
label = tk.Label(root, text="Welcome to Tkinter!")



This creates a label widget that displays text.
Let's examine each part:
Part	Meaning
label	Variable that refers to the label widget
tk.Label	Tkinter class used to create a label
root	Parent container in which the label will appear
text=	Option specifying the text to display
"Welcome to Tkinter!"	The message displayed on the label
A widget is a graphical component of a GUI, such as a label, button, entry box, or checkbox.


A widget is a graphical component of a GUI, such as a label, button, entry box, or checkbox.
The first argument, root, tells Tkinter which window should contain the label.
The text option specifies what the label should display.
For example:
label = tk.Label(root, text="Welcome, Students!")


This creates a label with the message Welcome, Students!.

Important: Creating a widget does not automatically determine where it will appear.
We need a geometry manager such as pack(), grid(), or place() to arrange it in the window.


Line 8: Display the label using pack()
label.pack()



The pack() method is a geometry manager in Tkinter.
It arranges a widget inside its parent container.
In this program:
1. The label object has already been created.
2. pack() tells Tkinter to arrange the label inside root.
3. With the default settings, the label appears near the top, centered horizontally.

Other geometry managers include:
- pack() — arranges widgets in relation to available space.
- grid() — arranges widgets in rows and columns.
- place() — positions widgets using specified coordinates or relative positions.
For example:
label.pack(pady=20)


This adds 20 pixels of vertical padding around the label.

Remember: tk.Label() creates the widget, while label.pack() arranges
it in the window.


Line 9: Keep the window running
root.mainloop()


This is the main event loop of the Tkinter application.
When Python reaches this line, Tkinter starts processing GUI events and keeps the window responsive.
The event loop handles events such as:
- Mouse clicks
- Keyboard input
- Window resizing
- Button presses
- Requests to close the window
Without mainloop(), the program would generally finish without keeping the GUI open and responsive.


For example, when a user clicks the window's close button, Tkinter processes that event and closes the window.
Real-life analogy: Imagine a receptionist continuously waiting for visitors.
The receptionist responds whenever someone arrives. Similarly, mainloop() waits for and processes GUI events.



"""

# try new prog with some changes

import tkinter as tk

root = tk.Tk()
root.title("M.Sc. Computer Applications")
root.geometry("500x300")

label = tk.Label(
    root,
    text="Welcome to Python GUI Programming!",
    font=("Arial", 14)
)

label.pack(pady=30)

root.mainloop()



"""
Demo 2: Add a button and handle a click
Now let's make the application respond to the user.

"""


import tkinter as tk

root = tk.Tk()
root.title("Button Demo")
root.geometry("350x200")

def say_hello():
    label.config(text="Hello! Button clicked.")

label = tk.Label(root, text="Click the button below")
label.pack(pady=20)

button = tk.Button(
    root,
    text="Click Me",
    command=say_hello
)
button.pack()

root.mainloop()



"""
Line 6:
label.config(text="Hello! Button clicked.")


This changes the label's displayed text.

Let's break it down:

Part	   Explanation
label	   Variable referring to the label widget
.	   Accesses a method or attribute of an object
config()   Modifies the widget's configuration
text=	   Specifies which property to change
"Hello! Button clicked."	The new label text
For example, if the label currently displays Click the button below, this statement changes it to Hello! Button clicked.
Important: The function refers to label, which is created later in the program.
This works because the function is called only after the label has been created, when the user clicks the button.


Lines 9–13: Create the button
button = tk.Button(    root,    text="Click Me",    command=say_hello)

This creates a button widget.
Argument	   Purpose
root	           Places the button inside the main window
text="Click Me"	   Sets the text shown on the button
command=say_hello  Registers the function to run when the button is clicked

Notice that we write say_hello, not say_hello().
- say_hello passes the function itself as a callback.
- say_hello() calls the function immediately.


Difference between command=say_hello and command=say_hello()
This is a common point of confusion for beginners.
Code	What happens?
command=say_hello	Registers the function to run when clicked.
command=say_hello()	Calls the function immediately during button creation and assigns its return value to command.


You can change its position using options:
Code	                        Placement
button.pack()	                Top, centered by default
button.pack(side="left")	Left side of the available area
button.pack(side="right")	Right side of the available area
button.pack(side="bottom")	Bottom of the available area

Important: pack() does not assign fixed coordinates such as (100, 50).
It arranges widgets relative to the available space and the other widgets managed by pack().


If you want to position a button at an exact location, you can use place(), for example:
button.place(x=100, y=100)

Here, x=100 and y=100 specify its position relative to the parent window.

"""
