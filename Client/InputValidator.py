class InputValidator:

    @staticmethod
    def validateInput(prompt):
        while True:
            try:
                value = int(input(prompt))
                if value < 0:
                    print("The value must be non-negative. Please try again.")
                else:
                    return value
                
            except ValueError:
                print("Invalid input. Please enter a valid integer.")