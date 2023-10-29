from flask import Flask
from os import path

import psycopg2

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dsadasldanslas'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yourusername:yourpassword@db:5432/yourdbname'

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
