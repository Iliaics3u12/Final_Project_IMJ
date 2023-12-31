import tkinter as tk
from math import pi, sqrt, cos, sin, tan, acos, asin, atan, factorial, radians, degrees, log10, log, exp
from cmath import sqrt as csqrt
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

def cosine_deg():
    """
    Calculates the cosine of the value in the entry field (in degrees).

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
    Calculates the tangent of the value in the entry field (in degrees).

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
    Calculates the sine of the value in the entry field (in degrees).

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

def cube():
    """Calculate the cube of the input value and display the result."""
    try:
        value = float(entry.get())
        clear_entry()
        entry.insert(tk.END, str(value ** 3))
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")

def cube_root():
    """Calculate the cubic root of the input value and display the results."""
    try:
        value = float(entry.get())
        clear_entry()
        entry.insert(tk.END, str(value ** (1/3)))
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")

def logarithm_base_10():
    """Computes the base 10 logarithm of the input value and displays the result."""
    try:
        value = float(entry.get())
        clear_entry()
        entry.insert(tk.END, str(log10(value)))
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")

def euler_number():
    """Inserts the value of Euler's number (e) into the calculator."""
    entry.insert(tk.END, str(exp(1)))

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

def cubic_formula():
    """
    Toggles the visibility of entry widgets for coefficients in a cubic equation.

    If the entry widgets for coefficients (p, q, r, s) are currently visible, it hides them; otherwise, it shows them.
    """
    if p_label.winfo_viewable():
        p_label.grid_remove()
        p_entry.grid_remove()
        q_label.grid_remove()
        q_entry.grid_remove()
        r_label.grid_remove()
        r_entry.grid_remove()
        s_label.grid_remove()
        s_entry.grid_remove()
    else:
        p_label.grid(row=10, column=2)
        p_entry.grid(row=10, column=3)
        q_label.grid(row=11, column=2)
        q_entry.grid(row=11, column=3)
        r_label.grid(row=12, column=2)
        r_entry.grid(row=12, column=3)
        s_label.grid(row=13, column=2)
        s_entry.grid(row=13, column=3)

def cubic_formula():
    if p_label.winfo_viewable():
        p_label.grid_remove()
        p_entry.grid_remove()
        q_label.grid_remove()
        q_entry.grid_remove()
        r_label.grid_remove()
        r_entry.grid_remove()
        s_label.grid_remove()
        s_entry.grid_remove()
    else:
        p_label.grid(row=10, column=2)
        p_entry.grid(row=10, column=3)
        q_label.grid(row=11, column=2)
        q_entry.grid(row=11, column=3)
        r_label.grid(row=12, column=2)
        r_entry.grid(row=12, column=3)
        s_label.grid(row=13, column=2)
        s_entry.grid(row=13, column=3)

def calculate_cubic_roots():
    """
    Calculates the roots of a cubic equation and displays the result in the entry widget.

    Reads coefficients (p, q, r, s) from entry widgets, applies the cubic formula, and displays the roots in the entry widget.
    """
    try:
        p = float(p_entry.get())
        q = float(q_entry.get())
        r = float(r_entry.get())
        s = float(s_entry.get())
        # Cubic formula
        a = (3*q - p**2)/3
        b = (2*p**3 - 9*p*q + 27*r)/27
        offset = -p/3
        # Calculate the roots
        root1 = csqrt(b**2/4 + a**3/27)
        root2 = ((-b/2 + root1)**(1/3) if -b/2 + root1.real >= 0 else -((-b/2 + root1)**(1/3)))
        root3 = ((-b/2 - root1)**(1/3) if -b/2 - root1.real >= 0 else -((-b/2 - root1)**(1/3)))
        roots = [root2 + root3 + offset, -((root2 + root3)/2) + offset + csqrt(3)*(root2 - root3)*1j/2, -((root2 + root3)/2) + offset - csqrt(3)*(root2 - root3)*1j/2]
        entry.configure(width=50)
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"{roots[0].real if roots[0].imag == 0 else roots[0]}, {roots[1].real if roots[1].imag == 0 else roots[1]}, {roots[2].real if roots[2].imag == 0 else roots[2]}")
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Enter values for a, b, c, d")

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("800x1200")  # Increase the size of the calculator
# Create the entry widget for user input
entry = tk.Entry(root, font=('arial', 30, 'bold'), borderwidth=3, relief="ridge", justify="right", bg="#2c3e50", fg="#ecf0f1")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")
# Define button styling parameters
button_params = {
    'padx': 20,
    'pady': 20,
    'font': ('arial', 20, 'bold')
}
# Define the layout of the calculator buttons
buttons = [
    ('7', '8', '9', '/',),
    ('4', '5', '6', '*', ),
    ('1', '2', '3', '-', ),
    ('0', '.', 'pi', '+'),
    ('x²','x³', 'x^y', '='),
    ('√', '³√', 'log10','factorial', ),
    ('cos', 'sin', 'tan','quadratic'),
    ('acos', 'asin', 'atan','cubic' ),
    ('e')
]
# Create and place the buttons on the grid
for i, row in enumerate(buttons, start=1):
    # Define the action for each button
    for j, button_label in enumerate(row):
        if button_label == 'pi':
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
        elif button_label == 'factorial':
            action = factorial_func
        elif button_label == 'quadratic':
            action = quadratic_formula
        elif button_label == 'cubic':
            action = cubic_formula
        elif button_label == 'log10':
            action = logarithm_base_10
        elif button_label == 'e':
            action = euler_number
        elif button_label == 'x³':
            action = cube
        elif button_label == '³√':
            action = cube_root
        else:
            action = lambda button_label=button_label: insert_text(button_label)
        # Create and place the button on the grid
        button = tk.Button(root, text=button_label, **button_params, command=action)
        button.grid(row=i, column=j, sticky="nsew")
# Create and place the clear button
clear_button = tk.Button(root, text='Clear', **button_params, command=clear_entry)
clear_button.grid(row=9, column=1, columnspan=3, sticky="nsew")

# Quadratic formula inputs
a_label = tk.Label(root, text="a:", font=('arial', 20, 'bold'))
a_entry = tk.Entry(root, font=('arial', 20, 'bold'), width=5)
b_label = tk.Label(root, text="b:", font=('arial', 20, 'bold'))
b_entry = tk.Entry(root, font=('arial', 20, 'bold'), width=5)
c_label = tk.Label(root, text="c:", font=('arial', 20, 'bold'))
c_entry = tk.Entry(root, font=('arial', 20, 'bold'), width=5)

# Cubic formula inputs
p_label = tk.Label(root, text="a:", font=('arial', 20, 'bold'))
p_entry = tk.Entry(root, font=('arial', 20, 'bold'), width=5)
q_label = tk.Label(root, text="b:", font=('arial', 20, 'bold'))
q_entry = tk.Entry(root, font=('arial', 20, 'bold'), width=5)
r_label = tk.Label(root, text="c:", font=('arial', 20, 'bold'))
r_entry = tk.Entry(root, font=('arial', 20, 'bold'), width=5)
s_label = tk.Label(root, text="d:", font=('arial', 20, 'bold'))
s_entry = tk.Entry(root, font=('arial', 20, 'bold'), width=5)
# Configure row and column weights so they expand proportionally with the window size
for i in range(16):
    root.grid_rowconfigure(i, weight=1)
for j in range(5):
    root.grid_columnconfigure(j, weight=1)
# Start the main loop of the application
root.mainloop()
