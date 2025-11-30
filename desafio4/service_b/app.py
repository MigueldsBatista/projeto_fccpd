import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    try:
        response = requests.get('http://service_a:5000/users')
        users = response.json()
        result = "<h1>Relatório de Usuários</h1><ul>"
        for user in users:
            result += f"<li>Usuário <b>{user['name']}</b> ativo desde {user['active_since']}</li>"
        result += "</ul>"
        return result
    except Exception as e:
        return f"Erro ao comunicar com Serviço A: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
