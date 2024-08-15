import sqlite3
import requests
from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from Client.RangeGenerator import RangeGenerator
from Client.PrimeAlgorithms import PrimeAlgorithms
import time
from datetime import datetime

bluePrint = Blueprint('main', __name__)

def insert_operation(algorithm, number_range, prime_numbers, prime_count, timestamp, time_elapsed):
    conn = sqlite3.connect('operations.db')
    cursor = conn.cursor()
    insert_query = '''
    INSERT INTO Operations (algorithm, number_range, prime_numbers, prime_count, timestamp, time_elapsed)
    VALUES (?, ?, ?, ?, ?, ?);
    '''
    cursor.execute(insert_query, (algorithm, number_range, prime_numbers, prime_count, timestamp, time_elapsed))
    conn.commit()
    conn.close()

@bluePrint.route('/', methods=['GET'])
def home():
    algorithms = ["Trial Division", "E. Trial Division", "Sieve of Eratosthenes"]
    return render_template('home.html', algorithms=algorithms)

@bluePrint.route('/api/generatePrimeNumbers', methods=['POST'])
def generatePrimeNumbers():
    start = request.form.get('start')
    end = request.form.get('end')
    algorithm = request.form.get('algorithm')

    try:
        start = int(start)
        end = int(end)
    except ValueError:
        return redirect(url_for('main.home', message="Invalid input. Please enter valid integers."))

    range_tuple = tuple(sorted((start, end)))
    range_result = RangeGenerator.generateRange(range_tuple)
    if isinstance(range_result, set):
        range_result = list(range_result)
    
    session['range_result'] = range_result
    session['algorithm'] = algorithm

    start_time = time.time()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    session['timestamp'] = timestamp

    api_url = None
    if algorithm == "Trial Division":
        api_url = url_for('main.trialDivision', _external=True)
    elif algorithm == "E. Trial Division":
        api_url = url_for('main.enhancedTrialDivision', _external=True)
    elif algorithm == "Sieve of Eratosthenes":
        api_url = url_for('main.eratosthenesSieve', _external=True)

    if api_url:
        response = requests.post(api_url, json={"start": start, "end": end})
        if response.status_code == 200:
            prime_numbers = response.json()
            prime_count = len(prime_numbers)
            session['prime_numbers'] = prime_numbers
        else:
            prime_numbers = []
            prime_count = 0
            session['prime_numbers'] = []
    else:
        prime_numbers = []
        prime_count = 0
        session['prime_numbers'] = []

    end_time = time.time()
    time_elapsed = end_time - start_time
    session['time_elapsed'] = time_elapsed

    insert_operation(algorithm, f"{start}-{end}", str(prime_numbers), prime_count, timestamp, time_elapsed)

    return redirect(url_for('main.generatedPrimeNumbers'))

@bluePrint.route('/api/generatedPrimeNumbers', methods=['GET'])
def generatedPrimeNumbers():
    range_result = session.get('range_result', 'No result')
    prime_numbers = session.get('prime_numbers', 'No result')
    algorithm = session.get('algorithm', 'No algorithm selected')
    timestamp = session.get('timestamp', 'No timestamp')
    time_elapsed = session.get('time_elapsed', 'Not calculated')

    return render_template('index.html', 
                           range_result=range_result, 
                           prime_numbers=prime_numbers, 
                           algorithm=algorithm,
                           timestamp=timestamp,
                           time_elapsed=time_elapsed)

@bluePrint.route('/api/trialDivision', methods=['POST'])
def trialDivision():
    start = request.json.get('start')
    end = request.json.get('end')
    range_tuple = tuple(sorted((start, end)))
    prime_numbers = PrimeAlgorithms.trialDivision(range_tuple)
    return jsonify(prime_numbers)

@bluePrint.route('/api/enhancedTrialDivision', methods=['POST'])
def enhancedTrialDivision():
    start = request.json.get('start')
    end = request.json.get('end')
    range_tuple = tuple(sorted((start, end)))
    prime_numbers = PrimeAlgorithms.enhancedTrialDivision(range_tuple)
    return jsonify(prime_numbers)

@bluePrint.route('/api/eratosthenesSieve', methods=['POST'])
def eratosthenesSieve():
    start = request.json.get('start')
    end = request.json.get('end')
    range_tuple = tuple(sorted((start, end)))
    prime_numbers = PrimeAlgorithms.eratosthenesSieve(range_tuple)
    return jsonify(prime_numbers)

@bluePrint.route('/api/getOperations', methods=['GET'])
def getOperations():
    try:
        conn = sqlite3.connect('operations.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Operations")
        rows = cursor.fetchall()
        conn.close()
        return jsonify(rows)
    except sqlite3.Error as e:
        return jsonify({"error": str(e)})
    
@bluePrint.route('/values', methods=['GET'])
def values():
    return render_template('values.html')