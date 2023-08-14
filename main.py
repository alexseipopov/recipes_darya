from flask import Flask

app = Flask(__name__)


if __name__ == '__main__':
    app.run(port=5005, debug=True, host='0.0.0.0')
