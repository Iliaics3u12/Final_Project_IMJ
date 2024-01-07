import tkinter as tk
from math import pi, sqrt, cos, sin, tan, acos, asin, atan, factorial # Functions that I wrote there.
from cmath import sqrt as csqrt

def insert_text(text):
    entry.insert(tk.END, text)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        clear_entry()
        entry.insert(tk.END, "Error")

def clear_entry():
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
    entry.insert(tk.END, '**')

def square_root():
    try:
        value = float(entry.get())
        clear_entry()
        entry.insert(tk.END, str(sqrt(value)))
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")
def cosine():
    try:
        value = float(entry.get())
        clear_entry()
        entry.insert(tk.END, str(cos(value)))
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")

def sine():
    try:
        value = float(entry.get())
        clear_entry()
        entry.insert(tk.END, str(sin(value)))
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")

def tangent():
    try:
        value = float(entry.get())
        clear_entry()
        entry.insert(tk.END, str(tan(value)))
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")

def inverse_cosine():
    try:
        value = float(entry.get())
        clear_entry()
        entry.insert(tk.END, str(acos(value)))
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")

def inverse_sine():
    try:
        value = float(entry.get())
        clear_entry()
        entry.insert(tk.END, str(asin(value)))
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")

def inverse_tangent():
    try:
        value = float(entry.get())
        clear_entry()
        entry.insert(tk.END, str(atan(value)))
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")

def factorial_func():
    try:
        value = int(entry.get())
        clear_entry()
        entry.insert(tk.END, str(factorial(value)))
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")

def quadratic_formula():
    try:
        a, b, c = map(float, entry.get().split())
        clear_entry()
        root1 = (-b + csqrt(b**2 - 4*a*c)) / (2*a)
        root2 = (-b - csqrt(b**2 - 4*a*c)) / (2*a)
        entry.insert(tk.END, f"Roots: {root1}, {root2}")
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")

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

    ('cos', 'sin', 'tan', 'factorial'),
    ('acos', 'asin', 'atan', 'quadratic'),
]

for i, row in enumerate(buttons, start=1):
    for j, button_label in enumerate(row):
        if button_label == 'cos':
            action = cosine
        elif button_label == 'sin':
            action = sine
        elif button_label == 'tan':
            action = tangent
        elif button_label == 'acos':
            action = inverse_cosine
        elif button_label == 'asin':
            action = inverse_sine
        elif button_label == 'atan':
            action = inverse_tangent
        elif button_label == 'factorial':
            action = factorial_func
        elif button_label == 'quadratic':
            action = quadratic_formula
        else:
            action = lambda button_label=button_label: insert_text(button_label)

        button = tk.Button(root, text=button_label, **button_params, command=action)
        button.grid(row=i, column=j, sticky="nsew")

clear_button = tk.Button(root, text='Clear', **button_params, command=clear_entry)
clear_button.grid(row=6, column=0, columnspan=4, sticky="nsew")

for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
