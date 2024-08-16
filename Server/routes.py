# Import SQLite library for database operations
import sqlite3

# Import requests library for making HTTP requests  
import requests

# Import necessary Flask components  
from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify  

# Import RangeGenerator from Client module
from Client.RangeGenerator import RangeGenerator  

# Import PrimeAlgorithms from Client module
from Client.PrimeAlgorithms import PrimeAlgorithms  

# Import time library for measuring elapsed time
import time 

# Import datetime for timestamp
from datetime import datetime  

# Create a Blueprint named 'main' for organizing routes
bluePrint = Blueprint('main', __name__)

# Function to insert an operation record into the SQLite database
def insert_operation(algorithm, number_range, prime_numbers, prime_count, timestamp, time_elapsed):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('operations.db')  
        # Create a cursor object to interact with the database
        cursor = conn.cursor()  
        # SQL query to insert a record into the Operations table
        insert_query = '''
        INSERT INTO Operations (algorithm, number_range, prime_numbers, prime_count, timestamp, time_elapsed)
        VALUES (?, ?, ?, ?, ?, ?);
        '''  
        # Execute the query
        cursor.execute(insert_query, (algorithm, number_range, prime_numbers, prime_count, timestamp, time_elapsed)) 
        # Commit the transaction to save changes
        conn.commit()  
    except sqlite3.Error as e:
        # Print the error if one occurs
        print(f"An error occurred: {e}")  
    finally:
        # Ensure the database connection is closed
        conn.close()  

# Route to render the home page with available algorithms
@bluePrint.route('/', methods=['GET'])
def home():
    try:
        # List of algorithms
        algorithms = ["Trial Division", "E. Trial Division", "Sieve of Eratosthenes"]  
        # Render the home page template
        return render_template('home.html', algorithms=algorithms)  
    except Exception as e:
        # Print the error if one occurs
        print(f"An error occurred while rendering the home page: {e}")  

# Route to handle prime number generation and store operation details
@bluePrint.route('/api/generatePrimeNumbers', methods=['POST'])
def generatePrimeNumbers():
    try:
        # Get the start value from the form
        start = request.form.get('start')  
        # Get the end value from the form
        end = request.form.get('end')  
        # Get the selected algorithm from the form
        algorithm = request.form.get('algorithm')  

        try:
            # Convert start to integer
            start = int(start)  
            # Convert end to integer
            end = int(end)  

            # Validate that start and end values are non-negative integers
            if start < 0 or end < 0:
                raise ValueError("Start and end values must be non-negative integers.")
            
        except ValueError as e:
            # Redirect with error message
            return redirect(url_for('main.home', message=f"Invalid input: {e}"))  

        # Create a sorted tuple of the range
        range_tuple = tuple(sorted((start, end)))  
        # Generate the range using RangeGenerator
        range_result = RangeGenerator.generateRange(range_tuple)  
        # Convert set to list if necessary
        if isinstance(range_result, set):
            range_result = list(range_result)  

        # Store range result in session
        session['range_result'] = range_result  
        # Store selected algorithm in session
        session['algorithm'] = algorithm  

        # Record the start time
        start_time = time.time()  
        # Get the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
        # Store timestamp in session
        session['timestamp'] = timestamp  

        # Determine the API URL based on the selected algorithm
        api_url = None
        if algorithm == "Trial Division":
            api_url = url_for('main.trialDivision', _external=True)  
        elif algorithm == "E. Trial Division":
            api_url = url_for('main.enhancedTrialDivision', _external=True)  
        elif algorithm == "Sieve of Eratosthenes":
            api_url = url_for('main.eratosthenesSieve', _external=True)  

        # Make a POST request to the selected API
        if api_url:
            try:
                response = requests.post(api_url, json={"start": start, "end": end})  
                if response.status_code == 200:
                    # Get the list of prime numbers from the response
                    prime_numbers = response.json()  
                    # Count the number of primes
                    prime_count = len(prime_numbers)  
                    # Store prime numbers in session
                    session['prime_numbers'] = prime_numbers  
                else:
                    # Empty list if response is not successful
                    prime_numbers = []  
                    # Count of primes is zero
                    prime_count = 0  
                    # Store empty list in session
                    session['prime_numbers'] = []  
            except requests.RequestException as e:
                # Print the error if one occurs
                print(f"An error occurred with the API request: {e}")  
                # Default to empty list
                prime_numbers = []  
                # Default to zero
                prime_count = 0  
                # Store empty list in session
                session['prime_numbers'] = []  
        else:
            # Default to empty list if no valid API URL
            prime_numbers = []  
            # Default to zero
            prime_count = 0  
            # Store empty list in session
            session['prime_numbers'] = []  

        # Record the end time
        end_time = time.time()  
        # Calculate the elapsed time
        time_elapsed = end_time - start_time  
        # Store elapsed time in session
        session['time_elapsed'] = time_elapsed  

        # Insert operation record into the database
        insert_operation(algorithm, f"{start}-{end}", str(prime_numbers), prime_count, timestamp, time_elapsed)  

        # Redirect to the generatedPrimeNumbers route
        return redirect(url_for('main.generatedPrimeNumbers'))  
    except Exception as e:
        # Print the error if one occurs
        print(f"An error occurred during prime number generation: {e}")  
        # Redirect to home page on error
        return redirect(url_for('main.home'))  


