# app/logica_simulador.py

COMANDOS_RESPOSTA = {
    "git init": "🚀 Repositório inicializado! Agora o Git está de olho nesta pasta.",
    "git add .": "📦 Arquivos movidos para a área de preparação (Staging).",
    "git commit -m": "💾 Mudanças salvas no seu histórico local.",
    "git push": "☁️  Código enviado para o servidor remoto (GitHub)!",
    "git pull": "📥 Baixando as novidades do servidor para sua máquina.",
}

def processar_comando(comando):
    comando = comando.lower().strip()
    return COMANDOS_RESPOSTA.get(comando, "⚠️ Comando não reconhecido ou ainda não mapeado no simulador.")