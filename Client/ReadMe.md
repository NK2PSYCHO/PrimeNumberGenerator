# Prime Number Generator

## Overview

This project is a Python-based application designed to generate prime numbers within a specified range using different algorithms. The project is modular, allowing easy testing and extension. The main components include:

- **Input Validation**: Ensures the user inputs are valid and handles error cases gracefully.
- **Prime Generation Algorithms**: Implements different methods to generate prime numbers.
- **User Interaction**: Allows users to select the algorithm and define the range for prime number generation.
- **Unit Tests**: Comprehensive tests to validate the functionality of the application.

## Project Structure

```
.
├── InputValidator.py          # Handles user input validation
├── UserInput.py               # Manages user input and interacts with InputValidator
├── PrimeAlgorithms.py         # Implements various prime number generation algorithms
├── RangeGenerator.py          # Generates a range of integers from user input
├── PrimeNumberGenerator.py    # Main script to run the prime number generator application
├── test_prime_number_generator.py  # Unit tests for the entire application
├── README.md                  # Project documentation
```

### File Explanations

1. **InputValidator.py**:  
   Contains methods to validate user inputs, ensuring they are within expected ranges and formats. It includes functions to validate both numerical ranges and menu options.

2. **UserInput.py**:  
   Manages the process of gathering user input. It uses the `InputValidator` to validate the inputs and stores the range and algorithm choice for use in the prime number generation process.

3. **PrimeAlgorithms.py**:  
   Implements three different algorithms for generating prime numbers:
   - **Trial Division**
   - **Enhanced Trial Division**
   - **Sieve of Eratosthenes**

   These algorithms are used based on the user's selection to generate prime numbers within a specified range.

4. **RangeGenerator.py**:  
   Generates a set of integers representing the range of numbers within which the prime numbers are to be found.

5. **PrimeNumberGenerator.py**:  
   The main script that ties all components together. It orchestrates user input, selects the prime generation algorithm, and displays the results.

6. **test_prime_number_generator.py**:  
   Contains unit tests for the entire application, ensuring that each component functions as expected.

## How to Run the Code

### Prerequisites

- Python 3.x installed on your system.

### Step 1: Clone the Repository

If you haven't already, clone the repository to your local machine:

```bash
git clone <your-repository-url>
cd <your-repository-directory>
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required packages using `pip`. If there's no `requirements.txt`, the dependencies are minimal and include standard Python libraries like `unittest`:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Prime Number Generator

Execute the main program:

```bash
python -m Client.PrimeNumberGenerator
```

You will be prompted to select a prime generation algorithm and input a range. The program will output the prime numbers within the specified range.

## How to Run Unit Tests

Unit tests are included to verify the functionality of each module. To run the tests:

```bash
python -m unittest Client.UnitTests 
```
