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
    
    def clear_screen(self):
        os.system('cls' if os.name == "nt" else "clear")
        
    def execute(self):
        while True:
            self.clear_screen()
            Menu.show()
            
            choice = self.input_handler.get_input("Wprowadź numer działania")
            
            if choice == 5:
                print("\nDziękujemy za skorzystanie z kalkulatora!")
                sys.exit(0)
            
            if choice not in [1, 2, 3, 4]:
                self.clear_screen()
                print(f"\nNieprawidłowy wybór. Proszę wybrać liczbę od 1 do 5.\n")
                input("Wciśnij Enter, aby kontynuować") 
                continue
            

            a, b = self.get_numbers()
                
            match choice:
                case 1: 
                    operation = Addition(a, b)
                case 2: 
                    operation = Subtraction(a, b)
                case 3: 
                    operation = Multiplication(a, b)
                case 4:
                    operation = Division(a, b)
                case _:
                    print(f"\nNieprawidłowy wybór.\n")
                
            try:
                result = operation.calculate()
                self.output_handler.display_result(result)
            except ValueError as e:
                print(e)
                                
            exit_choice = self.input_handler.get_input("\nCzy chcesz zakończyć program? 1 - Tak, dowolna liczba - Nie")
            if exit_choice == 1:
                print("\nDziękujemy za skorzystanie z kalkulatora!")
                sys.exit(0)