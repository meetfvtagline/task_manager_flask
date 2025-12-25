from flask import Flask
from .config import Config
from .extensions import db
from .routes.auth import auth_bp
from .routes.tasks import tasks_bp
from .routes.home import home_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    # app.register_blueprint(dash_page)

    with app.app_context():
        db.create_all()

    return app