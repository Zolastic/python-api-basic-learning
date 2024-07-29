from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<user_id>", methods=["GET"])
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com",
    }   

    extra = request.args.get('extra')
    if extra:
        user_data['extra'] = extra # add extra key to user_data dictionary if extra query parameter is provided

    return jsonify(user_data), 200 # return JSON response with status code 200

@app.route("/create-user", methods=["POST"]) # only allow POST requests. If a GET request is made, it will return 405 Method Not Allowed. If I want to allow both GET and POST requests, I can put methods=["GET", "POST"]
def create_user():
    # if request.method == "POST": # Use this if you accept different types of requests in the same route
    data = request.get_json() # get JSON data from request

    return jsonify(data), 201


if __name__ == '__main__':
    app.run(debug=True)