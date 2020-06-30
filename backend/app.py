from flask import Flask, make_response, request

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username == "user" and password == "pass":
        return make_response("success", 200)
    else:
        return make_response("failure", 401)


@app.route('/games', methods=['GET'])
def games():
    with open("./games.json") as file:
        response_text = file.read()
    return make_response(response_text, 200)


if __name__ == '__main__':
    app.run()
