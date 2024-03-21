import math
import tkinter as tk
from functions import functions


# Create the main application window
root = tk.Tk()
root.title("Command Line App UI")

# Define your functions here
custom_functions = functions
custom_functions['exit'] = exit


# Create a frame to hold the buttons
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Create buttons for each function
total_functions_length = len(custom_functions)
mid = math.ceil(total_functions_length/2)
for i, (function, _) in enumerate(custom_functions.items()):
    button = tk.Button(frame, text=function, width=40, command=lambda f=function: custom_functions[f]())
    button.grid(row=(i % mid), column=math.floor(i / mid), pady=5)



root.mainloop()
