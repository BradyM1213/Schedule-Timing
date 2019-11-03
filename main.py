from flask import Flask, request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, logout_user, LoginManager
import hashlib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = 'MUAHAHAHAHHAHAHAHAHAHAHAHAAHAH'
db = SQLAlchemy(app)
login = LoginManager()
login.init_app(app)


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

    def is_authenticated(self):
        return True


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/', methods=["GET"])
def index():
    if User.is_authenticated is True:
        return 'Muah'
    else:
        return render_template("Signup.html")


@app.route('/signup', methods=["POST"])
def Signup():
    try:
        uname = request.form["username"]
        Number = request.form["phone"]
        email = request.form["email"]
        Pass = request.form["password"]
        user = User(Number, email, uname, Pass)
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)
        return 'MUAHA'
    except Exception as e:
        return str(e)


@app.route('/logout')
def logout():
    logout_user()
    return 'Logged Out'


@app.route('/login')
def login():
    return render_template("Login.html")


if __name__ == "__main__":
    app.run(debug=True)
