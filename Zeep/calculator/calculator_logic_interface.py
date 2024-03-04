from abc import ABC, abstractmethod


class CalculatorLogicInterface(ABC):
    @abstractmethod
    def calculate(self, operation: str, numbers: tuple[str, str]) -> int | float:
        pass
