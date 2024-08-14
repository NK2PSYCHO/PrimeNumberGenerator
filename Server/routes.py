from flask import Blueprint, render_template, request, redirect, url_for, session
from Client.RangeGenerator import RangeGenerator
from Client.PrimeAlgorithms import PrimeAlgorithms

bluePrint = Blueprint('main', __name__)

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

    if algorithm == "Trial Division":
        prime_numbers = PrimeAlgorithms.trialDivision(range_tuple)
    elif algorithm == "E. Trial Division":
        prime_numbers = PrimeAlgorithms.enhancedTrialDivision(range_tuple)
    elif algorithm == "Sieve of Eratosthenes":
        prime_numbers = PrimeAlgorithms.eratosthenesSieve(range_tuple)
    else:
        prime_numbers = []

    range_result = RangeGenerator.generateRange(range_tuple)

    if isinstance(range_result, set):
        range_result = list(range_result)

    session['prime_numbers'] = prime_numbers
    session['algorithm'] = algorithm

    return redirect(url_for('main.generatedPrimeNumbers'))

@bluePrint.route('/api/generatedPrimeNumbers', methods=['GET'])
def generatedPrimeNumbers():
    range_result = session.get('range_result', 'No result')
    prime_numbers = session.get('prime_numbers', 'No result')
    algorithm = session.get('algorithm', 'No algorithm selected')
    return render_template('index.html', algorithm=algorithm, range_result=range_result, prime_numbers=prime_numbers)