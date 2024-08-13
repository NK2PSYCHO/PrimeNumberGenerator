# Import the 'InputValidator' class from the 'InputValidator' module
from InputValidator import InputValidator

# Define a class named 'UserInput'
class UserInput:

    # Initialize the 'UserInput' class
    def __init__(self):
        # Initialize the '_starting' attribute to store the starting value of the range
        self._starting = None
        
        # Initialize the '_ending' attribute to store the ending value of the range
        self._ending = None
        
        # Initialize the '_algorithm' attribute to store the selected algorithm
        self._algorithm = None

    # Define a private method '_setStarting' to set the starting value
    def _setStarting(self):
        try:
            # Use 'validateRangeInput' to prompt the user for the starting value and assign it to '_starting'
            self._starting = InputValidator.validateRangeInput("Enter the start of the range ")
        # Handle any exceptions that occur during the process
        except Exception as e:
            # Print an error message with details about the exception
            print(f"An error occurred while setting the starting value: {e}")

    # Define a private method '_setEnding' to set the ending value
    def _setEnding(self):
        try:
            # Use 'validateRangeInput' to prompt the user for the ending value and assign it to '_ending'
            self._ending = InputValidator.validateRangeInput("Enter the end of the range ")
        # Handle any exceptions that occur during the process
        except Exception as e:
            # Print an error message with details about the exception
            print(f"An error occurred while setting the ending value: {e}")

    # Define a private method '_setAlgorithm' to set the algorithm choice
    def _setAlgorithm(self):
        try:
            # Define a list of algorithm options
            algorithms = ["Trial Division", "Enhanced Trial Division", "Sieve of Eratosthenes"]
            
            # Use 'validateMenuInput' to prompt the user to select an algorithm and assign it to '_algorithm'
            self._algorithm = InputValidator.validateMenuInput("Select your algorithm:", algorithms)
        # Handle any exceptions that occur during the process
        except Exception as e:
            # Print an error message with details about the exception
            print(f"An error occurred while setting the algorithm: {e}")

    # Define a private method '_getStarting' to retrieve the starting value
    def _getStarting(self):
        # Return the value stored in '_starting'
        return self._starting
    
    # Define a private method '_getEnding' to retrieve the ending value
    def _getEnding(self):
        # Return the value stored in '_ending'
        return self._ending
    
    # Define a private method '_getAlgorithm' to retrieve the algorithm choice
    def _getAlgorithm(self):
        # Return the value stored in '_algorithm'
        return self._algorithm
    
    # Define a public method 'setUserInput' to collect user input
    def setUserInput(self):
        try:
            # Call the private method '_setAlgorithm' to set the algorithm choice
            self._setAlgorithm()
            
            # Call the private method '_setStarting' to set the starting value
            self._setStarting()
            
            # Call the private method '_setEnding' to set the ending value
            self._setEnding()
        # Handle any exceptions that occur during the process
        except Exception as e:
            # Print an error message with details about the exception
            print(f"An error occurred while setting user input: {e}")

    # Define a public method 'getUserInput' to retrieve the collected user input
    def getUserInput(self):
        # Return a tuple containing the algorithm choice and a sorted list of the starting and ending values
        return (self._algorithm, sorted([self._getStarting(), self._getEnding()]))
