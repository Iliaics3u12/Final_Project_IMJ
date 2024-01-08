import tkinter as tk
from math import log10, sqrt, exp

def clear_entry():
    entry.delete(0, tk.END)

def insert_text(text):
    entry.insert(tk.END, text)

def cube():
    try:
        value = float(entry.get())
        clear_entry()
        entry.insert(tk.END, str(value ** 3))
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")

def cube_root():
    try:
        value = float(entry.get())
        clear_entry()
        entry.insert(tk.END, str(value ** (1/3)))
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")

def logarithm_base_x():
    entry.insert(tk.END, 'logx(')

def logarithm_base_10():
    try:
        value = float(entry.get())
        clear_entry()
        entry.insert(tk.END, str(log10(value)))
    except ValueError:
        clear_entry()
        entry.insert(tk.END, "Error")

def euler_number():
    entry.insert(tk.END, str(exp(1)))

def calculate():
    try:
        result = eval(entry.get())
        clear_entry()
        entry.insert(tk.END, str(result))
    except Exception as e:
        clear_entry()
        entry.insert(tk.END, f"Error")

def delete_previous():
    current_text = entry.get()
    if current_text:
        entry.delete(len(current_text) - 1, tk.END)

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("1080x720")

entry = tk.Entry(root, font=('arial', 30, 'bold'), borderwidth=3, relief="ridge", justify="right", bg="#2c3e50", fg="#ecf0f1")
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
    ('0', '.', '+', '='),
    ('x²','log10', '√', 'Del'),
]

for i, row in enumerate(buttons, start=1):
    for j, button_label in enumerate(row):
        if button_label == 'logx':
            action = logarithm_base_x
        elif button_label == 'log10':
            action = logarithm_base_10
        elif button_label == 'Del':
            action = delete_previous
        elif button_label == '=':
            action = calculate
        elif button_label == 'e':
            action = euler_number
        elif button_label == 'x³':
            action = cube
        elif button_label == '³√':
            action = cube_root
        else:
            action = lambda button_label=button_label: insert_text(button_label)

        button = tk.Button(root, text=button_label, **button_params, command=action)
        button.grid(row=i, column=j, sticky="nsew")

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
