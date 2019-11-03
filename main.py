from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    PNumber = db.Column(db.String())
    Email = db.Column(db.String())
    Username = db.Column(db.String())
    PasswordH = db.Column(db.String())

@app.route('/', methods=["GET"])
def index():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)