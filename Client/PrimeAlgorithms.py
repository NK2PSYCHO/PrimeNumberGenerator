# Import the 'RangeGenerator' class from the 'RangeGenerator' module
from RangeGenerator import RangeGenerator

# Import the 'math' module, which provides access to mathematical functions
import math

# Define a class named 'PrimeAlgorithms'
class PrimeAlgorithms:

    # Initialize the 'PrimeAlgorithms' class
    def __init__(self):
        # Create an instance of 'RangeGenerator' and assign it to the '_range' attribute
        self._range = RangeGenerator()

        # Define a default message to be returned when no primes are found
        self._message = "No Prime Values present in the range"

    # Define a method 'trialDivision' that takes a single argument 'rangeSet'
    def trialDivision(self, rangeSet):
        try:
            # Initialize an empty list '_primes' to store prime numbers
            _primes = []

            # Generate a range of values from 'rangeSet' using the 'generateRange' method of '_range'
            _rangeValues = self._range.generateRange(rangeSet)

            # Remove 0 and 1 from the set of range values since they are not prime
            _rangeValues.discard(0)
            _rangeValues.discard(1)

            # Iterate over each value in '_rangeValues'
            for prime in _rangeValues:
                # Iterate from 2 to the square root of 'prime' to check for divisors
                for i in range(2, int(math.sqrt(prime)) + 1):
                    # If 'prime' is divisible by 'i', it is not a prime number
                    if prime % i == 0:
                        # Exit the inner loop if a divisor is found
                        break
                else:
                    # If no divisor is found, 'prime' is a prime number
                    # Add 'prime' to the '_primes' list
                    _primes.append(prime)

            # Return the list of primes if it's not empty; otherwise, return the default message
            return _primes if _primes else self._message

        # Handle any exceptions that occur during the process
        except Exception as e:
            # Return an error message with details about the exception
            return f"An error occurred during trial division: {e}"

    # Define a method 'enhancedTrialDivision' that takes a single argument 'rangeSet'
    def enhancedTrialDivision(self, rangeSet):
        try:
            # Initialize an empty list '_primes' to store prime numbers
            _primes = []

            # Generate a range of values from 'rangeSet' using the 'generateRange' method of '_range'
            _rangeValues = self._range.generateRange(rangeSet)

            # Remove 0 and 1 from the set of range values since they are not prime
            _rangeValues.discard(0)
            _rangeValues.discard(1)

            # Iterate over the first few known prime numbers (2, 3, 5)
            for prime in [2, 3, 5]:
                # If 'prime' is in '_rangeValues'
                if prime in _rangeValues:
                    # Add 'prime' to the '_primes' list
                    _primes.append(prime)

                # If '_rangeValues' is not empty
                if _rangeValues:
                    # Remove multiples of 'prime' from '_rangeValues'
                    _rangeValues.difference_update(set(range(prime, max(_rangeValues) + 1, prime)))
                else:
                    # Return the default message if no values are left in '_rangeValues'
                    return self._message

            # Iterate over the remaining values in '_rangeValues'
            for prime in _rangeValues:
                # Iterate from 2 to the square root of 'prime' to check for divisors
                for i in range(2, int(math.sqrt(prime)) + 1):
                    # If 'prime' is divisible by 'i', it is not a prime number
                    if prime % i == 0:
                        # Exit the inner loop if a divisor is found
                        break
                else:
                    # If no divisor is found, 'prime' is a prime number
                    # Add 'prime' to the '_primes' list
                    _primes.append(prime)

            # Return the list of primes if it's not empty; otherwise, return the default message
            return _primes if _primes else self._message

        # Handle any exceptions that occur during the process
        except Exception as e:
            # Return an error message with details about the exception
            return f"An error occurred during enhanced trial division: {e}"

    # Define a method 'eratosthenesSieve' that takes a single argument 'rangeSet'
    def eratosthenesSieve(self, rangeSet):
        try:
            # Generate a range of values from 'rangeSet' using the 'generateRange' method of '_range'
            _rangeValues = self._range.generateRange(rangeSet)

            # Determine the maximum number in the generated range
            _maxNum = max(_rangeValues)

            # Create a list '_isPrime' to track prime status, initialized to 'True'
            _isPrime = [True] * (_maxNum + 1)

            # Set index 0 and 1 to 'False' since 0 and 1 are not prime numbers
            _isPrime[0] = _isPrime[1] = False

            # Iterate over each number from 2 to the square root of '_maxNum'
            for prime in range(2, int(math.sqrt(_maxNum)) + 1):
                # If the number is marked as prime
                if _isPrime[prime]:
                    # Mark all multiples of 'prime' as 'False' starting from 'prime^2'
                    for i in range(prime * prime, _maxNum + 1, prime):
                        _isPrime[i] = False

            # Create a set of prime numbers from '_rangeValues' using the '_isPrime' list
            _primes = {num for num in _rangeValues if _isPrime[num]}

            # Return the set of primes if it's not empty; otherwise, return the default message
            return _primes if _primes else self._message

        # Handle any exceptions that occur during the process
        except Exception as e:
            # Return an error message with details about the exception
            return f"An error occurred during Sieve of Eratosthenes: {e}"
