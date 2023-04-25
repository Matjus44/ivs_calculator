##
# @file calc.py
# @brief graphical user interface
#
# @author Matúš Janek (xjanek05)
# @author Richard Húska (xhuska03)
#
#
import tkinter as tk
import math_library as m
bg_color = "#f5f5f5"
button_bg_color = "#e1e1e1"
button_fg_color = "#333"
label_bg_color = "#fff"
label_fg_color = "#333"
# Create the window
window = tk.Tk()
window.title("Calculator")
window.configure(bg="#FFFFFF")
window.geometry("316x618")
window.resizable(0, 0)

# Create the display

display = tk.Label(window, width=18, bg="#202222", fg="#FFFFFF", font=("Helvetica Neue", 22), padx=0, pady=10)
display.grid(row=1, column=0, columnspan=4)

total_expression = tk.Label(window,width=18, bg="#202222", fg="#FFFFFF", font=("Helvetica Neue", 22), padx=0, pady=10)
total_expression.grid(row=0, column=0, columnspan=4)


calculation = []
total_calculation = []

## Append the given number to the display and the total expression
# @brief Adds the given number to the current display and the total expression
# @param number The number to be added to the display
#
def button_click(number):
    current = display["text"]
    display["text"] = str(current) + str(number)

        
    total_expression["text"] = total_expression["text"] + str(number)
## 
# @brief Clears the current calculation and the display
#
def button_clear():
    global calculation
    calculation.clear()
    display["text"] = ""
    total_expression["text"] = ""
##
# @brief Adds the current number to the calculation list and "+" to the total expression
#
def button_add():
    number = display["text"]
    calculation.append(float(number))
    calculation.append('+')
    total_expression["text"] += "+"
   
    display["text"] = ""
##
# @brief Adds the current number to the calculation list and "-" to the total expression
#
def button_subtract():
    number = display["text"]
    calculation.append(float(number))
    calculation.append('-')
    total_expression["text"] += "-"
    display["text"] = ""
##
# @brief Adds the current number to the calculation list and "*" to the total expression
#
def button_multiply():
    number = display["text"]
    calculation.append(float(number))
    calculation.append('*')
    total_expression["text"] += "*"
    display["text"] = ""
##
# @brief Appends the number on the display to the calculation list, followed by the division operator. 
#           Updates the total expression label with the division symbol, clears the display.
#
def button_divide():
    number = display["text"]
    calculation.append(float(number))
    calculation.append('/')
    total_expression["text"] += "/"
    display["text"] = ""
##
# @brief Appends the number on the display to the calculation list, followed by the power operator. 
#           Updates the total expression label with the power symbol, clears the display.
#
def button_power():
    number = display["text"]
    calculation.append(float(number))
    calculation.append('^')
    total_expression["text"] += "^"
    display["text"] = ""
##    
# @brief Appends the number on the display to the calculation list, followed by the square root operator. 
#           Updates the total expression label with the square root symbol, clears the display.
#
def button_root():
    number = display["text"]
    calculation.append(float(number))
    calculation.append('√')
    total_expression["text"] += "√"
    display["text"] = ""
##
# @brief Appends the number on the display to the calculation list, followed by the factorial operator. Updates the total expression label with the factorial symbol, sets the display to '0'.
#
#
def button_factorial():
    number = display["text"]
   
    calculation.append(int(number))
    calculation.append('!')
    total_expression["text"] += "!"
    display["text"] = "0"
##
# @brief Gets the number on the display and appends it to the calculation list.
#           If the last operator in the calculation list is factorial, appends 0 to the calculation list.
#           Evaluates the calculation by processing the operators and operands in the calculation list
#           using the math_library module. Updates the display with the result and clears the calculation list.
#


