from flask import session, render_template, Blueprint, request
from models.user import User

user_blueprint = Blueprint("users", __name__)

@user_blueprint.route('/login', methods=['POST', 'GET'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None

    return render_template("users/profile.html", email=session['email'])


@user_blueprint.route('/register', methods=['POST', 'GET'])
def register_user():
    email = request.form['email']
    password = request.form['password']

    if User.get_by_email(email) is not None:
        return "Already an existing users! Please login instead."
    else:
        User.register(email, password)

    return render_template("users/profile.html", email=session['email'])




