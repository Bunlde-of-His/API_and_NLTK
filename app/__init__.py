from flask import Flask


def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .routes import NltkApi
        nltk_api = NltkApi(app)

    return app
