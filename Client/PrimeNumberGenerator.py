# We import the UserInput class so we can call the apt methods to 
# set and get the values of the required attributes.
from Client.UserInput import UserInput

# We import the PrimeAlgorithms class so the apt method containing the algorithm
# of the user's selection can be called to get prime numbers in a range.
from Client.PrimeAlgorithms import PrimeAlgorithms

# PrimeNumberGenerator class contains the main method of the program.
class PrimeNumberGenerator():

    # Main method will run the program by calling the requried methods, it is a static method
    # so it can be called directly without creating an instance of the class. 
    @staticmethod
    def main():
        try:
            # We create an instance of UserInput class so we can call the required set and get method.
            _user = UserInput()

            # setUserInput is called from the UserInput class to set input for algorithm and start,end of the 
            # range to be generated.
            _user.setUserInput()
            
            # getUserInput is called from the UserInput class to get input for algorithm and start,end of the 
            # range to be generated.
            _algorithm, rangeSet = _user.getUserInput()

            # This is the list for the algorithm methods present in PrimeAlgorithms for indexing.
            algorithms = [
                PrimeAlgorithms.trialDivision,
                PrimeAlgorithms.enhancedTrialDivision,
                PrimeAlgorithms.eratosthenesSieve,
            ]

            # We now select the apt method according to the user's algorithm selection.
            selected_algorithm = algorithms[_algorithm - 1]

            # We know execute the selected method for the opted algorithm to get the list of
            # prime numbers found in the range.
            primes = selected_algorithm(rangeSet)
            
            # We check if the result recieved is a list (to confirm that no exception occurred).
            if isinstance(primes, list):
                # If the result is a list, we print the list of prime numbers.
                print(f"Prime numbers in the range are: {primes}")
            else:
                # If the result is not a list, we print any message returned by the algorithm function.
                print(primes)

        except Exception as e:
            # Here we handle any other exception that may occur. We print a 
            # general message and the exception thrown for details.
            print(f"An error occurred in the main program: {e}")
        
# Here we check if the script is being run directly if so the latter will be executed.
if __name__ == "__main__":
    
    # Call the 'main' method to run the program
    PrimeNumberGenerator.main()
