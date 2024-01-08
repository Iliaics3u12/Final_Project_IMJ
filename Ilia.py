import tkinter as tk
from math import pi, sqrt, cos, sin, tan, acos, asin, atan, factorial, radians, degrees, log10, log, exp
from cmath import sqrt as csqrt

def insert_text(text):
    """
    Inserts the given text into the entry field.

    :param text: The text to be inserted.
    :return: None
    """
    entry.insert(tk.END, text)

def calculate():
    """
    Evaluates the expression in the entry field.

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
    """
    Clears the entry field.

    :return: None
    """
    entry.delete(0, tk.END)

def square():
    """
    Squares the value in the entry field.

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
    """
    Inserts the power operator into the entry field.

    :return: None
    """
    entry.insert(tk.END, '**')

def square_root():
    """
    Calculates the square root of the value in the entry field.

    :return: None
    """
    try:
        value = float(entry.get())
        clear_entry()
        entry.insert(tk.END, str(sqrt(value)))
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")

def cosine_deg():
    """
    Calculates the cosine of the value in the entry field.

    :return: None
    """
    try:
        value = float(entry.get())
        clear_entry()
        entry.insert(tk.END, str(cos(radians(value))))
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")

def tangent_deg():
    """
    Calculates the tangent of the value in the entry field.

    :return: None
    """
    try:
        value = float(entry.get())
        clear_entry()
        entry.insert(tk.END, str(tan(radians(value))))
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")

def sine_deg():
    """
    Calculates the sine of the value in the entry field.

    :return: None
    """
    try:
        value = float(entry.get())
        clear_entry()
        entry.insert(tk.END, str(sin(radians(value))))
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")

def inverse_cosine_deg():
    """
    Calculates the inverse cosine of the value in the entry field.

    :return: None
    """
    try:
        value = float(entry.get())
        clear_entry()
        entry.insert(tk.END, str(degrees(acos(value))))
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")

def inverse_sine_deg():
    """
    Calculates the inverse sine of the value in the entry field.

    :return: None
    """
    try:
        value = float(entry.get())
        clear_entry()
        entry.insert(tk.END, str(degrees(asin(value))))
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")

def inverse_tangent_deg():
    """
    Calculates the inverse tangent of the value in the entry field.

    :return: None
    """
    try:
        value = float(entry.get())
        clear_entry()
        entry.insert(tk.END, str(degrees(atan(value))))
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")

def factorial_func():
    """
    Calculates the factorial of the value in the entry field.

    :return: None
    """
    try:
        value = int(entry.get())
        clear_entry()
        entry.insert(tk.END, str(factorial(value)))
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")

def quadratic_formula():
    """
    Displays or hides the input fields for the quadratic formula.

    :return: None
    """
    if a_label.winfo_viewable():
        a_label.grid_remove()
        a_entry.grid_remove()
        b_label.grid_remove()
        b_entry.grid_remove()
        c_label.grid_remove()
        c_entry.grid_remove()
    else:
        a_label.grid(row=10, column=0)
        a_entry.grid(row=10, column=1)
        b_label.grid(row=11, column=0)
        b_entry.grid(row=11, column=1)
        c_label.grid(row=12, column=0)
        c_entry.grid(row=12, column=1)

def calculate_quadratic_roots():
    """
    Calculates the roots of the quadratic equation using the quadratic formula.

    :return: None
    """
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        c = float(c_entry.get())
        root1 = (-b + csqrt(b**2 - 4*a*c)) / (2*a)
        root2 = (-b - csqrt(b**2 - 4*a*c)) / (2*a)
        entry.configure(width=50)  # Increase width for larger roots
        # Display roots as real numbers if they are real, otherwise display as complex numbers
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"{root1.real if root1.imag == 0 else root1}, {root2.real if root2.imag == 0 else root2}")
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Enter values for a, b, c")

root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, font=('arial', 20, 'bold'), borderwidth=3, relief="ridge", justify="right", bg="#2c3e50", fg="#ecf0f1")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

button_params = {
    'padx': 20,
    'pady': 20,
    'font': ('arial', 20, 'bold')
}

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
    ('x²', '√', 'x!', 'x^y'),
    ('cos', 'sin', 'tan', 'π'),
    ('acos', 'asin', 'atan', 'e'),
    ('log10', 'ln', 'exp', 'quadratic')
]

for i, row in enumerate(buttons, start=1):
    for j, button_label in enumerate(row):
        if button_label == 'π':
            action = lambda pi=pi: insert_text(str(pi))
        elif button_label == 'x²':
            action = square
        elif button_label == 'x^y':
            action = power
        elif button_label == '√':
            action = square_root
        elif button_label == '=':
            action = calculate
        elif button_label == 'cos':
            action = cosine_deg
        elif button_label == 'sin':
            action = sine_deg
        elif button_label == 'tan':
            action = tangent_deg
        elif button_label == 'acos':
            action = inverse_cosine_deg
        elif button_label == 'asin':
            action = inverse_sine_deg
        elif button_label == 'atan':
            action = inverse_tangent_deg
        elif button_label == 'x!':
            action = factorial_func
        elif button_label == 'quadratic':
            action = quadratic_formula
        elif button_label == 'e':
            action = lambda e=exp(1): insert_text(str(e))
        elif button_label == 'ln':
            action = lambda: entry.insert(tk.END, 'log(')
        elif button_label == 'log10':
            action = lambda: entry.insert(tk.END, 'log10(')
        elif button_label == 'exp':
            action = lambda: entry.insert(tk.END, 'exp(')
        else:
            action = lambda button_label=button_label: insert_text(button_label)

        button = tk.Button(root, text=button_label, **button_params, command=action)
        button.grid(row=i, column=j, sticky="nsew")

clear_button = tk.Button(root, text='Clear', **button_params, command=clear_entry)
clear_button.grid(row=9, column=0, columnspan=4, sticky="nsew")

# Quadratic formula inputs
a_label = tk.Label(root, text="a:")
a_entry = tk.Entry(root)
b_label = tk.Label(root, text="b:")
b_entry = tk.Entry(root)
c_label = tk.Label(root, text="c:")
c_entry = tk.Entry(root)

for i in range(10):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
