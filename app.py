from flask import Flask, request, json
from models import User

users = []

app = Flask('Server')


@app.errorhandler(404)
def page_not_found(e):
    data = {"Mikola": "С тебя всё-таки какао!"}
    response = app.response_class(
        response=json.dumps(data, ensure_ascii=False).encode('utf8'),
        status=404,
        mimetype='application/json',
        headers={"X-pyfin": "povtoril i zagolovok"},
    )
    return response


@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    print(data)
    user = User()
    user.name = data["name"]
    user.password = data["password"]
    if "is_admin" in data:
        user.is_admin = data.is_admin
    users.append(user)
    print(users)
    return user.name


@app.route("/users", methods=["GET"])
def user_list():
    user_names = ""
    for user in users:
        user_names += "<p>user: {0}</p>".format(user.name)
    return user_names
