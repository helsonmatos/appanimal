from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

origins = [
    'http://127.0.0.1:5500'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#declarando nosso modelo de banco
class Animal(BaseModel):
    
    id: Optional[int]
    nome: str
    idade: Optional[int]
    sexo: str
    cor: Optional[str]


banco: List[Animal] = []


@app.get('/animais')
def listar_animais():
    return banco


@app.get('/animais/{animal_id}')
def obter_animal(animal_id:str):
    for animal in banco:
        if animal.id == animal_id:
            return animal
        return {'Erro': 'Animal não localizado.'}


@app.delete('/animais/{animal_id}')
def remover_animal(animal_id:str):
    posicao = -1
    for index,animal in enumerate(banco):
        if animal.id == animal_id:
            posicao = index

    if posicao != -1:
        banco.pop(posicao)
        return {"mensagem":"animal removido com sucesso"}
    else:
        return {"mensagem":"animal não encontrado"}


@app.post('/animais')
def criar_animal(animal: Animal):
    animal.id = str(uuid4())
    banco.append(animal)
    return {'status':'sucess'}