from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)