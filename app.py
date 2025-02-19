from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the API!"

@app.route('/add', methods=['GET'])
def add():
    """API to add two numbers."""

    # Get 'a' and 'b' parameters from request
    a = request.args.get('a')
    b = request.args.get('b')

    # Check if either parameter is missing
    if a is None or b is None:
        return jsonify(error="Both 'a' and 'b' parameters are required"), 400

    try:
        # Convert parameters to integers
        a = int(a)
        b = int(b)
    except ValueError:
        return jsonify(error="Both parameters must be integers"), 400

    # Perform addition and return result
    return jsonify(result=a + b)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
