from flask import Blueprint, render_template, abort
# No topo do arquivo run.py, adicione o import:
from app.erros_git import ERROS_COMUNS
web_bp = Blueprint('web', __name__)

# Este dicionário funciona como um "Banco de Dados" temporário.
# Centralizar o conteúdo aqui facilita a manutenção.
CONTEUDO_ESTAGIOS = {
    1: {
        "id": 1,
        "titulo": "Clone & Setup",
        "subtitulo": "Trazendo o projeto para sua máquina",
        "cor": "blue",
        "icone": "fa-download",
        "explicacao": "O clone cria uma cópia local do repositório remoto. Como sênior, lembre-se: clone uma vez, atualize sempre (git pull).",
        "comandos": ["git clone <url>", "python -m venv venv", "pip install -r requirements.txt"],
        "dica_senior": "Nunca esqueça o .gitignore. Subir a pasta venv é um erro clássico de quem está começando."
    },
    2: {
        "id": 2,
        "titulo": "Feature Branches",
        "subtitulo": "Trabalhando de forma isolada",
        "cor": "indigo",
        "icone": "fa-code-branch",
        "explicacao": "Branches permitem que você desenvolva novas funcionalidades sem afetar o código principal estável.",
        "comandos": ["git checkout -b feature/nome-tarefa", "git status", "git add ."],
        "dica_senior": "Dê nomes claros às suas branches, como 'feature/login-social' em vez de 'feature/teste'."
    },
    3: {
        "id": 3,
        "titulo": "PR & Review",
        "subtitulo": "Qualidade em primeiro lugar",
        "cor": "purple",
        "icone": "fa-eye",
        "explicacao": "O Pull Request é onde o time revisa seu código. É a melhor escola para um desenvolvedor júnior.",
        "comandos": ["git push origin feature/nome", "Abrir PR no GitHub", "Revisar comentários"],
        "dica_senior": "Um PR pequeno é revisado rápido. Um PR com 50 arquivos alterados é o pesadelo do revisor."
    },
    4: {
        "id": 4,
        "titulo": "Merge Conflicts",
        "subtitulo": "Resolvendo divergências",
        "cor": "orange",
        "icone": "fa-exclamation-triangle",
        "explicacao": "Conflitos ocorrem quando dois devs alteram a mesma linha. É um processo manual de decisão.",
        "comandos": ["git pull origin develop", "Aceitar alterações", "git commit"],
        "dica_senior": "Conflitos não são erros, são apenas o Git pedindo uma decisão humana."
    },
    5: {
        "id": 5,
        "titulo": "CI/CD Pipeline",
        "subtitulo": "Automação no Google Cloud",
        "cor": "green",
        "icone": "fa-rocket",
        "explicacao": "CI/CD garante que o código passe por testes antes de chegar no servidor de produção.",
        "comandos": ["git push", "Check GitHub Actions", "Deploy automático"],
        "dica_senior": "Confie nos seus testes. Se o CI falhou, o problema é real e precisa ser corrigido antes do merge."
    }
}

@web_bp.route('/')
def index():
    # Passamos apenas os valores do dicionário para o template
    return render_template('index.html', estagios=CONTEUDO_ESTAGIOS.values())

@web_bp.route('/estagio/<int:id>')
def detalhe_estagio(id):
    # Rota dinâmica: busca no dicionário pelo ID passado na URL
    item = CONTEUDO_ESTAGIOS.get(id)
    if not item:
        abort(404)  # Se o ID não existir, mostra erro 404
    return render_template('detalhe_estagio.html', item=item)

@web_bp.route('/fluxo-git')
def fluxo_git():
    # Mantemos esta rota separada pois é uma página de referência visual
    workflow = [
        {"branch": "main", "cor": "bg-red-600", "status": "Produção", "desc": "Código estável."},
        {"branch": "develop", "cor": "bg-yellow-500", "status": "Desenvolvimento", "desc": "Integração de código."},
        {"branch": "feature/*", "cor": "bg-blue-500", "status": "Novas Funcionalidades", "desc": "Trabalho isolado."},
        {"branch": "release/*", "cor": "bg-green-500", "status": "Preparação", "desc": "Ajustes de versão."},
        {"branch": "hotfix/*", "cor": "bg-purple-600", "status": "Correção Urgente", "desc": "Reparo imediato."}
    ]
    return render_template('modulos/fluxo.html', workflow=workflow)
  
@web_bp.route('/socorro')
def glossario_erros():
    erros = [
        {
            "erro": "Commit na branch errada",
            "solucao": "Use 'git reset HEAD~1 --soft' para desfazer o commit mas manter o código, mude de branch e commite novamente.",
            "nivel_desespero": "Baixo"
        },
        {
            "erro": "Esqueci de uma alteração no último commit",
            "solucao": "Adicione o arquivo com 'git add' e use 'git commit --amend --no-edit'. Isso 'remenda' o commit anterior.",
            "nivel_desespero": "Médio"
        },
        {
            "erro": "Entrei no editor Vim por engano e não sei sair",
            "solucao": "Aperte 'ESC', digite ':q!' e dê 'Enter' para sair sem salvar.",
            "nivel_desespero": "Alto (para iniciantes)"
        }
    ]
    return render_template('modulos/socorro.html', erros=erros)




# ... (outras rotas)

@web_bp.route('/glossario')
def glossario():
    return render_template('glossario.html', erros=ERROS_COMUNS)