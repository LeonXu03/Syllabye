from flask import Flask

#creates a Flask application
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey' #encrypts cookies and session data
    app.config['UPLOAD_FOLDER'] = 'uploaded'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app