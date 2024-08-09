from UserInput import UserInput
from PrimeAlgorithms import PrimeAlgorithms


class PrimeNumberGenerator():

    def __init__(self):
        self._user = UserInput()
        self._algo = PrimeAlgorithms()

    def main(self):
        self._user.setUserInput()
        rangeSet = self._user.getUserInput()
        print(f"Prime numbers in the range are ''{self._algo.enhancedTrialDivision(rangeSet)}''")
        
if __name__ == "__main__":
    generator = PrimeNumberGenerator()
    generator.main()