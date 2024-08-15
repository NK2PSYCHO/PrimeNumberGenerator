import sqlite3  # Import SQLite library for database operations
import requests  # Import requests library for making HTTP requests
from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify  # Import necessary Flask components
from Client.RangeGenerator import RangeGenerator  # Import RangeGenerator from Client module
from Client.PrimeAlgorithms import PrimeAlgorithms  # Import PrimeAlgorithms from Client module
import time  # Import time library for measuring elapsed time
from datetime import datetime  # Import datetime for timestamp

# Create a Blueprint named 'main' for organizing routes
bluePrint = Blueprint('main', __name__)

def insert_operation(algorithm, number_range, prime_numbers, prime_count, timestamp, time_elapsed):
    """Insert an operation record into the SQLite database."""
    try:
        conn = sqlite3.connect('operations.db')  # Connect to the SQLite database
        cursor = conn.cursor()  # Create a cursor object to interact with the database
        insert_query = '''
        INSERT INTO Operations (algorithm, number_range, prime_numbers, prime_count, timestamp, time_elapsed)
        VALUES (?, ?, ?, ?, ?, ?);
        '''  # SQL query to insert a record into the Operations table
        cursor.execute(insert_query, (algorithm, number_range, prime_numbers, prime_count, timestamp, time_elapsed))  # Execute the query
        conn.commit()  # Commit the transaction to save changes
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")  # Print the error if one occurs
    finally:
        conn.close()  # Ensure the database connection is closed

@bluePrint.route('/', methods=['GET'])
def home():
    """Render the home page with available algorithms."""
    try:
        algorithms = ["Trial Division", "E. Trial Division", "Sieve of Eratosthenes"]  # List of algorithms
        return render_template('home.html', algorithms=algorithms)  # Render the home page template
    except Exception as e:
        print(f"An error occurred while rendering the home page: {e}")  # Print the error if one occurs
        return redirect(url_for('main.home'))  # Redirect to home page on error

@bluePrint.route('/api/generatePrimeNumbers', methods=['POST'])
def generatePrimeNumbers():
    """Handle prime number generation and store operation details."""
    try:
        start = request.form.get('start')  # Get the start value from the form
        end = request.form.get('end')  # Get the end value from the form
        algorithm = request.form.get('algorithm')  # Get the selected algorithm from the form

        try:
            start = int(start)  # Convert start to integer
            end = int(end)  # Convert end to integer

            if start < 0 or end < 0:
                raise ValueError("Start and end values must be non-negative integers.")
            if start > end:
                raise ValueError("Start value cannot be greater than end value.")
        except ValueError as e:
            return redirect(url_for('main.home', message=f"Invalid input: {e}"))  # Redirect with error message

        range_tuple = tuple(sorted((start, end)))  # Create a sorted tuple of the range
        range_result = RangeGenerator.generateRange(range_tuple)  # Generate the range using RangeGenerator
        if isinstance(range_result, set):
            range_result = list(range_result)  # Convert set to list if necessary

        session['range_result'] = range_result  # Store range result in session
        session['algorithm'] = algorithm  # Store selected algorithm in session

        start_time = time.time()  # Record the start time
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get the current timestamp
        session['timestamp'] = timestamp  # Store timestamp in session

        api_url = None
        if algorithm == "Trial Division":
            api_url = url_for('main.trialDivision', _external=True)  # Get URL for trialDivision API
        elif algorithm == "E. Trial Division":
            api_url = url_for('main.enhancedTrialDivision', _external=True)  # Get URL for enhancedTrialDivision API
        elif algorithm == "Sieve of Eratosthenes":
            api_url = url_for('main.eratosthenesSieve', _external=True)  # Get URL for eratosthenesSieve API

        if api_url:
            try:
                response = requests.post(api_url, json={"start": start, "end": end})  # Make a POST request to the selected API
                if response.status_code == 200:
                    prime_numbers = response.json()  # Get the list of prime numbers from the response
                    prime_count = len(prime_numbers)  # Count the number of primes
                    session['prime_numbers'] = prime_numbers  # Store prime numbers in session
                else:
                    prime_numbers = []  # Empty list if response is not successful
                    prime_count = 0  # Count of primes is zero
                    session['prime_numbers'] = []  # Store empty list in session
            except requests.RequestException as e:
                print(f"An error occurred with the API request: {e}")  # Print the error if one occurs
                prime_numbers = []  # Default to empty list
                prime_count = 0  # Default to zero
                session['prime_numbers'] = []  # Store empty list in session
        else:
            prime_numbers = []  # Default to empty list if no valid API URL
            prime_count = 0  # Default to zero
            session['prime_numbers'] = []  # Store empty list in session

        end_time = time.time()  # Record the end time
        time_elapsed = end_time - start_time  # Calculate the elapsed time
        session['time_elapsed'] = time_elapsed  # Store elapsed time in session

        insert_operation(algorithm, f"{start}-{end}", str(prime_numbers), prime_count, timestamp, time_elapsed)  # Insert operation record into the database

        return redirect(url_for('main.generatedPrimeNumbers'))  # Redirect to the generatedPrimeNumbers route
    except Exception as e:
        print(f"An error occurred during prime number generation: {e}")  # Print the error if one occurs
        return redirect(url_for('main.home'))  # Redirect to home page on error


