from flask import Flask
from flask_misaka import Misaka

misaka = Misaka()


def create_app():
    app = Flask(__name__)
    
    misaka.init_app(app)

    with app.app_context():
        from app.frontend.frontend import frontend_bp

        app.register_blueprint(frontend_bp)
    return app
