import math
import openpyxl
from openpyxl import Workbook
from openpyxl.utils import get_column_letter


class Calculator:
    def __init__(self, val1: float, val2: float):
        self.val1 = float(val1)
        self.val2 = float(val2)

    def sum_plus(self):
        try:
            return float(self.val1) + float(self.val2)
        except Exception as error:
            print(error)
            return "None"

    def sum_minus(self):
        try:
            return float(self.val1) - float(self.val2)
        except Exception as error:
            print(error)
            return "None"

    def multiply(self):
        try:
            return float(self.val1) * float(self.val2)
        except Exception as error:
            print(error)
            return "None"

    def divide(self):
        try:
            return float(self.val1) / float(self.val2)
        except Exception as error:
            print(error)
            return "None"

    def exponentiation(self):
        try:
            return float(self.val1) ** float(self.val2)
        except Exception as error:
            print(error)
            return "None"

    def division_without_remainder(self):
        try:
            return float(self.val1) // float(self.val2)
        except Exception as error:
            print(error)
            return "None"

    def remainder_of_division(self):
        try:
            return float(self.val1) % float(self.val2)
        except Exception as error:
            print(error)
            return "None"

# STATIC
    @staticmethod
    def sum_plus_static(val1, val2):
        try:
            return float(val1) + float(val2)
        except Exception as error:
            print(error)
            return "None"

    @staticmethod
    def sum_minus_static(val1, val2):
        try:
            return float(val1) - float(val2)
        except Exception as error:
            print(error)
            return "None"

    @staticmethod
    def multiply_static(val1, val2):
        try:
            return float(val1) * float(val2)
        except Exception as error:
            print(error)
            return "None"

    @staticmethod
    def divide_static(val1, val2):
        try:
            return float(val1) / float(val2)
        except Exception as error:
            print(error)
            return "None"

    @staticmethod
    def exponentiation_static(val1, val2):
        try:
            return float(val1) ** float(val2)
        except Exception as error:
            print(error)
            return "None"

    @staticmethod
    def division_without_remainder_static(val1, val2):
        try:
            return float(val1) // float(val2)
        except Exception as error:
            print(error)
            return "None"

    @staticmethod
    def remainder_of_division_static(val1, val2):
        try:
            return float(val1) % float(val2)
        except Exception as error:
            print(error)
            return "None"


print("Calculator:\n")
numbers = Calculator(12, 2)
print(numbers.divide())
print(numbers.sum_plus())
print(numbers.sum_minus())
print(numbers.multiply())
print(numbers.divide())
print(numbers.division_without_remainder())
print(numbers.remainder_of_division())

print("\n STATIC")
print(Calculator.divide_static(12, 2))
print(Calculator.sum_plus_static(12, 2))
print(Calculator.sum_minus_static(12, 2))
print(Calculator.multiply_static(12, 2))
print(Calculator.divide_static(12, 2))
print(Calculator.division_without_remainder_static(12, 2))
print(Calculator.remainder_of_division_static(12, 2))
