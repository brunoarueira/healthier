from flask import Flask
from app.apis.status import mod as statusModule
import os

app = Flask(__name__)

app.register_blueprint(statusModule)


if __name__ == "__main__":
    debug = os.environ["FLASK_ENV"] == "development"

    app.run(debug=debug)
