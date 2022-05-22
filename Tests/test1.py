from flask import Flask
from mongoengine import *
import names

app = Flask(__name__)

connect(host="mongodb+srv://<AgentUsr>:<Logiologio1998>@cluster0.7bqpr.mongodb.net/?retryWrites=true&w=majority/flask_example_db")

class User(Document):
    name = StringField()

@app.route("/create")
def add_user():
    new_user = User(name=names.get_full_name())
    new_user.save()
    return str(new_user.id)

@app.route("/list")
def get_user():
    return User.objects.to_json()