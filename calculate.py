import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'ok'

@app.route('/health')
def health():
    return "3RR TO LVE"


@app.route('/calculate/<value_one>/<operation>/<value_two>')
def calculate(value_one, operation, value_two):
    value_one = int(value_one)
    value_two = int(value_two)
    if operation == "sum":
        result = value_one + value_two
    elif operation == "sub":
        result = value_one - value_two
    elif operation == "mult":
        result = value_one * value_two
    elif operation == "div":
        result = value_one / value_two
    else:
        raise ValueError("Invalid operation %s" % (operation))

    return result



