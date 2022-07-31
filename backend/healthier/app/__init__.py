from flask import Flask
from app.apis.status import mod as statusModule

app = Flask(__name__)

app.register_blueprint(statusModule)


if __name__ == "__main__":
    app.run(debug=True)
