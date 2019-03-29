from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

users = []

@app.route('/', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data['name']
    email = data['email-address']
    password = data['password']

    payload = {
        'name': name,
        'email': email,
        'password': password
    }

    users.append(payload)

    return make_response(jsonify({
        'User': payload,
        'Message': 'User added successfully'
    }), 201)

if __name__ == '__main__':
    app.run(debug=True)