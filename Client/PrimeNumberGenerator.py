from UserInput import UserInput
from RangeGenerator import RangeGenerator

class PrimeNumberGenerator():

    def __init__(self):
        self._user = UserInput()
        self._range = RangeGenerator()

    def main(self):
        self._user.setUserInput()
        rangeSet = self._user.getUserInput()
        start, end = rangeSet
        print(f"Start of the range is set to {start}")
        print(f"End of the range is set to {end}")
        print(f"The generated range is {self._range.generateRange(rangeSet)}")
        
if __name__ == "__main__":
    generator = PrimeNumberGenerator()
    generator.main()