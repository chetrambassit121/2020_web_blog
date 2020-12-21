from flask import Flask
from views.home import home_blueprint


app = Flask(__name__)

app.register_blueprint(home_blueprint, url_prefix="/")


if __name__ == '__main__':
    app.run(port=3000, debug=True)
