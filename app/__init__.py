from flask import Flask
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sua-chave-secreta-aqui'

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Importações dentro da função para evitar erros de inicialização
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    from app.blueprints.web import web_bp
    from app.blueprints.auth import auth_bp

    app.register_blueprint(web_bp)
    app.register_blueprint(auth_bp)

    return app