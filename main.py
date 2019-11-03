from flask import Flask, request, flash, url_for
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
    Authenticated = db.Column(db.Boolean())

    def __init__(self, Number, Email, Uname, Pass, Auth):
        self.PNumber = Number
        self.Email = Email
        self.Username = Uname
        self.PasswordH = str(hashlib.md5(Pass.encode()).hexdigest())
        self.Authenticated = Auth

    def is_authenticated(self):
        return self.Authenticated

    def get_id(self):
        return self.id


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
        user = User(Number, email, uname, Pass, True)
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)
        return render_template("Schedule.html")
    except Exception as e:
        return str(e)


@app.route('/logout')
def logout():
    UQ = User.query.filter_by(id=User.get_id()).first()
    UQ.Authenticated = False
    db.session.add(UQ)
    db.session.commit()
    logout_user()
    flash("Logged Out")
    return url_for('login')


@app.route('/login')
def login():
    return render_template("Login.html")


@app.route('/loginuser', methods=['POST'])
def loginuser():
    try:
        Pwd = request.form["password"]
        Uname = request.form["username"]
        UQ = User.query.filter_by(Username=Uname, Password=Pwd)
        UQ.Authenticated = True
        db.session.add(UQ)
        db.session.commit()
        login_user(UQ)
    except Exception:
        return 'NO'


@app.route('/settings')
def settings():
    return render_template("Index.html")


@app.route('/change', methods=["POST"])
def changesettings():
    return 'NO'


@app.route('/schedule')
def schedule():
    return render_template("Schedule.html")


if __name__ == "__main__":
    app.run(debug=True)
