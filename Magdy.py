import tkinter as tk
from math import pi, sqrt

def insert_text(text):
    # Inserts the given text at the end of the entry widget
    entry.insert(tk.END, text)

def calculate():
    """
    Evaluates the expression in the entry widget and displays the result.

    If the expression is invalid, it clears the entry and shows an error.

    :return: None
    """

    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        clear_entry()
        entry.insert(tk.END, "Error")

def clear_entry():
    # Clears the entry widget
    entry.delete(0, tk.END)

def square():
    """
    Calculates the square of the number in the entry widget and displays the result.

    If the input is not a number, it clears the entry and shows an error.
    :return: None
    """
    try:
        value = float(entry.get())
        clear_entry()
        entry.insert(tk.END, str(value ** 2))
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")

def power():
    # Inserts the power operator into the entry widget
    entry.insert(tk.END, '**')

def square_root():
    """
    Calculates the square root of the number in the entry widget and display the result.

    If the input is not a number, it clears the entry and shows an error.
    :return: None
    """

    try:
        value = float(entry.get())
        clear_entry()
        entry.insert(tk.END, str(sqrt(value)))
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")

# Create the entry widget for user input
entry = tk.Entry(root, font=('arial', 20, 'bold'), borderwidth=3, relief="ridge", justify="right", bg="#2c3e50", fg="#ecf0f1")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Define button styling parameters
button_params = {
    'padx': 20,
    'pady': 20,
    'font': ('arial', 20, 'bold')
}

# Define the layout of the calculator buttons
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', 'pi', '+'),
    ('x^2', 'x^y', 'sqrt', '='),
]

# Create and place the buttons on the grid
for i, row in enumerate(buttons, start=1):
    for j, button_label in enumerate(row):
        # Define the action for each button
        if button_label == 'pi':
            action = lambda pi=pi: insert_text(str(pi))
        elif button_label == 'x^2':
            action = square
        elif button_label == 'x^y':
            action = power
        elif button_label == 'sqrt':
            action = square_root
        elif button_label == '=':
            action = calculate
        else:
            action = lambda button_label=button_label: insert_text(button_label)

        # Create and place the button on the grid
        button = tk.Button(root, text=button_label, **button_params, command=action)
        button.grid(row=i, column=j, sticky="nsew")

# Create and place the clear button
clear_button = tk.Button(root, text='Clear', **button_params, command=clear_entry)
clear_button.grid(row=6, column=0, columnspan=4, sticky="nsew")

# Configure row and column weights so they expand proportionally with the window size
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Start the main loop of the application
root.mainloop()
