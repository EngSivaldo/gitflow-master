from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Registro de Blueprints (Separação de rotas)
    from app.blueprints.web import web_bp
    app.register_blueprint(web_bp)
    
    return app