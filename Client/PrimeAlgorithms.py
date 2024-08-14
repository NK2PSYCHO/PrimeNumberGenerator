# We import the RangeGenerator class so we can use its method to 
# generate the rang eof integers from start value to end.
from Client.RangeGenerator import RangeGenerator

# Math module contains methods related to mathematics, here we use it to calculate
# square root of a value and get the maximum value out of the range.
import math

# PrimeAlgorithms class contains all the methods for algorithms that can be used to filter
# the prime numbers from a given range.
class PrimeAlgorithms:

    # trialDivision method uses the trial division algorithm to filter
    # the prime numbers from a given range.
    @staticmethod
    def trialDivision(rangeSet):
        try:
            # _primes list is initialized that will store the prime numbers from the range and will be returned
            # as result.
            _primes = []

            # _rangValues contains the range of integers that are generated using RangeGenerator's
            # generateRange method which accepts a set of start and end value.
            _rangeValues = RangeGenerator.generateRange(rangeSet)

            # Remove 0 and 1 from the set of range values since they are not prime.
            _rangeValues.discard(0)
            _rangeValues.discard(1)

            # We iterate over the generated integer range.
            for prime in _rangeValues:
                # Iterate from 2 to the square root of the current element(prime) to check for divisors.
                for i in range(2, int(math.sqrt(prime)) + 1):
                    # If the current element is divisble by i it is not prime.
                    if prime % i == 0:
                        # We break the current interation of the inner loop 
                        # (moving on to the next element in the integer range).
                        break
                else:
                    # If no divisor is found we add the current element to the 
                    # _primes list.
                    _primes.append(prime)

            # Return the list of primes if it's not empty; otherwise, return the default message.
            return _primes if _primes else "No Prime Values present in the range"

        except Exception as e:
            # Here we handle any other exception that may occur. We print a 
            # general message and the exception thrown for details.
            return f"An error occurred during trial division: {e}"

    # enhancedTrialDivision method uses the enhanced trial division algorithm to filter
    # the prime numbers from a given range.
    @staticmethod
    def enhancedTrialDivision(rangeSet):
        try:
            # _primes list is initialized that will store the prime numbers from the range and will be returned
            # as result.
            _primes = []

            # _rangValues contains the range of integers that are generated using RangeGenerator's
            # generateRange method which accepts a set of start and end value.
            _rangeValues = RangeGenerator.generateRange(rangeSet)

            # Remove 0 and 1 from the set of range values since they are not prime.
            _rangeValues.discard(0)
            _rangeValues.discard(1)

            # We iterate through the basic primes.
            for prime in [2, 3, 5]:
                # Check f the current element is present in the integer range.
                if prime in _rangeValues:
                    # If the current element is present in the integer range add it to primes list.
                    _primes.append(prime)

                # We check if the integer range still has values (if an iteration has already been
                # conducted and the list is empty) to avoid exceptions.
                if _rangeValues:
                    # We remove the basic primes and their multiples from the list.
                    _rangeValues.difference_update(set(range(prime, max(_rangeValues) + 1, prime)))
                else:
                    # If the range has already been cleared resturn default message.
                    return "No Prime Values present in the range"

            # We iterate over the remaining values of the generated integer range.
            for prime in _rangeValues:
                # Iterate from 2 to the square root of the current element(prime) to check for divisors.
                for i in range(2, int(math.sqrt(prime)) + 1):
                    # If the current element is divisble by i it is not prime.
                    if prime % i == 0:
                        # We break the current interation of the inner loop 
                        # (moving on to the next element in the integer range).
                        break
                else:
                    # If no divisor is found we add the current element to the 
                    # _primes list.
                    _primes.append(prime)

            # Return the list of primes if it's not empty; otherwise, return the default message.
            return _primes if _primes else "No Prime Values present in the range"

        except Exception as e:
            # Here we handle any other exception that may occur. We print a 
            # general message and the exception thrown for details.
            return f"An error occurred during enhanced trial division: {e}"

    # eratosthenesSieve method uses the sieve of eratosthenes algorithm to filter
    # the prime numbers from a given range.
    @staticmethod
    def eratosthenesSieve(rangeSet):
        try:
            # _rangValues contains the range of integers that are generated using RangeGenerator's
            # generateRange method which accepts a set of start and end value.
            _rangeValues = RangeGenerator.generateRange(rangeSet)

            # Determine the maximum number in the generated range
            _maxNum = max(_rangeValues)

            # _isPrime boolean list is created to keep track of prime values
            # currently all values are true.
            _isPrime = [True] * (_maxNum + 1)

            # Set index 0 and 1 to 'False' since 0 and 1 are not prime numbers.
            _isPrime[0] = _isPrime[1] = False

            # We iterate over each number from 2 to the (square root + 1) of maximum number
            # in the generated range.
            for prime in range(2, int(math.sqrt(_maxNum)) + 1):
                # Check if the element in the current iteration is set as prime  
                if _isPrime[prime]:
                    # We mark all the multiples of the element from the current iteration as not prime
                    # (loop starts from the square of the element to the maximum number with the current element
                    # as the difference)
                    for i in range(prime * prime, _maxNum + 1, prime):
                        _isPrime[i] = False

            # Now we create a prime integer list from the values that are true in _isPrime
            # boolean list. 
            _primes = [num for num in _rangeValues if _isPrime[num]]

            # Return the set of primes if it's not empty; otherwise, return the default message
            return _primes if _primes else "No Prime Values present in the range"

        except Exception as e:
            # Here we handle any other exception that may occur. We print a 
            # general message and the exception thrown for details.
            return f"An error occurred during Sieve of Eratosthenes: {e}"