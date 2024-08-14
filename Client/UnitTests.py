# unittest is the module provided by python which we can use to create
# unit tests.
import unittest

# This is an in memory file like object which we will use to capture the output from
# sys so that it can be compared in the tests.
from io import StringIO

# Patch as the name suggests patches the current method or class object with temporary
# mock object. (We can mock the method or class without accessing it promoting isolation)
from unittest.mock import patch

# InputValidator is imported to write unit tests for all methods in this class.
from Client.InputValidator import InputValidator

# UserInput is imported to write unit test for public set and get methods.
from Client.UserInput import UserInput

# PrimeAlgorithms is imported to write unit tests for all methods in this class.
from Client.PrimeAlgorithms import PrimeAlgorithms

# PrimeAlgorithms is imported to write unit tests for all methods in this class.
from Client.RangeGenerator import RangeGenerator

# PrimeAlgorithms is imported to write unit tests for all methods in this class.
from Client.PrimeNumberGenerator import PrimeNumberGenerator

# This class contains test cases related to InputValidator
class TestInputValidator(unittest.TestCase):

    # Test case for valideRangeInput when a valid input is given.
    def test_validRangeInput(self):
        with patch('builtins.input', return_value='10'):
            # Mock user input as 10
            result = InputValidator.validateRangeInput("Enter a number: ")
            # Assert that the returned value is 10
            self.assertEqual(result, 10)

    # Test case for valideRangeInput when a non-integer input is given.
    def test_nonIntegerRangeInput(self):
        with patch('builtins.input', side_effect=['abc', '10']), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Mock user input as abc first, then 10
            result = InputValidator.validateRangeInput("Enter a number: ")
            # Assert that the returned value is 10
            self.assertEqual(result, 10)
            # Assert that the output contains the error message for invalid input
            self.assertIn("Invalid input. Please enter a valid integer.", mock_stdout.getvalue())

    # Test case for valideRangeInput when a negative integer input is given.
    def test_negativeIntegerRangeInput(self):
        with patch('builtins.input', side_effect=['-10', '10']), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Mock user input as -10 first, then 10
            result = InputValidator.validateRangeInput("Enter a number: ")
            # Assert that the returned value is 10
            self.assertEqual(result, 10)
            # Assert that the output contains the error message for non-negative input
            self.assertIn("The value must be non-negative. Please try again.", mock_stdout.getvalue())

    # Test case for valideMenuInput when a valid input is given.
    def test_validMenuInput(self):
        with patch('builtins.input', return_value='2'):
            # Mock user input as 2
            result = InputValidator.validateMenuInput("Choose:", ["Option 1", "Option 2", "Option 3"])
            # Assert that the returned value is 2
            self.assertEqual(result, 2)

    # Test case for valideMenuInput when a non-integfer input is given.
    def test_nonIntegerMenuInput(self):
        with patch('builtins.input', side_effect=['abc', '2']), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Mock user input as abc first, then 2
            result = InputValidator.validateMenuInput("Choose:", ["Option 1", "Option 2", "Option 3"])
            # Assert that the returned value is 2
            self.assertEqual(result, 2)
            # Assert that the output contains the error message for invalid input
            self.assertIn("Invalid input. Please enter a valid integer.", mock_stdout.getvalue())

    # Test case for valideMenuInput when an out of range input is given.
    def test_nonOptionMenuInput(self):
        with patch('builtins.input', side_effect=['4', '2']), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Mock user input as 4 first, then 2
            result = InputValidator.validateMenuInput("Choose:", ["Option 1", "Option 2", "Option 3"])
            # Assert that the returned value is 2
            self.assertEqual(result, 2)
            # Assert that the output contains the error message for out-of-range input
            self.assertIn("The value must be in the range of 1 to 3.", mock_stdout.getvalue())

