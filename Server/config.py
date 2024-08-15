# Define a configuration class to store application settings.
class Config:  
    try:
        # Set a secret key for securely signing session cookies and other security-related needs.
        SECRET_KEY = 'jIub1ejbPwDEGzIZcyKmWv7mrNspPtnX'  
    except Exception as e:
        # Print an error message if there is an issue with setting the secret key.
        print(f"Error setting SECRET_KEY: {e}")
