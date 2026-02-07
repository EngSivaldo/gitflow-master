# app/erros_git.py

ERROS_COMUNS = [
    {
        "id": 1,
        "titulo": "Merge Conflict (Conflito de Mesclagem)",
        "descricao": "Ocorre quando dois desenvolvedores alteram a mesma linha no mesmo arquivo em branches diferentes.",
        "sinal": "O Git interrompe o merge e exibe: 'CONFLICT (content): Merge conflict in...'",
        "solucao": "Abra o arquivo, localize as marcações (<<<<, ====, >>>>), escolha o código correto e faça o commit.",
        "comando": "git status"
    },
    {
        "id": 2,
        "titulo": "Rejected - Non-fast-forward",
        "descricao": "Você tentou dar push, mas o repositório remoto tem commits que você não tem localmente.",
        "sinal": "error: failed to push some refs to... Updates were rejected.",
        "solucao": "Sincronize seu repositório local com o remoto antes de enviar suas mudanças.",
        "comando": "git pull origin main"
    },
    {
        "id": 3,
        "titulo": "Detached HEAD",
        "descricao": "Você não está em uma branch, mas sim 'flutuando' em um commit específico ou tag.",
        "sinal": "You are in 'detached HEAD' state.",
        "solucao": "Crie uma nova branch a partir desse ponto ou volte para a main.",
        "comando": "git checkout main"
    }
]