@bluePrint.route('/api/generatedPrimeNumbers', methods=['GET'])
def generatedPrimeNumbers():
    """Render the results page with generated prime numbers and operation details."""
    try:
        range_result = session.get('range_result', 'No result')  # Get the range result from session or default to 'No result'
        prime_numbers = session.get('prime_numbers', 'No result')  # Get the prime numbers from session or default to 'No result'
        algorithm = session.get('algorithm', 'No algorithm selected')  # Get the selected algorithm from session or default to 'No algorithm selected'
        timestamp = session.get('timestamp', 'No timestamp')  # Get the timestamp from session or default to 'No timestamp'
        time_elapsed = session.get('time_elapsed', 'Not calculated')  # Get the elapsed time from session or default to 'Not calculated'

        return render_template('index.html', 
                               range_result=range_result, 
                               prime_numbers=prime_numbers, 
                               algorithm=algorithm,
                               timestamp=timestamp,
                               time_elapsed=time_elapsed)  # Render the index page with results
    except Exception as e:
        print(f"An error occurred while rendering the results page: {e}")  # Print the error if one occurs
        return redirect(url_for('main.home'))  # Redirect to home page on error

@bluePrint.route('/api/trialDivision', methods=['POST'])
def trialDivision():
    """Handle requests for the Trial Division algorithm."""
    try:
        start = request.json.get('start')  # Get the start value from the request
        end = request.json.get('end')  # Get the end value from the request
        range_tuple = tuple(sorted((start, end)))  # Create a sorted tuple of the range
        prime_numbers = PrimeAlgorithms.trialDivision(range_tuple)  # Get prime numbers using the trialDivision algorithm
        return jsonify(prime_numbers)  # Return the prime numbers as a JSON response
    except Exception as e:
        print(f"An error occurred in the trialDivision API: {e}")  # Print the error if one occurs
        return jsonify({"error": "An error occurred while processing the request."})  # Return an error message

@bluePrint.route('/api/enhancedTrialDivision', methods=['POST'])
def enhancedTrialDivision():
    """Handle requests for the Enhanced Trial Division algorithm."""
    try:
        start = request.json.get('start')  # Get the start value from the request
        end = request.json.get('end')  # Get the end value from the request
        range_tuple = tuple(sorted((start, end)))  # Create a sorted tuple of the range
        prime_numbers = PrimeAlgorithms.enhancedTrialDivision(range_tuple)  # Get prime numbers using the enhancedTrialDivision algorithm
        return jsonify(prime_numbers)  # Return the prime numbers as a JSON response
    except Exception as e:
        print(f"An error occurred in the enhancedTrialDivision API: {e}")  # Print the error if one occurs
        return jsonify({"error": "An error occurred while processing the request."})  # Return an error message

@bluePrint.route('/api/eratosthenesSieve', methods=['POST'])
def eratosthenesSieve():
    """Handle requests for the Sieve of Eratosthenes algorithm."""
    try:
        start = request.json.get('start')  # Get the start value from the request
        end = request.json.get('end')  # Get the end value from the request
        range_tuple = tuple(sorted((start, end)))  # Create a sorted tuple of the range
        prime_numbers = PrimeAlgorithms.eratosthenesSieve(range_tuple)  # Get prime numbers using the eratosthenesSieve algorithm
        return jsonify(prime_numbers)  # Return the prime numbers as a JSON response
    except Exception as e:
        print(f"An error occurred in the eratosthenesSieve API: {e}")  # Print the error if one occurs
        return jsonify({"error": "An error occurred while processing the request."})  # Return an error message

@bluePrint.route('/api/getOperations', methods=['GET'])
def getOperations():
    """Return the content of the Operations table as a JSON response."""
    try:
        conn = sqlite3.connect('operations.db')  # Connect to the SQLite database
        cursor = conn.cursor()  # Create a cursor object to interact with the database
        cursor.execute("SELECT * FROM Operations")  # Execute a query to select all records from the Operations table
        rows = cursor.fetchall()  # Fetch all rows from the result
        conn.close()  # Close the database connection
        return jsonify(rows)  # Return the rows as a JSON response
    except sqlite3.Error as e:
        print(f"An error occurred with the database operation: {e}")  # Print the error if one occurs
        return jsonify({"error": str(e)})  # Return the error as a JSON response

@bluePrint.route('/values', methods=['GET'])
def values():
    """Render the values page to display the content of the Operations table."""
    try:
        return render_template('values.html')  # Render the values page template
    except Exception as e:
        print(f"An error occurred while rendering the values page: {e}")  # Print the error if one occurs
        return redirect(url_for('main.home'))  # Redirect to home page on error
