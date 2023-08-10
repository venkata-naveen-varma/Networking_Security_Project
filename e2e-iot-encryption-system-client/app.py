from flask import Flask, jsonify, request
import tea
app = Flask(__name__)

@app.route('/process_data', methods=['POST'])
def process_data():
    # Get the JSON object from the request body
    print('entered here', request)
    print('get_json', request.get_json)
    print('get_json', request.headers)
    # request.headers['Content-Type']='application/json'
    try:
        data = request.get_json()
        print('data: ', data)
        print('data.items', data.items)
        if not data:
            return jsonify({'error': 'Invalid JSON'}), 400
        decrypted_response = {}
        for key, value in data.items():
            if isinstance(value, str):
                decrypted_response[key] = tea.decrypt('1c2e445708f1121ef948b08cc0a3c59d', value)
            else:
                decrypted_response[key] = value
        return jsonify(decrypted_response)
    except Exception as ex:
        print(ex)
        return ex

if __name__ == '__main__':
    app.run(debug=True)