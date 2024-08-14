# We import the InputValidator class to use the satitc validator functions
# that will be used to validate range input and menu input.
from InputValidator import InputValidator

# UserInput class will contain the methods that will be used to handle User input
# for range input and menu input.
class UserInput:

    # This is the constructor for the UserInput class and will have attributes that will
    # be used amongst all of the methods.
    def __init__(self):
        # We initialize the _starting attribute to store the range starting input given by user.
        self._starting = None
        
        # We initialize the _ending attribute to store the range ending input given by user.
        self._ending = None
        
        # We initialize the _algorithm attribute to store the algorithm index opted by user.
        self._algorithm = None

    # Private method _setStarting is used to get input from user and set the value for _starting.
    def _setStarting(self):
        try:
            # ValidateRangeInput is used to validate the range starting input from the user
            # and set the value for the _starting attribute.
            self._starting = InputValidator.validateRangeInput("Enter the start of the range ")
        except Exception as e:
            # Here we handle any other exception that may occur. We print a 
            # general message and the exception thrown for details.
            print(f"An error occurred while setting the starting value: {e}")

     # Private method _setEnding is used to get input from user and set the value for _ending.
    def _setEnding(self):
        try:
            # ValidateRangeInput is used to validate the range ending input from the user
            # and set the value for the _ending attribute.
            self._ending = InputValidator.validateRangeInput("Enter the end of the range ")
        except Exception as e:
            # Here we handle any other exception that may occur. We print a 
            # general message and the exception thrown for details.
            print(f"An error occurred while setting the ending value: {e}")

    # Private method _setAlgorithm is used to get input from user and set the value for _algorithm.
    def _setAlgorithm(self):
        try:
            # This is the list of algorithm options available for the user to opt from.
            algorithms = ["Trial Division", "Enhanced Trial Division", "Sieve of Eratosthenes"]
            
            # ValidateMenuInput is used to validate the option selection input from the user
            # and set the value for the _algorithm attribute.
            self._algorithm = InputValidator.validateMenuInput("Select your algorithm:", algorithms)
        except Exception as e:
            # Here we handle any other exception that may occur. We print a 
            # general message and the exception thrown for details.
            print(f"An error occurred while setting the algorithm: {e}")
    
    # Public method setUserInput can be called to access all other private methods
    # that are used to set different attributes.
    def setUserInput(self):
        try:
            # _setAlgorithm is called to set the _algorithm attribute.
            self._setAlgorithm()
            
            # _setStarting is called to set the _starting attribute.
            self._setStarting()
            
            # _setEnding is called to set the _ending attribute.
            self._setEnding()
        except Exception as e:
            # Here we handle any other exception that may occur. We print a 
            # general message and the exception thrown for details.
            print(f"An error occurred while setting user input: {e}")

    # Public method getUserInput is used to get the values of all the attributes present.
    def getUserInput(self):
        # We return the values in a tuple format with value of _algorithm attribute and sorted
        # values of _starting and _ending attribute. (User can enter the range points in any manner
        # the validations are to check integer and non-negative only).
        return (self._algorithm, sorted([self._starting, self._ending]))
