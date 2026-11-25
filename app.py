from webbrowser import get

from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

chamados = [];
proximo_id = 1;

@app.get('/')
def inicio():
    return {
        "mensagem": "API de chamados em funcionamento"
    }

@app.get('/chamados')
def listar_chamados():
    global chamados
    return chamados

@app.get('/chamados/<int:id>')
def obter_chamado(id):   
    chamado = next((c for c in chamados if c["id"] == id), None)
    
    if chamado:
        return chamado
    else:
        return {"mensagem": "Chamado não encontrado"}, 404
    
@app.post('/chamados')
def criar_chamado():
    
    global proximo_id
    data = request.get_json()
    chamado = {**data, "id": proximo_id}
    chamados.append(chamado)
    proximo_id += 1
    
    return jsonify({
        "mensagem": "Chamado criado com sucesso",
        "id": chamado["id"]
    }), 201
  