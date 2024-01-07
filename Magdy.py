import tkinter as tk
from math import pi, sqrt

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
    ('0', '.', 'pi', '+'),
    ('x^2', 'x^y', 'sqrt', '='),
]

for i, row in enumerate(buttons, start=1):
    for j, button_label in enumerate(row):
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

        button = tk.Button(root, text=button_label, **button_params, command=action)
        button.grid(row=i, column=j, sticky="nsew")

clear_button = tk.Button(root, text='Clear', **button_params, command=clear_entry)
clear_button.grid(row=6, column=0, columnspan=4, sticky="nsew")

# Configure row and column weights so they expand proportionally
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
