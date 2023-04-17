from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror

# Function to perform addition operation
def add():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 + num2
        lbl_result.config(text="Result: " + str(result))
    except ValueError:
        showerror("Error", "Invalid input")

# Function to perform subtraction operation
def subtract():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 - num2
        lbl_result.config(text="Result: " + str(result))
    except ValueError:
        showerror("Error", "Invalid input")

# Function to perform multiplication operation
def multiply():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 * num2
        lbl_result.config(text="Result: " + str(result))
    except ValueError:
        showerror("Error", "Invalid input")

# Function to perform division operation
def divide():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            showerror("Error", "Cannot divide by zero")
        else:
            result = num1 / num2
            lbl_result.config(text="Result: " + str(result))
    except ValueError:
        showerror("Error", "Invalid input")

# Function to perform modulo operation
def modulo():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            showerror("Error", "Cannot divide by zero")
        else:
            result = num1 % num2
            lbl_result.config(text="Result: " + str(result))
    except ValueError:
        showerror("Error", "Invalid input")

# Create the main window
root = Tk()
root.title("Basic Calculator")

# Apply a simple style using ttk
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 14), padding=10)
style.configure("TLabel", font=("Helvetica", 14), padding=10)
style.configure("TEntry", font=("Helvetica", 14), padding=10)

# Create input labels and entry boxes
lbl_num1 = ttk.Label(root, text="Number 1:")
lbl_num1.grid(row=0, column=0)
entry_num1 = ttk.Entry(root)
entry_num1.grid(row=0, column=1)

lbl_num2 = ttk.Label(root, text="Number 2:")
lbl_num2.grid(row=1, column=0)
entry_num2 = ttk.Entry(root)
entry_num2.grid(row=1, column=1)

# Create buttons for each operation
btn_add = ttk.Button(root, text="Add", command=add)
btn_add.grid(row=2, column=0, columnspan=2, sticky="we")

btn_subtract = ttk.Button(root, text="Subtract", command=subtract)
btn_subtract.grid(row=3, column=0, columnspan=2, sticky="we")

btn_multiply = ttk.Button(root, text="Multiply", command=multiply)
btn_multiply.grid(row=4, column=0, columnspan=2, sticky="we")

btn_divide = ttk.Button(root, text="Divide", command=divide)
btn_divide.grid(row=5, column=0,columnspan=2, sticky="we")

btn_modulo = ttk.Button(root, text="Modulo", command=modulo)
btn_modulo.grid(row=6, column=0, columnspan=2, sticky="we")

lbl_result = ttk.Label(root, text="")
lbl_result.grid(row=7, column=0, columnspan=2, sticky="we")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_rowconfigure(7, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)


root.mainloop()