# This class contains test cases related to RangeGenerator
class TestRangeGenerator(unittest.TestCase):

    # Test range generation for a valid range
    def test_generateRange(self):
        # Generate a range set from (1, 5)
        result = RangeGenerator.generateRange((1, 5))
        # Assert that the result is the set {1, 2, 3, 4, 5}
        self.assertEqual(result, {1, 2, 3, 4, 5})

    # Test range generation with incomplete input
    def test_incompleteSetGenerateRange(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Attempt to generate a range set with a single value (5,)
            result = RangeGenerator.generateRange((5,))
            # Assert that the result is an empty set
            self.assertEqual(result, set())  
            # Assert that the output contains the error message for not enough values to unpack
            self.assertIn("not enough values to unpack", mock_stdout.getvalue())

    # Test range generation with invalid type input
    def test_invalidTypeGenerateRange(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Attempt to generate a range set with an invalid type (1, "abc")
            RangeGenerator.generateRange((1,"abc"))
            # Assert that the output contains the error message for invalid input types
            self.assertIn("Invalid input: rangeSet must be a tuple or list.", mock_stdout.getvalue())

    # Test range generation with too many values input
    def test_tooManyValuesGenerateRange(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Attempt to generate a range set with too many values (1, "abc", "cba")
            RangeGenerator.generateRange((1,"abc","cba"))
            # Assert that the output contains the error message for too many values to unpack
            self.assertIn("too many values to unpack", mock_stdout.getvalue())

# This class contains test cases related to PrimeAlgorithms
class TestPrimeAlgorithms(unittest.TestCase):

    # Test trialDivision method with a valid range
    def test_trialDivision(self):
        with patch.object(RangeGenerator, 'generateRange', return_value={2, 3, 4, 5, 6}):
            # Mock the generateRange method to return {2, 3, 4, 5, 6}
            result = PrimeAlgorithms.trialDivision((2, 6))
            # Assert that the result is the list [2, 3, 5]
            self.assertEqual(result, [2, 3, 5])

    # Test trialDivision method with no primes in the range
    def test_noPrimeTrialDivision(self):
        with patch.object(RangeGenerator, 'generateRange', return_value={24,25,26,27,28}):
            # Mock the generateRange method to return {24, 25, 26, 27, 28}
            result = PrimeAlgorithms.trialDivision((24,28))
            # Assert that the result is the message "No Prime Values present in the range"
            self.assertEqual(result,"No Prime Values present in the range")

    # Test trialDivision method with an exception in the range
    def test_exceptionTrialDivision(self):
        with patch.object(RangeGenerator, 'generateRange', return_value={24,"abc",26,27,28}):
            # Mock the generateRange method to return {24, "abc", 26, 27, 28}
            result = PrimeAlgorithms.trialDivision(())
            # Assert that the result contains the error message for trial division exception
            self.assertIn("An error occurred during trial division", result)

    # Test enhancedTrialDivision method with a valid range
    def test_enhancedTrialDivision(self):
        with patch.object(RangeGenerator, 'generateRange', return_value={2, 3, 4, 5, 6, 7, 11, 13, 15}):
            # Mock the generateRange method to return {2, 3, 4, 5, 6, 7, 11, 13, 15}
            result = PrimeAlgorithms.enhancedTrialDivision((2, 15))
            # Assert that the result is the list [2, 3, 5, 7, 11, 13]
            self.assertEqual(result, [2, 3, 5, 7, 11, 13])

    # Test enhancedTrialDivision method with no primes in the range
    def test_noPrimeEnhancedTrialDivision(self):
        with patch.object(RangeGenerator, 'generateRange', return_value={74,75,76,77,78}):
            # Mock the generateRange method to return {74, 75, 76, 77, 78}
            result = PrimeAlgorithms.enhancedTrialDivision((74, 78))
            # Assert that the result is the message "No Prime Values present in the range"
            self.assertEqual(result,"No Prime Values present in the range")

    # Test enhancedTrialDivision method with an exception in the range
    def test_exceptionEnhancedTrialDivision(self):
        with patch.object(RangeGenerator, 'generateRange', return_value={74,75,"76.5",77,78}):
            # Mock the generateRange method to return {74, 75, "76.5", 77, 78}
            result = PrimeAlgorithms.enhancedTrialDivision((74, 78))
            # Assert that the result contains the error message for enhanced trial division exception
            self.assertIn("An error occurred during enhanced trial division", result)

    # Test eratosthenesSieve method with a valid range
    def test_eratosthenesSieve(self):
        with patch.object(RangeGenerator, 'generateRange', return_value={10, 11, 12, 13, 14, 15, 16, 17, 18, 19}):
            # Mock the generateRange method to return {10, 11, 12, 13, 14, 15, 16, 17, 18, 19}
            result = PrimeAlgorithms.eratosthenesSieve((10, 19))
            # Assert that the result is the list [11, 13, 17, 19]
            self.assertEqual(result, [11, 13, 17, 19])

    # Test eratosthenesSieve method with no primes in the range
    def test_noPrimeEratosthenesSieve(self):
        with patch.object(RangeGenerator, 'generateRange', return_value={62, 63, 64, 65, 66}):
            # Mock the generateRange method to return {62, 63, 64, 65, 66}
            result = PrimeAlgorithms.eratosthenesSieve((62, 66))
            # Assert that the result is the message "No Prime Values present in the range"
            self.assertEqual(result,"No Prime Values present in the range")

    # Test eratosthenesSieve method with an exception in the range
    def test_exceptionEratosthenesSieve(self):
        with patch.object(RangeGenerator, 'generateRange', return_value={62, 63, 64, 65, "66"}):
            # Mock the generateRange method to return {62, 63, 64, 65, "66"}
            result = PrimeAlgorithms.eratosthenesSieve((62, 66))
            # Assert that the result contains the error message for sieve exception
            self.assertIn("An error occurred during Sieve of Eratosthenes", result)

# This class contains test cases related to TestUserInput
class TestUserInput(unittest.TestCase):
    
    # Test setting and getting user input in UserInput
    def test_setAndGetUserInput(self):
        user_input = UserInput()
        with patch('builtins.input', side_effect=['2', '10', '20']):
            # Mock user input as 2, 10, 20
            user_input.setUserInput()
            # Retrieve the algorithm choice and range set from the user input
            algo, range_set = user_input.getUserInput()
            # Assert that the algorithm choice is 2
            self.assertEqual(algo, 2)
            # Assert that the range set is [10, 20]
            self.assertEqual(range_set, [10, 20])

# This class contains test cases related to PrimeNumberGenerator
class TestPrimeNumberGenerator(unittest.TestCase):

    # Test the main method in PrimeNumberGenerator
    def test_PrimeNumberGenerator_main(self):
        with patch.object(UserInput, 'setUserInput'):
            # Mock the setUserInput method
            with patch.object(UserInput, 'getUserInput', return_value=(3, (10, 20))):
                # Mock the getUserInput method to return (3, (10, 20))
                with patch.object(PrimeAlgorithms, 'eratosthenesSieve', return_value=[11, 13, 17, 19]):
                    # Mock the eratosthenesSieve method to return {11, 13, 17, 19}
                    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                        # Capture the output of the main method
                        PrimeNumberGenerator.main()
                        # Assert that the output contains the correct prime numbers
                        self.assertIn("Prime numbers in the range are: [11, 13, 17, 19]", mock_stdout.getvalue())

# Check if the script is being run directly (not imported)
if __name__ == '__main__':
    # Run the unit tests
    unittest.main()
