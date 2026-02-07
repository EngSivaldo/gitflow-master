import os  # IMPORTANTE: Sem isso, o app.config['SECRET_KEY'] quebra o site
from flask import Flask
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    
    # Busca a chave do seu arquivo .env ou do sistema
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-não-segura')

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Importações protegidas contra erro de inicialização circular
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    # Registro das rotas (Blueprints)
    from app.blueprints.web import web_bp
    from app.blueprints.auth import auth_bp

    app.register_blueprint(web_bp)
    app.register_blueprint(auth_bp)

    return app