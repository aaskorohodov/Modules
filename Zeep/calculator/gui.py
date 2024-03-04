import tkinter as tk

from Zeep.calculator.calculator_logic_interface import CalculatorLogicInterface


class CalculatorApp:
    """Main application. Responsible for GUI-window

    Attributes:
        calculator_logic: Instance, responsible for calculation logic
        root: Window, made with Tk"""

    def __init__(self, calculator_logic: CalculatorLogicInterface):
        self.calculator_logic: CalculatorLogicInterface = calculator_logic

        self.root: tk.Tk = tk.Tk()
        self.root.title("Calculator")

        self._create_entries()
        self._create_result_field()
        self._create_buttons()

        self.root.mainloop()

    def _create_entries(self) -> None:
        """Create 2 input fields for 2 numbers and 2 labels for each input"""

        self.label1 = tk.Label(self.root, text="Enter the first number:")
        self.label1.pack(pady=5, padx=10, anchor='w')

        self.entry1 = tk.Entry(self.root, width=15)
        self.entry1.pack(pady=5, padx=10)

        self.label2 = tk.Label(self.root, text="Enter the second number:")
        self.label2.pack(pady=5, padx=10, anchor='w')

        self.entry2 = tk.Entry(self.root, width=15)
        self.entry2.pack(pady=5, padx=10)

    def _create_result_field(self) -> None:
        """Creates an empty filed to put result into"""

        # Label to display the result
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)

    def _create_buttons(self) -> None:
        """Creates buttons, each responsible for some operation (add, divide...)"""

        add_button = tk.Button(self.root, text="Add", command=lambda: self.calculate("Add"))
        add_button.pack(pady=5)

        subtract_button = tk.Button(self.root, text="Subtract", command=lambda: self.calculate("Subtract"))
        subtract_button.pack(pady=5)

        multiply_button = tk.Button(self.root, text="Multiply", command=lambda: self.calculate("Multiply"))
        multiply_button.pack(pady=5)

        divide_button = tk.Button(self.root, text="Divide", command=lambda: self.calculate("Divide"))
        divide_button.pack(pady=5)

    def calculate(self, operation_name: str) -> None:
        """Reads numbers from entries, gets operation_name from button and calls for calculation-logic

        Args:
            operation_name: Name of the operation (Divide, Add...)"""

        num1 = self.entry1.get()
        num2 = self.entry2.get()
        numbers = (num1, num2)

        try:
            # Setting result-label and updating Window, as operation will take a while
            self.result_label.config(text='.................................')
            self.root.update_idletasks()

            result = self.calculator_logic.calculate(operation_name, numbers)
            self.result_label.config(text=f"{operation_name} Result: {result}")
        except Exception as e:
            self.result_label.config(text=e.__str__())
