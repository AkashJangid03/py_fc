
import tkinter as tk
from tkinter import messagebox
"""
 What is tkinter?
tkinter is Python's standard library for creating Graphical User Interface (GUI) applications.
Examples of GUI components include:
- Windows
- Buttons
- Labels
- Text input fields
- Popup messages
Step 2: What is messagebox?
messagebox is a module inside tkinter that provides predefined popup dialog boxes.
For example, in our calculator, if the user tries to divide by zero, we can display an error popup.

Important messagebox methods
Method	Purpose	Example
showerror()	Displays an error	Invalid number
showwarning()	Displays a warning	Missing information
showinfo()	Displays information	Calculation completed
askyesno()	Asks a Yes/No question	Do you want to exit?
"""
def calculate(operator):

    try:
        # Entry.get() returns the entered value as a STRING.
        # float() converts that string into a number.
        # Example: "12.5" becomes 12.5.
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        # -------------------------------------------------
        # CONCEPT 3: CONDITIONAL STATEMENTS
        # The operator determines which calculation runs.
        # -------------------------------------------------
        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":
            # Division by zero must be handled separately.
            # Otherwise, Python raises ZeroDivisionError.
            if num2 == 0:
                messagebox.showerror(
                    "Calculation Error",
                    "Cannot divide by zero!"
                )
                return  # Stop this function immediately.

            result = num1 / num2

        # Update the existing result label.
        # config() changes a widget's properties.
        result_label.config(text=f"Result: {result}")

#result_label.config(text=f"Result: {result}")
#The f before the opening quotation mark enables Python to evaluate expressions inside curly braces {}.

   
    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Please enter valid numbers in both fields."
        )


# =========================================================
# CONCEPT 4: CREATING THE MAIN WINDOW
# Tk() creates the main application window.
# root is the variable referring to that window.
# =========================================================
root = tk.Tk()

# title() sets the text displayed in the title bar.
root.title("Simple Calculator")

# geometry() sets the initial width and height in pixels.
root.geometry("380x320")

# resizable(False, False) prevents resizing horizontally
# and vertically. This is optional.
root.resizable(False, False)


# =========================================================
# CONCEPT 5: LABEL WIDGET
# A Label displays text or an image.
#
# root is the parent widget: this label belongs to root.
# text specifies what the label displays.
# =========================================================
heading = tk.Label(
    root,
    text="SIMPLE CALCULATOR",
    font=("Arial", 16, "bold")
)

# pack() places the widget in the available window space.
# pady adds vertical padding around the widget.
heading.pack(pady=15)


# =========================================================
# CONCEPT 6: ENTRY WIDGET
# Entry creates a single-line input field.
#
# Users type the numbers into these fields.
# We retain each Entry object in a variable so that
# we can retrieve its input later using get().
# =========================================================
tk.Label(root, text="First Number:").pack()

entry1 = tk.Entry(root, width=25)
entry1.pack(pady=5)
"""
This statement creates a single-line text input field in the main application window. The user can type the first number into this field.
1. Understand each part
Code	Explanation
entry1	A variable that stores a reference to the Entry widget.
=	Assigns the created widget to the variable.
tk.Entry()	Creates a single-line text input field.
root	The parent window in which the input field will appear.
width=25	Sets the approximate width of the input field to 25 characters, depending on the font.
"""
tk.Label(root, text="Second Number:").pack()

entry2 = tk.Entry(root, width=25)
entry2.pack(pady=5)


# =========================================================
#  BUTTON WIDGET AND EVENT HANDLING
# Button creates a clickable control.
#
# command connects a button click to a callback function.
# lambda lets us pass an argument to calculate().
#
# command=lambda: calculate("+")
# means: call calculate("+") when clicked.
#
# Do not write command=calculate("+") here, because that
# would execute the function immediately during setup.
# =========================================================
button_frame = tk.Frame(root)
"""
This statement creates a Frame widget inside the main window. We use it as a container to group related widgets,
such as the Addition, Subtraction, Multiplication, and Division buttons.
Why do we need a Frame?
Imagine we want to arrange four calculator buttons in two rows and two columns.
Without a Frame, you can still arrange buttons directly in the main window.
A Frame simply makes it easier to organize widgets into groups.
Let's understand the execution:
1. tk.Frame(root) creates the container.
2. button_frame.pack(pady=10) places the container in the main window with vertical padding.
3. tk.Button(button_frame, ...) creates a button inside the Frame, rather than directly inside root.
4. .grid(row=0, column=0) places that button in the first row and first column of the Frame.
"""
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Addition (+)",
    width=12,
    command=lambda: calculate("+")
).grid(row=0, column=0, padx=5, pady=5)

"""
The grid() method places a widget in a specific row and column inside its parent container.
Here, it places the button in the first row and second column, with spacing around it.
Parameter	Meaning
grid()	Arranges widgets in a table-like structure of rows and columns.
row=0	Places the widget in the first row.
column=1	Places the widget in the second column.
padx=5	Adds 5 pixels of horizontal spacing around the widget.
pady=5	Adds 5 pixels of vertical spacing around the widget.
Remember: Row and column numbering starts from 0, not 1.
"""

tk.Button(
    button_frame,
    text="Subtraction (-)",
    width=12,
    command=lambda: calculate("-")
).grid(row=0, column=1, padx=5, pady=5)

tk.Button(
    button_frame,
    text="Multiplication (*)",
    width=12,
    command=lambda: calculate("*")
).grid(row=1, column=0, padx=5, pady=5)

tk.Button(
    button_frame,
    text="Division (/)",
    width=12,
    command=lambda: calculate("/")
).grid(row=1, column=1, padx=5, pady=5)


# =========================================================
# RESULT DISPLAY
# This label initially displays "Result: ".
# After a calculation, config() changes its text.
# =========================================================
result_label = tk.Label(
    root,
    text="Result: ",
    font=("Arial", 12, "bold")
)
result_label.pack(pady=5)



root.mainloop()
