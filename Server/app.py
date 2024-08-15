# Import the Flask class from the flask module to create the app instance.
from flask import Flask  

# Import the Blueprint object (routes) from the Server module.
from Server.routes import bluePrint  

# Import the config module where your configuration settings are defined.
import Server.config  

# Create an instance of the Flask class, which represents your web application.
app = Flask(__name__)  

try:
    # Load configuration settings from the Config class in the config module.
    app.config.from_object(Server.config.Config)  
except Exception as e:
    # Print an error message if loading configuration fails.
    print(f"Error loading configuration: {e}")

try:
    # Register the Blueprint (bluePrint) with the Flask application.
    app.register_blueprint(bluePrint)  
except Exception as e:
    # Print an error message if registering the blueprint fails.
    print(f"Error registering blueprint: {e}")

# Check if this script is being run directly (not imported as a module).
if __name__ == '__main__':  
    try:
        # Start the Flask development server.
        app.run()  
    except Exception as e:
        # Print an error message if starting the server fails.
        print(f"Error starting the Flask server: {e}")
