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
  
  
@web_bp.route('/fluxo-git')
def fluxo_git():
    # Definindo a hierarquia de branches para a aula
    workflow = [
        {"branch": "main", "cor": "bg-red-600", "status": "Produção", "desc": "Código estável e pronto para o usuário final."},
        {"branch": "develop", "cor": "bg-yellow-500", "status": "Desenvolvimento", "desc": "Integração de novas funcionalidades testadas."},
        {"branch": "feature/*", "cor": "bg-blue-500", "status": "Novas Funcionalidades", "desc": "Trabalho isolado para cada tarefa do time."},
        {"branch": "release/*", "cor": "bg-green-500", "status": "Preparação", "desc": "Ajustes finos antes de subir para a main."},
        {"branch": "hotfix/*", "cor": "bg-purple-600", "status": "Correção Urgente", "desc": "Reparo imediato em produção."}
    ]
    return render_template('modulos/fluxo.html', workflow=workflow)