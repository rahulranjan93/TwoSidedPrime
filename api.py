from flask import Flask,jsonify
import sys
from function import twoSidedPrime

app = Flask(__name__)

@app.route('/<int:id>')
def is_two_sided_prime(id):
    return jsonify({"twoSidedPrime":twoSidedPrime(id)})

if __name__ == "__main__":
    app.run(debug=True)