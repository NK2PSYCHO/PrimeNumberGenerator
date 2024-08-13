# Import the 'UserInput' class from the 'UserInput' module
from UserInput import UserInput

# Import the 'PrimeAlgorithms' class from the 'PrimeAlgorithms' module
from PrimeAlgorithms import PrimeAlgorithms

# Define a class named 'PrimeNumberGenerator'
class PrimeNumberGenerator():

    # Define the main method which will run the program
    def main(self):
        try:
            # Create an instance of the 'UserInput' class and assign it to '_user'
            _user = UserInput()
            
            # Create an instance of the 'PrimeAlgorithms' class and assign it to '_algo'
            _algo = PrimeAlgorithms()

            # Call the 'setUserInput' method to collect user input
            _user.setUserInput()
            
            # Retrieve the selected algorithm and range set from the user input
            _algorithm, rangeSet = _user.getUserInput()

            # Create a list of algorithm methods from the 'PrimeAlgorithms' class
            algorithms = [
                _algo.trialDivision,
                _algo.enhancedTrialDivision,
                _algo.eratosthenesSieve,
            ]

            # Select the algorithm based on the user's choice
            selected_algorithm = algorithms[_algorithm - 1]

            # Execute the selected algorithm with the provided range set and store the result in 'primes'
            primes = selected_algorithm(rangeSet)
            
            # Check if the result is a set (indicating prime numbers were found)
            if isinstance(primes, set):
                # Print the prime numbers found in the specified range
                print(f"Prime numbers in the range are: {primes}")
            else:
                # If the result is not a set (indicating no primes were found)
                print(primes)
                # Print the message returned by the algorithm (e.g., no primes found)
        
        # Handle any exceptions that occur during the process
        except Exception as e:
            # Print an error message with details about the exception
            print(f"An error occurred in the main program: {e}")
        
# Check if the script is being run directly (not imported)
if __name__ == "__main__":
    # Create an instance of the 'PrimeNumberGenerator' class
    generator = PrimeNumberGenerator()
    
    # Call the 'main' method to run the program
    generator.main()
