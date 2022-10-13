import uuid
from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel, Field


# Criar uma API com rotas POST e GET para cadastrar notas com título e descrição e fazer a listagem dessas.
# Criar identificador para as notas, rota para alterar nota, rota para deletar nota e rota para pegar uma nota por id. 
# Ps: passar id na rota utilizando path parameters.

app = FastAPI()
notas = []

class DadosNotas(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    titulo: str
    descricao: str


@app.post('/notas')
def criar_notas(nota: DadosNotas = Body()):
    notas.append(nota)
    return nota

@app.get("/notas/listar")
def listar_notas():
    return notas


@app.put('/alterar/{id}')
def atualizar_notas(id:uuid.UUID, nota: DadosNotas = Body()):
    for i in range(len(notas)):
        if notas[i].id == id:
            notas[i] = nota
            notas[i].id = id
            return notas[i]
    raise HTTPException(status_code=404, detail='ID not found')
    

@app.delete('/deletar/{id}')
def deletar_notas(id: uuid.UUID):
    for i in range(len(notas)):
        if notas[i].id == id:
            return notas.pop(i)
            
@app.get('/notas/{id}')
def buscar_id(id: uuid.UUID):
    for i in range(len(notas)):
        if notas[i].id == id:
            return notas[i]
    raise HTTPException(status_code=404, detail="ID not found")