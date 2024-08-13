# Define a class named 'InputValidator'
class InputValidator:
    
    # Define a static method 'validateRangeInput' that takes a single argument 'prompt'
    @staticmethod
    def validateRangeInput(prompt):
        # Start an infinite loop to repeatedly prompt the user for input until valid
        while True:
            # Attempt to execute the following block of code
            try:
                # Prompt the user for input and convert the input to an integer
                value = int(input(prompt))

                # Check if the entered value is negative
                if value < 0:
                    # Display an error message if the value is negative and continue the loop
                    print("The value must be non-negative. Please try again.")
                else:
                    # If the value is non-negative, return the value and exit the loop
                    return value
                
            # Handle the case where the input is not a valid integer
            except ValueError:
                # Handle the case where the input is not a valid integer
                # Display an error message indicating that the input is invalid
                print("Invalid input. Please enter a valid integer.")
            
            # Handle any other unexpected exceptions
            except Exception as e:
                # Handle any other unexpected exceptions
                # Display a general error message with details about the exception
                print(f"An error occurred during range validation: {e}")

    # Define a static method 'validateMenuInput' that takes a 'prompt' and a list of 'options'
    @staticmethod
    def validateMenuInput(prompt, options):
        # Start an infinite loop to repeatedly prompt the user for input until valid
        while True:
            # Attempt to execute the following block of code
            try:
                # Print the provided prompt message
                print(prompt)

                # Enumerate through the 'options' list, starting the index at 1
                for i, option in enumerate(options, 1):
                    # Print each option with a corresponding number
                    print(f"{i}. {option}")

                # Prompt the user to select an option and convert the input to an integer
                value = int(input("Please select an option: "))

                # Check if the entered value is within the valid range of options
                if 1 <= value <= len(options):
                    # If the value is valid, return the value and exit the loop
                    return value
                else:
                    # If the value is out of range, display an error message and continue the loop
                    print(f"The value must be in the range of 1 to {len(options)}. Please try again.")
    
            # Handle the case where the input is not a valid integer
            except ValueError:
                # Handle the case where the input is not a valid integer
                # Display an error message indicating that the input is invalid
                print("Invalid input. Please enter a valid integer.")
            
            # Handle any other unexpected exceptions
            except Exception as e:
                # Handle any other unexpected exceptions
                # Display a general error message with details about the exception
                print(f"An error occurred during menu validation: {e}")
