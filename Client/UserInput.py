from InputValidator import InputValidator

class UserInput:

    def __init__(self):
        self._starting = None
        self._ending = None

    def _setStarting(self):
        self._starting = InputValidator.validateInput("Enter the start of the range ")

    def _setEnding(self):
        self._ending = InputValidator.validateInput("Enter the end of the range ")

    def _getStarting(self):
        return self._starting
    
    def _getEnding(self):
        return self._ending
    
    def setUserInput(self):
        self._setStarting()
        self._setEnding()

    def getUserInput(self):
        return sorted([self._getStarting(),self._getEnding()])