from flask import Flask
from Server.routes import bluePrint
import Server.config

app = Flask(__name__)

app.config.from_object(Server.config.Config)

app.register_blueprint(bluePrint)

if __name__ == '__main__':
    app.run(debug=True)
