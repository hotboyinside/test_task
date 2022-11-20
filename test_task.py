from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello_func():
    name = request.args.get('name')
    message = request.args.get('message')
    return f'Hello {name}! {message}!'


if __name__ == "__main__":
    app.run(debug=True)