def button_equal():
    global total_calculation
    global calculation
    number = display["text"]
    
    if(calculation[-1] == '!'):
        
       calculation.append(0)
    else:
        calculation.append(float(number))
    
    # create two stacks to keep track of operators and operands
    operators = []
    operands = []
    help = 0
    
    # iterate over the calculation list and push operators and operands onto the stacks
    for i in range(len(calculation)):
        if calculation[i] in ['+', '-', '*', '/', '^', '√','!', 'log']:
            
            operators.append(calculation[i])
        else:
            operands.append(float(calculation[i]))
    
    # perform exponentiation and square root operations first
    while '^' in operators or '√' in operators or '!' in operators or 'log' in operators:
        for i in range(len(operators)):
            if operators[i] == '^':
                operands[i] = m.exponentiate(operands[i], int(operands[i+1]))
                del operators[i]
                del operands[i+1]
                break
            elif operators[i] == '√':
                operands[i] = m.sqrt(operands[i], int(operands[i+1]))
                del operators[i]
                del operands[i+1]
                break
            elif operators[i] == '!':
                operands[i] = m.factorial(int(operands[i]))
                del operators[i]
                del operands[i+1]
                break
            elif operators[i] == 'log':
                operands[i] = m.logarithm(operands[i], int(operands[i+1]))
                del operators[i]
                del operands[i+1]
                break


    ##
    # @brief perform multiplication and division operations next
    #
    while '*' in operators or '/' in operators:
        for i in range(len(operators)):
            if operators[i] == '*':
                operands[i] = m.multiple(operands[i], operands[i+1])
                del operators[i]
                del operands[i+1]
                break
            elif operators[i] == '/':
                operands[i] = m.divide(operands[i], operands[i+1])
                del operators[i]
                del operands[i+1]
                break
    
    # perform addition and subtraction operations last
    result = operands[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result = m.add(result, operands[i+1])
        elif operators[i] == '-':
            result = m.sub(result, operands[i+1])
    
    display["text"] = str(result)
    total_expression["text"] = str(result)
    total_calculation.extend(calculation)
    calculation.clear()
##
# @brief Adds a decimal point to the current number on the calculator display.
# If the current number does not already contain a decimal point, this function
# adds one to the end of the current number and updates the total expression to
# reflect the change. If the current number already contains a decimal point,
# this function does nothing.
#
def button_dot():
    current = display["text"]
    if '.' not in current:
        display["text"] = str(current) + "."
        total_expression["text"] += "."
##
# @brief Appends the number on the display to the calculation list, followed by the log operator. Updates the total expression label with the factorial symbol, sets the display to '0'.
#
#
def button_log():
    number = display["text"]
    calculation.append(int(number))
    calculation.append('log')
    total_expression["text"] += "log"
    display["text"] = ""
##
# @brief After clicking at help button shows window with help and instructions
#
def show_help():
    help_window = tk.Toplevel()
    help_window.title("Help")
    help_window.geometry("400x400")
    help_window.resizable(False, False)
    help_text = tk.Label(help_window, text="Usage of calculator.\nCalculator is capable of performing basic math operations.Top label signals tottal expression you have entered and bottom just the answer, top label resets after you press equal button.\nYou can control the numbers and operations with the mouse or the keyboard.\n Calculator supports math logic such (multiply etc.) are performed as first.\n Usage of root: 1. number of which you want to take root,press root, 2. number is index of the root(2 number is natural number!)\n Usage of logarithm: 1. number is the base of the logarithm,press log, 2. number is of which you want to take the logarithm(base is natural number!)\n Usage of factorial: 1. number of which you want to take factorial, then press factorial.(Number must be whole real number!), if any ERROR message appears, just press CE(CLEAR) and continue with correct operations.", wraplength=300, justify="left")

    help_text.pack()
# Create the buttons
button_1 = tk.Button(window, text="1",width=6, height=3, font=("Helvetica", 16), bg="#e6e6e6", activebackground="#cccccc", command=lambda: button_click(1),padx=0, pady=0)
button_2 = tk.Button(window, text="2", width=6, height=3, font=("Helvetica", 16), bg="#e6e6e6", activebackground="#cccccc", command=lambda: button_click(2),padx=0, pady=0)
button_3 = tk.Button(window, text="3",width=6, height=3,font=("Helvetica", 16), bg="#e6e6e6", activebackground="#cccccc", command=lambda: button_click(3),padx=0, pady=0)
button_4 = tk.Button(window, text="4", width=6, height=3, font=("Helvetica", 16), bg="#e6e6e6", activebackground="#cccccc", command=lambda: button_click(4),padx=0, pady=0)
button_5 = tk.Button(window, text="5", width=6, height=3, font=("Helvetica", 16), bg="#e6e6e6", activebackground="#cccccc", command=lambda: button_click(5),padx=0, pady=0)
button_6 = tk.Button(window, text="6", width=6, height=3, font=("Helvetica", 16), bg="#e6e6e6", activebackground="#cccccc", command=lambda: button_click(6),padx=0, pady=0)
button_7 = tk.Button(window, text="7", width=6, height=3, font=("Helvetica", 16), bg="#e6e6e6", activebackground="#cccccc", command=lambda: button_click(7),padx=0, pady=0)
button_8 = tk.Button(window, text="8", width=6, height=3, font=("Helvetica", 16), bg="#e6e6e6", activebackground="#cccccc", command=lambda: button_click(8),padx=0, pady=0)
button_9 = tk.Button(window, text="9", width=6, height=3, font=("Helvetica", 16), bg="#e6e6e6", activebackground="#cccccc", command=lambda: button_click(9),padx=0, pady=0)
button_0 = tk.Button(window, text="0", width=6, height=3, font=("Helvetica", 16), bg="#e6e6e6", activebackground="#cccccc", command=lambda: button_click(0),padx=0, pady=0)
button_add = tk.Button(window, text="+", width=6, height=3, font=("Helvetica", 16), bg="#ff9933", activebackground="#ffcc66", command=button_add,padx=0, pady=0)
button_equal = tk.Button(window, text="=", width=6, height=3, font=("Helvetica", 16), bg="#4d4d4d", activebackground="#ffcc66", command=button_equal,padx=0, pady=0)
button_clear = tk.Button(window, text="CE", width=6, height=3, font=("Helvetica", 16), bg="#4d4d4d",  activebackground="#666666", command=button_clear,padx=0, pady=0)
button_subtract = tk.Button(window, text="-", width=6, height=3, font=("Helvetica", 16), bg="#ff9933", activebackground="#ffcc66", command=button_subtract,padx=0, pady=0)
button_multiply = tk.Button(window, text="*", width=6, height=3, font=("Helvetica", 16), bg="#ff9933", activebackground="#ffcc66", command=button_multiply,padx=0, pady=0)
button_divide = tk.Button(window, text="/", width=6, height=3,font=("Helvetica", 16), bg="#ff9933", activebackground="#ffcc66",  command=button_divide,padx=0, pady=0)
button_power = tk.Button(window, text="x^y", width=6, height=3,font=("Helvetica", 16),  bg="#ff9933", activebackground="#ffcc66", command=button_power,padx=0, pady=0)
button_root = tk.Button(window, text="y√x", width=6, height=3, font=("Helvetica", 16), bg="#ff9933", activebackground="#ffcc66", command=button_root,padx=0, pady=0)
button_dot = tk.Button(window, text=".", width=6, height=3, font=("Helvetica", 16),  bg="#ff9933", activebackground="#ffcc66",command=button_dot,padx=0, pady=0)
button_factorial = tk.Button(window, text="x!", width=6, height=3, font=("Helvetica", 16),  bg="#ff9933", activebackground="#ffcc66", command=button_factorial,padx=0, pady=0)
button_log = tk.Button(window, text="x log y", width=6, height=3, font=("Helvetica", 16),  bg="#ff9933", activebackground="#ffcc66", command=button_log,padx=0, pady=0)
button_help = tk.Button(window, text="?",bg="#FFFFFF", fg="#333333", bd=0, highlightthickness=0, padx=0, pady=0, command=show_help)
# Put the buttons on the screen
button_1.grid(row=4, column=0,sticky=tk.NSEW)
button_2.grid(row=4, column=1,sticky=tk.NSEW)
button_3.grid(row=4, column=2,sticky=tk.NSEW)

button_4.grid(row=3, column=0,sticky=tk.NSEW)
button_5.grid(row=3, column=1,sticky=tk.NSEW)
button_6.grid(row=3, column=2,sticky=tk.NSEW)

button_7.grid(row=2, column=0,sticky=tk.NSEW)
button_8.grid(row=2, column=1,sticky=tk.NSEW)
button_9.grid(row=2, column=2,sticky=tk.NSEW)

button_0.grid(row=5, column=0,sticky=tk.NSEW)
button_help.place(x=0, y=0)
button_clear.grid(row=5, column=1,sticky=tk.NSEW)
button_add.grid(row=6, column=0,sticky=tk.NSEW)
button_equal.grid(row=5, column=2,sticky=tk.NSEW)

button_subtract.grid(row=7, column=0,sticky=tk.NSEW)
button_multiply.grid(row=7, column=1,sticky=tk.NSEW)
button_divide.grid(row=7, column=2,sticky=tk.NSEW)

button_power.grid(row=8, column=0,sticky=tk.NSEW)
button_root.grid(row=8, column=1,sticky=tk.NSEW)
button_dot.grid(row=8, column=2,sticky=tk.NSEW)
button_factorial.grid(row=6, column=1,sticky=tk.NSEW)
button_log.grid(row=6, column=2,sticky=tk.NSEW)
window.bind("1", lambda event: button_1.invoke())
window.bind("2", lambda event: button_2.invoke())
window.bind("3", lambda event: button_3.invoke())
window.bind("4", lambda event: button_4.invoke())
window.bind("5", lambda event: button_5.invoke())
window.bind("6", lambda event: button_6.invoke())
window.bind("7", lambda event: button_7.invoke())
window.bind("8", lambda event: button_8.invoke())
window.bind("9", lambda event: button_9.invoke())
window.bind("0", lambda event: button_0.invoke())
window.bind("+", lambda event: button_add.invoke())
window.bind("-", lambda event: button_subtract.invoke())
window.bind("/", lambda event: button_divide.invoke())
window.bind("*", lambda event: button_multiply.invoke())
window.bind(".", lambda event: button_dot.invoke())
window.bind("^", lambda event: button_power.invoke())
window.bind("<Return>", lambda event: button_equal.invoke())





# Run the program
window.mainloop()