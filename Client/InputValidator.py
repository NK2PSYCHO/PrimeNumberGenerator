# InputValidator class will contain the methods that will validate 
# the input given by the user for range and algorithm.
class InputValidator:
    
    # validateRangeInput validates the user input for range generation, it is a static method 
    # we can call without creating an instance of the class.
    @staticmethod
    def validateRangeInput(prompt):
        # We start an infinite loop so the program can only progress when it 
        # gets a valid input.
        while True:
            try:
                # We prompt the user for an input, and convert the input to integer type
                # (try to do it wong input raises exception)
                value = int(input(prompt))

                # As prime numbers are positive integers we check that the range 
                # endpoints are positive.
                if value < 0:
                    # If the value is negative display error message and prompt the user again.
                    print("The value must be non-negative. Please try again.")
                else:
                    # If the value is non-negative integer, raising no exception we return it.
                    return value

            except ValueError:
                # Here we handle the exception when the user input any value that is of any 
                # other type than integer. (Checking if the Value is of the correct type).
                print("Invalid input. Please enter a valid integer.")
            
            except Exception as e:
                # Here we handle any other exception that may occur. We print a 
                # general message and the exception thrown for details.
                print(f"An error occurred during range validation: {e}")

    # validateMenuInput validates the user input for algorithm selection, it is a static method 
    # we can call without creating an instance of the class.
    @staticmethod
    def validateMenuInput(prompt, options):
        # We start an infinite loop so the program can only progress when it 
        # gets a valid input.
        while True:
            try:
                # We print a part of the prompt we'll ask the user.
                print(prompt)
                # We loop over the list received using enumerate so we get the index as well as value
                # we start at the index 1 not 0.
                for i, option in enumerate(options, 1):
                    # Print the index and value of the current element the loop is pointing to.
                    print(f"{i}. {option}")

                # We prompt the user for an input, and convert the input to integer type
                # (try to do it wong input raises exception)
                value = int(input("Please select an option: "))

                # Here we check if the user input corresponds to any available index.
                if 1 <= value <= len(options):
                    # If the input corresponds to available index, then we return the value.
                    return value
                else:
                    # If the input does not corresponds to any available index, we print a message 
                    # to tell the user so and prompt the user again for the input.
                    print(f"The value must be in the range of 1 to {len(options)}. Please try again.")
    
            except ValueError:
                # Here we handle the exception when the user input any value that is of any 
                # other type than integer. (Checking if the Value is of the correct type).
                print("Invalid input. Please enter a valid integer.")
            
            except Exception as e:
                # Here we handle any other exception that may occur. We print a 
                # general message and the exception thrown for details.
                print(f"An error occurred during menu validation: {e}")
