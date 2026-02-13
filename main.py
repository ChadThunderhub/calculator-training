import sys

from interface.menu import Menu
from interface.logic import Logic
from interface.input_handler import InputHandler
from interface.output_handler import OutputHandler


def main():
    menu = Menu.show()
    
    input_handler = InputHandler()
    output_handler = OutputHandler()
    
    logic = Logic(input_handler, output_handler)
    logic.execute()
        
if __name__ == "__main__":
    main()