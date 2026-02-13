from operations.addition import Addition
from operations.subtraction import Subtraction
from operations.division import Division
from operations.multiplication import Multiplication

class Logic:
    def __init__(self, input_handler, output_handler):
        self.input_handler = input_handler
        self.output_handler = output_handler
        
    def execute(self):
        choice = self.input_handler.get_input("Wprowadź numer działania")

        if choice == 1:
            a = self.input_handler.get_input("Podaj pierwszą liczbę")
            b = self.input_handler.get_input("Podaj drugą liczbę")
            operation = Addition(a, b)
            result = operation.calculate()
            self.output_handler.display_result(result)

        elif choice == 2:
            a = self.input_handler.get_input("Podaj pierwszą liczbę")
            b = self.input_handler.get_input("Podaj drugą liczbę")
            operation = Subtraction(a, b)
            result = operation.calculate()
            self.output_handler.display_result(result)

        elif choice == 3:
            a = self.input_handler.get_input("Podaj pierwszą liczbę")
            b = self.input_handler.get_input("Podaj drugą liczbę")
            operation = Multiplication(a, b)
            result = operation.calculate()
            self.output_handler.display_result(result)

        elif choice == 4:
            a = self.input_handler.get_input("Podaj pierwszą liczbę")
            b = self.input_handler.get_input("Podaj drugą liczbę")
            operation = Division(a, b)
            try:
                result = operation.calculate()
                self.output_handler.display_result(result)
            except ValueError as e:
                print(e)

        else:
            print("Nieprawidłowy wybór.")