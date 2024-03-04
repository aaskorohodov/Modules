from typing import Callable
from zeep import Client

from Zeep.calculator.calculator_logic_interface import CalculatorLogicInterface


class SoapCalculator(CalculatorLogicInterface):
    """Calculator, made with SOAP-Based-API

    Attributes:
        client: Zeep's client, to make API-calls with
        operations: Dict of supported operation to map operation with factory-method"""

    def __init__(self, wsdl: str):
        """Init

        Args:
            wsdl: WSDL-path (URL or file-path)"""

        self.client = Client(wsdl=wsdl)

        self.operations = {
            'Add': self._add,
            'Divide': self._divide,
            'Multiply': self._multiply,
            'Subtract': self._subtract
        }

    def calculate(self, operation_name: str, numbers: tuple[str]) -> int:
        """Executes calculation logic

        Args:
            operation_name: Add, Divide...
            numbers: Tuple with 2 numbers, to perform operation on
        Returns:
            Result"""

        numbers = self._convert_numbers(numbers)
        operation_manager = self._select_operation(operation_name)

        return operation_manager(numbers)

    def _convert_numbers(self, numbers: tuple[str]) -> tuple[int]:
        """Converts numbers into integers

        Args:
            numbers: Tuple with 2 numbers (strs)
        Raises:
            ValueError: In case numbers can not be converted into integers
        Returns:
            Tuple with 2 numbers (ints)"""

        if len(numbers) != 2:
            raise ValueError('Only operations on 2 numbers are supported!')

        try:
            converted_numbers = []
            for numb in numbers:
                converted_numbers.append(int(numb))
            return tuple(converted_numbers)
        except ValueError:
            raise ValueError('Unsupported number! Probably a string')

    def _select_operation(self, operation_name: str) -> Callable:
        """Factory method, to select operation-method

        Args:
            operation_name: Divide, Add...
        Raises:
            ValueError: In case operation_name is not supported
        Returns:
            Method to be called for provided operation_name"""

        if operation_name in self.operations:
            return self.operations[operation_name]
        raise ValueError(f'Operation "{operation_name}" is not supported!')

    # Operations

    def _add(self, numbers: tuple[int]) -> int:
        """Adds 2 numbers with SOAP-Request to the API

        Args:
            numbers: Tuple with 2 numbers"""

        return self.client.service.Add(numbers[0], numbers[1])

    def _divide(self, numbers: tuple[int]) -> int:
        """Divides 2 numbers with SOAP-Request to the API

        Args:
            numbers: Tuple with 2 numbers"""

        return self.client.service.Divide(numbers[0], numbers[1])

    def _multiply(self, numbers: tuple[int]) -> int:
        """Multiplies 2 numbers with SOAP-Request to the API

        Args:
            numbers: Tuple with 2 numbers"""

        return self.client.service.Multiply(numbers[0], numbers[1])

    def _subtract(self, numbers: tuple[int]) -> int:
        """Subtracts 2 numbers with SOAP-Request to the API

        Args:
            numbers: Tuple with 2 numbers"""

        return self.client.service.Subtract(numbers[0], numbers[1])
