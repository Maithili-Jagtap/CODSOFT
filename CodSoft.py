import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Choose operation":
            result_label.config(text="Please choose an operation.")
        else:
            if operation == "Addition":
                result = num1 + num2
            elif operation == "Subtraction":
                result = num1 - num2
            elif operation == "Multiplication":
                result = num1 * num2
            elif operation == "Division":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Cannot divide by zero."

            result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widgets for numbers
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

# Dropdown for operation choice
label_operation = tk.Label(root, text="Choose operation:")
label_operation.grid(row=2, column=0, padx=10, pady=10)
operations = ["Choose operation", "Addition", "Subtraction", "Multiplication", "Division"]
operation_var = tk.StringVar(root)
operation_var.set(operations[0])  # default choice
dropdown_operation = tk.OptionMenu(root, operation_var, *operations)
dropdown_operation.grid(row=2, column=1, padx=10, pady=10)

# Button to perform the calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label to display the result
result_label = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
