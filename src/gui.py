import tkinter as tk
import math_library as m

# Create the window
window = tk.Tk()
window.title("Calculator")

# Create the display
display = tk.Entry(window, width=25, borderwidth=5, font=("Helvetica", 20))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

calculation = []
total_calculation = []

# Define button click function
def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(number))

def button_clear():
    global calculation
    calculation.clear()
    display.delete(0, tk.END)

def button_add():
    number = display.get()
    calculation.append(float(number))
    calculation.append('+')
    display.delete(0, tk.END)

def button_subtract():
    number = display.get()
    calculation.append(float(number))
    calculation.append('-')
    display.delete(0, tk.END)

def button_multiply():
    number = display.get()
    calculation.append(float(number))
    calculation.append('*')
    display.delete(0, tk.END)

def button_divide():
    number = display.get()
    calculation.append(float(number))
    calculation.append('/')
    display.delete(0, tk.END)

def button_power():
    number = display.get()
    calculation.append(float(number))
    calculation.append('^')
    display.delete(0, tk.END)

def button_root():
    number = display.get()
    calculation.append(float(number))
    calculation.append('√')
    display.delete(0, tk.END)

def button_equal():
    global total_calculation
    global calculation
    number = display.get()
    calculation.append(float(number))
    result = calculation[0]
    for i in range(1, len(calculation), 2):
        operator = calculation[i]
        operand = calculation[i+1]
        if operator == '+':
            result = m.add(result, operand)
        elif operator == '-':
            result = m.sub(result,operand)
        elif operator == '*':
            result = m.multiple(result, operand)
        elif operator == '/':
            result = m.divide(result, operand)
        elif operator == '^':
            result = m.exponentiate(result, int(operand))
        elif operator == '√':
            result = m.sqrt(result, operand)
    
    display.delete(0, tk.END)
    display.insert(0, result)
    total_calculation.extend(calculation)
    calculation.clear()

def button_dot():
    current = display.get()
    if '.' not in current:
        display.delete(0, tk.END)
        display.insert(0, str(current) + ".")

# Create the buttons
button_1 = tk.Button(window, text="1", padx=40, pady=20,font=("Helvetica", 16), command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=40, pady=20, font=("Helvetica", 16), command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=40, pady=20, font=("Helvetica", 16), command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=40, pady=20,font=("Helvetica", 16),  command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=40, pady=20,font=("Helvetica", 16),  command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=40, pady=20, font=("Helvetica", 16), command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=40, pady=20,font=("Helvetica", 16),  command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=40, pady=20,font=("Helvetica", 16),  command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=40, pady=20,font=("Helvetica", 16),  command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=40, pady=20,font=("Helvetica", 16),  command=lambda: button_click(0))
button_add = tk.Button(window, text="+", padx=39, pady=20,font=("Helvetica", 16),  command=button_add)
button_equal = tk.Button(window, text="=", padx=91, pady=20,font=("Helvetica", 16),  command=button_equal)
button_clear = tk.Button(window, text="Clear", padx=79, pady=20,font=("Helvetica", 16),  command=button_clear)
button_subtract = tk.Button(window, text="-", padx=41, pady=20,font=("Helvetica", 16),  command=button_subtract)
button_multiply = tk.Button(window, text="*", padx=40, pady=20, font=("Helvetica", 16), command=button_multiply)
button_divide = tk.Button(window, text="/", padx=41, pady=20,font=("Helvetica", 16),  command=button_divide)
button_power = tk.Button(window, text="^", padx=41, pady=20,font=("Helvetica", 16),  command=button_power)
button_root = tk.Button(window, text="√", padx=41, pady=20, font=("Helvetica", 16), command=button_root)
button_dot = tk.Button(window, text=".", padx=37, pady=20, font=("Helvetica", 16), command=button_dot)

# Put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_power.grid(row=7, column=0)
button_root.grid(row=7, column=1)
button_dot.grid(row=7, column=2)
# Run the program
window.mainloop()