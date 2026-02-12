class InputHandler:
    def get_input(self, message):
        while True:
            try:
                return float(input(f"{message}: "))
            except ValueError:
                print("Nieprawidłowe dane. Proszę podać liczby.")