from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def sum_numbers():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1+ num2
    return jsonify({'result': result})

def sum():
    data = request.get_json()
    try:
        return jsonify({'result': data['num1'] + data['num2']}), 200
    except KeyError:
        return jsonify({'message': "Missing properties num1 and/or num2"}), 400

if __name__ == '__main__':
    app.run(debug=True)

