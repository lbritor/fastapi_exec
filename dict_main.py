import uuid
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field


# Criar uma API com rotas POST e GET para cadastrar notas com título e descrição e fazer a listagem dessas.
# Criar identificador para as notas, rota para alterar nota, rota para deletar nota e rota para pegar uma nota por id. 
# Ps: passar id na rota utilizando path parameters.

app = FastAPI()
notas = {}

class DadosNotas(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    titulo: str
    descricao: str


@app.post('/notas')
def criar_notas(nota: DadosNotas = Body()):
    notas[nota.id] = nota
    return nota

@app.get("/notas/listar")
def listar_notas():
    return notas


@app.put('/alterar/{id}')
def atualizar_notas(id: uuid.UUID, nota: DadosNotas = Body()):
    notas[id] = nota
    return notas[id]


@app.delete('/deletar/{id}')
def deletar_notas(id: uuid.UUID):
    id_del = notas[id]
    notas.pop(id)
    return id_del


@app.get('/notas/{id}')
def buscar_id(id: uuid.UUID):
    return notas[id]

