from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    app.config.from_object('app.secure')
    register_blueprint(app)
    return app

def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
    return app