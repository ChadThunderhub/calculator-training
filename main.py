import sys

from operations.addition import Addition
from operations.subtraction import Subtraction
from operations.multiplication import Multiplication
from operations.division import Division

from interface.draw import Draw
from interface.input_handler import InputHandler
from interface.output_handler import OutputHandler


def main():
    
    input_handler = InputHandler()
    output_handler = OutputHandler()

    a = input_handler.get_input("Podaj pierwszą liczbę")
    b = input_handler.get_input("Podaj drugą liczbę")

    addition = Addition(a, b)
    subtraction = Subtraction(a, b)
    multiplication = Multiplication(a, b)
    division = Division(a, b)

    output_handler.display_result(addition.calculate())
    output_handler.display_result(subtraction.calculate())
    output_handler.display_result(multiplication.calculate())
    
    try:
        output_handler.display_result(division.calculate())
    except ValueError as e:
        print(e)