# Route to render the results page with generated prime numbers and operation details
@bluePrint.route('/api/generatedPrimeNumbers', methods=['GET'])
def generatedPrimeNumbers():
    try:
        # Get the range result from session or default to 'No result'
        range_result = session.get('range_result', 'No result')  
        # Get the prime numbers from session or default to 'No result'
        prime_numbers = session.get('prime_numbers', 'No result')  
        # Get the selected algorithm from session or default to 'No algorithm selected'
        algorithm = session.get('algorithm', 'No algorithm selected')  
        # Get the timestamp from session or default to 'No timestamp'
        timestamp = session.get('timestamp', 'No timestamp')  
        # Get the elapsed time from session or default to 'Not calculated'
        time_elapsed = session.get('time_elapsed', 'Not calculated')  

        # Render the index page with results
        return render_template('index.html', 
                               range_result=range_result, 
                               prime_numbers=prime_numbers, 
                               algorithm=algorithm,
                               timestamp=timestamp,
                               time_elapsed=time_elapsed)  
    except Exception as e:
        # Print the error if one occurs
        print(f"An error occurred while rendering the results page: {e}")  
        # Redirect to home page on error
        return redirect(url_for('main.home'))  


# Route to handle requests for the Trial Division algorithm
@bluePrint.route('/api/trialDivision', methods=['POST'])
def trialDivision():
    try:
        # Get the start value from the request
        start = request.json.get('start')  
        # Get the end value from the request
        end = request.json.get('end')  
        # Create a sorted tuple of the range
        range_tuple = tuple(sorted((start, end)))  
        # Get prime numbers using the trialDivision algorithm
        prime_numbers = PrimeAlgorithms.trialDivision(range_tuple)  

        # Check if the result is an error message
        if isinstance(prime_numbers, str):  
            # Return the error message
            return jsonify({"error": prime_numbers})  
        # Return the prime numbers as a JSON response
        return jsonify(prime_numbers)  
    except Exception as e:
        # Print the error if one occurs
        print(f"An error occurred in the trialDivision API: {e}")  
        # Return a generic error message
        return jsonify({"error": "An error occurred while processing the request."})  


# Route to handle requests for the Enhanced Trial Division algorithm
@bluePrint.route('/api/enhancedTrialDivision', methods=['POST'])
def enhancedTrialDivision():
    try:
        # Get the start value from the request
        start = request.json.get('start')  
        # Get the end value from the request
        end = request.json.get('end')  
        # Create a sorted tuple of the range
        range_tuple = tuple(sorted((start, end)))  
        # Get prime numbers using the enhancedTrialDivision algorithm
        prime_numbers = PrimeAlgorithms.enhancedTrialDivision(range_tuple)  

        # Check if the result is an error message
        if isinstance(prime_numbers, str):  
            # Return the error message
            return jsonify({"error": prime_numbers})  
        # Return the prime numbers as a JSON response
        return jsonify(prime_numbers)  
    except Exception as e:
        # Print the error if one occurs
        print(f"An error occurred in the enhancedTrialDivision API: {e}")  
        # Return a generic error message
        return jsonify({"error": "An error occurred while processing the request."})  


# Route to handle requests for the Sieve of Eratosthenes algorithm
@bluePrint.route('/api/eratosthenesSieve', methods=['POST'])
def eratosthenesSieve():
    try:
        # Get the start value from the request
        start = request.json.get('start')  
        # Get the end value from the request
        end = request.json.get('end')  
        # Create a sorted tuple of the range
        range_tuple = tuple(sorted((start, end)))  
        # Get prime numbers using the eratosthenesSieve algorithm
        prime_numbers = PrimeAlgorithms.eratosthenesSieve(range_tuple)  

        # Check if the result is an error message
        if isinstance(prime_numbers, str):  
            # Return the error message
            return jsonify({"error": prime_numbers})  
        # Return the prime numbers as a JSON response
        return jsonify(prime_numbers)  
    except Exception as e:
        # Print the error if one occurs
        print(f"An error occurred in the eratosthenesSieve API: {e}")  
        # Return a generic error message
        return jsonify({"error": "An error occurred while processing the request."})  


# Route to return the content of the Operations table as a JSON response
@bluePrint.route('/api/getOperations', methods=['GET'])
def getOperations():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('operations.db')  
        # Create a cursor object to interact with the database
        cursor = conn.cursor()  
        # Execute a query to select all records from the Operations table
        cursor.execute("SELECT * FROM Operations")  
        # Fetch all rows from the result
        rows = cursor.fetchall()  
        # Close the database connection
        conn.close()  
        # Return the rows as a JSON response
        return jsonify(rows)  
    except sqlite3.Error as e:
        # Print the error if one occurs
        print(f"An error occurred with the database operation: {e}")  
        # Return the error as a JSON response
        return jsonify({"error": str(e)})  

# Route to render the values page to display the content of the Operations table
@bluePrint.route('/values', methods=['GET'])
def values():
    try:
        # Render the values page template
        return render_template('values.html')  
    except Exception as e:
        # Print the error if one occurs
        print(f"An error occurred while rendering the values page: {e}")  
        # Redirect to home page on error
        return redirect(url_for('main.home'))  
