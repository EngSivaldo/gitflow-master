from flask import Flask
from flask_login import LoginManager # <--- Adicione
from app.blueprints.web import web_bp
from app.blueprints.auth import auth_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sua-chave-secreta-aqui' # Necessário para sessões

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login' # Onde mandar quem não está logado

    # Simulação de carregamento de usuário para o Sênior
    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User # Criaremos este modelo simples
        return User.get(user_id)

    app.register_blueprint(web_bp)
    app.register_blueprint(auth_bp)

    return app