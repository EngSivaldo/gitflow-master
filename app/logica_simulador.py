# app/logica_simulador.py

def processar_comando(comando):
    comando = comando.lower().strip()
    
    if not comando.startswith("git"):
        return "🚫 Todo comando Git precisa começar com a palavra 'git'!"

    partes = comando.split()
    
    if len(partes) < 2:
        return "❓ Você digitou apenas 'git'. Adicione uma ação (ex: git status)."

    acao = partes[1]

    # Dicionário expandido com mais detalhes
    respostas = {
        "init": "🚀 Repositório inicializado! Agora o Git está de olho nesta pasta.",
        "add": "📦 Arquivos movidos para a área de preparação (Staging).",
        "commit": "💾 Mudanças salvas com sucesso no seu histórico local!",
        "push": "☁️  Código enviado para o servidor remoto (GitHub)!",
        "pull": "📥 Baixando as novidades do servidor para sua máquina.",
        "status": "🔍 Verificando o estado atual dos seus arquivos e o que falta commitar.",
        "branch": "🌿 Gerenciando ramificações para trabalhar em novas funcionalidades.",
        "checkout": "🔄 Alternando entre branches ou restaurando arquivos.",
        "merge": "🤝 Unindo o histórico de duas branches diferentes.",
        "rm": "🗑️  Removendo arquivos do controle do Git (Staging) ou do diretório.",
        "remote": "🔗 Gerenciando as conexões com servidores remotos como o GitHub.",
        "log": "📜 Visualizando o histórico completo de commits realizados."
    }

    return respostas.get(acao, f"⚠️ O Git possui a ação '{acao}', mas ela ainda não foi detalhada no simulador.")