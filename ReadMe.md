# Prime Number Generator Project

## Overview

The Prime Number Generator Project is a comprehensive Python-based application designed to generate prime numbers within a specified range using various algorithms. The project is divided into two main modules: **Client** and **Server**. The **Client** module provides a command-line interface (CLI) for prime number generation, while the **Server** module offers a Flask-based web interface and RESTful API for the same purpose. This modular design ensures flexibility, easy testing, and scalability.

## Project Structure

```
PrimeNumberGenerator/
├── Client/
│   ├── __init__.py
│   ├── InputValidator.py
│   ├── PrimeAlgorithms.py
│   ├── PrimeNumberGenerator.py
│   ├── RangeGenerator.py
│   ├── UserInput.py
│   ├── UnitTests.py
│   ├── __pycache__/
│   └── ReadMe.md
├── Server/
│   ├── app.py
│   ├── config.py
│   ├── routes.py
│   ├── __init__.py
│   ├── templates/
│   │   ├── home.html
│   │   ├── index.html
│   │   └── values.html
│   ├── __pycache__/
│   └── ReadMe.md
├── operations.db
├── requirements.txt
└── __init__.py
```

### Module Breakdown

1. **Client Module**:
   - **`InputValidator.py`**: Validates user input for correctness, including numerical ranges and menu options.
   - **`UserInput.py`**: Handles the process of collecting and validating user inputs, storing the range and algorithm choice for prime number generation.
   - **`PrimeAlgorithms.py`**: Implements three different algorithms for generating prime numbers: Trial Division, Enhanced Trial Division, and Sieve of Eratosthenes.
   - **`RangeGenerator.py`**: Generates a set of integers representing the range for prime number search.
   - **`PrimeNumberGenerator.py`**: The main script for the command-line interface (CLI) that ties all components together and outputs prime numbers.
   - **`UnitTests.py`**: Contains unit tests for validating the functionality of the entire application.
   - **`ReadMe.md`**: Documentation specific to the Client module.

2. **Server Module**:
   - **`app.py`**: The entry point for running the Flask web application, initializing the server.
   - **`config.py`**: Configuration settings for the Flask application.
   - **`routes.py`**: Defines the HTTP routes and API endpoints, handling requests and calling the appropriate prime number generation algorithm.
   - **Templates**:
     - **`home.html`**: The main interface where users can input the range and select an algorithm.
     - **`index.html`**: Displays the results of the prime number generation.
     - **`values.html`**: A supplementary template for additional data display (optional).
   - **`ReadMe.md`**: Documentation specific to the Server module.

3. **`operations.db`**: SQLite database file for logging operations, such as the selected algorithm, the time elapsed, and the number range.

4. **`requirements.txt`**: Lists the dependencies required for the project.

5. **`__init__.py`**: Initializes the modules as Python packages.

## How to Run the Project

### Prerequisites

- Python 3.x installed on your system.
- Flask installed via `pip` for the Server module.

### Step 1: Clone the Repository

If you haven't already, clone the repository to your local machine:

```bash
git clone <your-repository-url>
cd PrimeNumberGenerator
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  
```

### Step 3: Install Dependencies

Install the required packages using `pip`:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Client Module

To use the command-line interface for prime number generation:

```bash
python -m Client.PrimeNumberGenerator
```

### Step 5: Run the Server Module

To start the Flask web application:

```bash
python -m Server.app
```

Open a web browser and navigate to `http://127.0.0.1:5000/` to access the application.

### Running Unit Tests

To run the unit tests for the entire project:

```bash
python -m unittest Client.UnitTests 
```

## Conclusion

The Prime Number Generator Project provides a versatile tool for generating prime numbers, with both CLI and web interfaces. Its modular structure allows for easy maintenance and expansion, making it a powerful resource for both developers and users interested in prime number generation.