from flask import Flask
import os


def create_app():
    app = Flask(__name__, instance_relative_config= True)
    app.config.from_mapping(
        KEY = 'DEV',
        DATABASE = os.join(app.instance_path,"recipie.sqlite")
    )
    try:
        os.makedirs(app.instance_path)
    except OSError:
        print("Unable to make the directory")


    @app.route("/")
    def hello():
        return "Hello"
    return app