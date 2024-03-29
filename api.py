import datetime
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from freedbmysql import addGreeting, clearGreeting, getAllGreeting

app = Flask(__name__)
CORS(app)
        

@app.route('/', methods=['GET'])
def index():
    # return html from the static folder
    return app.send_static_file('index.html')

@app.route('/all_greetings', methods=['GET'])
def all_greetings():
    result = getAllGreeting()
    return jsonify(result)

@app.route('/add_greeting', methods=['POST', 'GET'])
def add_greeting():
    text = request.args.get('greeting')
    name = request.args.get('name')
    result = addGreeting(name, text)
    return jsonify(result)

@app.route('/clear_greetings', methods=['GET'])
def clear():
    data = clearGreeting()
    return "<h1> Data Cleared </h1>"


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)