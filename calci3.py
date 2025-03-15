import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator with Backward Option")
        self.geometry("320x470")
        self.resizable(False, False)
        self.create_widgets()
        self.history = []  # To store expressions for backward option

    def create_widgets(self):
        self.expression = ""

        # Entry widget to display expressions and results
        self.entry = tk.Entry(
            self,
            font=("Arial", 20),
            bd=10,
            relief=tk.RIDGE,
            justify='right',
            bg="#F0F0F0"
        )
        self.entry.grid(row=0, column=0, columnspan=4, pady=10, padx=5, sticky="nsew")

        # Single button color
        button_color = "#90CAF9"  # Light blue for all buttons

        # Buttons layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('Back', 5, 1)
        ]

        for (text, row, col) in buttons:
            tk.Button(
                self,
                text=text,
                font=("Arial", 14),
                width=5,
                height=2,
                bg=button_color,
                activebackground="#64B5F6",
                command=lambda t=text: self.button_clicked(t)
            ).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        # Configure grid weights for responsiveness
        for i in range(7):
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)

    def button_clicked(self, text):
        if text == "=":
            try:
                result = str(eval(self.expression))
                self.history.append(self.expression)  # Save expression to history
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
                self.expression = result
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
                self.expression = ""
        elif text == "C":
            self.entry.delete(0, tk.END)
            self.expression = ""
        elif text == "Back":
            if self.history:
                last_expression = self.history.pop()  # Retrieve last expression
                self.expression = last_expression
                self.entry.delete(0, tk.END)
                self.entry.insert(0, last_expression)
            else:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "0")
        else:
            self.expression += text
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
