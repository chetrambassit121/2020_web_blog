from flask import Flask
from views.home import home_blueprint
from views.users import user_blueprint

app = Flask(__name__)

app.register_blueprint(home_blueprint, url_prefix="/")
app.register_blueprint(user_blueprint, url_prefix="/users")


if __name__ == '__main__':
    app.run(port=3000, debug=True)
