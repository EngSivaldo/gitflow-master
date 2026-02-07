from flask import Blueprint, render_template

web_bp = Blueprint('web', __name__)

@web_bp.route('/')
def index():
    # Dados das lições incluindo CI/CD
    estagios = [
        {"id": 1, "titulo": "Clone & Setup", "icone": "fa-download"},
        {"id": 2, "titulo": "Feature Branches", "icone": "fa-code-branch"},
        {"id": 3, "titulo": "PR & Review", "icone": "fa-eye"},
        {"id": 4, "titulo": "Merge Conflicts", "icone": "fa-exclamation-triangle"},
        {"id": 5, "titulo": "CI/CD Pipeline", "icone": "fa-rocket"}
    ]
    return render_template('index.html', estagios=estagios)

@web_bp.route('/estagio/5')
def cicd():
    return render_template('modulos/cicd.html')