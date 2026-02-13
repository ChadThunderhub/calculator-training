import sys
import os
from operations.addition import Addition
from operations.subtraction import Subtraction
from operations.division import Division
from operations.multiplication import Multiplication
from interface.menu import Menu

class Logic:
    def __init__(self, input_handler, output_handler):
        self.input_handler = input_handler
        self.output_handler = output_handler
        
    def get_numbers(self):
        a = self.input_handler.get_input("Podaj pierwszą liczbę")
        b = self.input_handler.get_input("Podaj drugą liczbę")
        return a, b
    def set_numbers(self, a, b):
        self.a = a
        self.b = b
    def clear_screen(self):
        os.system('cls' if os.name == "nt" else "clear")
        
    def execute(self):
        self.clear_screen()
        Menu.show()
        
        choice = self.input_handler.get_input("Wprowadź numer działania")
        

        if choice == 1:
            a, b = self.get_numbers()
            self.set_numbers(a, b)
            operation = Addition(a, b)
            result = operation.calculate()
            self.output_handler.display_result(result)

        elif choice == 2:
            a, b = self.get_numbers()
            self.set_numbers(a, b)
            operation = Subtraction(a, b)
            result = operation.calculate()
            self.output_handler.display_result(result)

        elif choice == 3:
            a, b = self.get_numbers()
            self.set_numbers(a, b)
            operation = Multiplication(a, b)
            result = operation.calculate()
            self.output_handler.display_result(result)

        elif choice == 4:
            a, b = self.get_numbers()
            self.set_numbers(a, b)
            operation = Division(a, b)
            try:
                result = operation.calculate()
                self.output_handler.display_result(result)
            except ValueError as e:
                print(e)
                
        elif choice == 5:
            print("\nDziękujemy za skorzystanie z kalkulatora!")
            sys.exit(0)

        else:
            print(f"\nNieprawidłowy wybór.\n")
            print("Czy chcesz spróbować ponownie? 0 - Nie, 1 - Tak")
            retry = self.input_handler.get_input("Wprowadź numer")
            if retry == 1:
                self.clear_screen()
                self.execute()
            
        exit = self.input_handler.get_input("\nCzy chcesz zakończyć program? 0 - Nie, 1 - Tak")
        if exit == 1:
            print("\nDziękujemy za skorzystanie z kalkulatora!")
            sys.exit(0)
        else:
            self.clear_screen()
            self.execute()