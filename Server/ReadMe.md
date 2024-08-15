# Prime Number API with Flask

## Overview

This project is a Flask-based web application designed to generate prime numbers within a specified range using different algorithms. The application features a simple GUI and provides RESTful API endpoints for each prime number generation algorithm. The main components include:

- **Input Validation**: Ensures user inputs are valid and handles error cases gracefully.
- **Prime Generation Algorithms**: Implements different methods to generate prime numbers.
- **REST APIs**: Exposes API endpoints for each algorithm, allowing users to request prime numbers via HTTP.
- **HTML Interface**: Provides a web-based interface for users to input data and view results.
- **Database Logging**: Logs each operation with details like time elapsed, algorithm chosen, and the number range.

## Project Structure

```
.
├── app.py                 # Entry point to run the Flask application
├── config.py              # Configuration settings for the Flask app
├── __init__.py            # Initializes the Flask application
├── routes.py              # Defines routes and API endpoints for prime number generation
└── templates
    ├── home.html          # Home page with input fields and dropdown menu
    ├── index.html         # Displays the prime numbers generated
    └── values.html        # A template for additional data display (if used)
```

### File Explanations

1. **`app.py`**:  
   The main entry point for running the Flask application. It initializes the server and begins listening for incoming requests.

2. **`config.py`**:  
   Contains configuration settings for the Flask app, such as `SECRET_KEY` and other environment-specific settings.

3. **`__init__.py`**:  
   Initializes the Flask application, loads configurations from `config.py`, and sets up the application context.

4. **`routes.py`**:  
   Contains the main logic for handling HTTP requests. Defines routes for rendering the home page, handling form submissions, and calling the appropriate prime number generation algorithm. Each algorithm is exposed through a separate API endpoint.

5. **`templates/home.html`**:  
   The main interface where users input the range and select the algorithm. It includes a form with input fields and a dropdown menu.

6. **`templates/index.html`**:  
   Displays the results of the prime number generation, including the complete range, the selected algorithm, and the list of prime numbers.

7. **`templates/values.html`**:  
   An additional template that can be used to display supplementary data or information related to the prime number generation.

## How to Run the Code

### Prerequisites

- Python 3.x installed on your system.
- Flask installed via `pip`.

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

Install the required packages using `pip`:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Flask Application

Start the Flask server:

```bash
python -m Server.app
```

Open a web browser and go to `http://127.0.0.1:5000/` to access the application.

Or

Use gunicorn

```bash
gunicorn -w 4 -b 0.0.0.0:8000 Server.app:app  
```
Open a web browser and go to `http://0.0.0.0:8000` to access the application.


## How to Use the Application

1. **Select an Algorithm**:  
   Choose one of the prime generation algorithms from the dropdown menu.

2. **Input the Range**:  
   Enter the start and end values of the range within which you want to find prime numbers.

3. **Submit**:  
   Click the submit button. The results, including the selected range and prime numbers, will be displayed on the results page.

