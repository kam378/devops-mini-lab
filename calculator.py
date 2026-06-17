from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/calculate/area', methods=['GET'])
def area():
    # Get width and height from the URL parameters (e.g., ?width=5&height=4)
    width = float(request.args.get('width', 0))
    height = float(request.args.get('height', 0))
    return jsonify({"result": width * height})

@app.route('/calculate/subtract', methods=['GET'])
def subtract():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify({"result": a - b})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)