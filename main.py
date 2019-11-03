from flask import Flask, request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, logout_user, LoginManager
import hashlib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = 'MUAHAHAHAHHAHAHAHAHAHAHAHAAHAH'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    PNumber = db.Column(db.String())
    Email = db.Column(db.String())
    Username = db.Column(db.String(), unique=True)
    PasswordH = db.Column(db.String())

    def __init__(self, Number, Email, Uname, Pass):
        self.PNumber = Number
        self.Email = Email
        self.Username = Uname
        self.PasswordH = str(hashlib.md5(Pass.encode()).hexdigest())


@app.route('/', methods=["GET"])
def index():
    if User.is_authenticated is True:
        return 'Muah'
    else:
        return render_template("login.html")


@app.route('/signup', methods=["POST"])
def Signup():
    uname = request.form["username"]
    Number = request.form["phone"]
    email = request.form["email"]
    Pass = request.form["password"]
    user = User(Number, email, uname, Pass)
    db.session.add(user)
    db.session.commit()
    login_user(user, remember=True)
    return 'MUAHA'


@app.route('/logout')
def logout():
    User.logout_user()
    return 'Logged Out'


if __name__ == "__main__":
    app.run(debug=True)
