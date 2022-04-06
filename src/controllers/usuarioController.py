from flask import jsonify
import simplejson as json
from bson import json_util,ObjectId

import src.connectDb as connectDb

def find_usuarios():
  bd_mercado_livre = connectDb.connect()
  col = bd_mercado_livre.usuario

  doc = col.find()

  retorno = []
  for x in doc:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))

  return json.dumps(retorno)

def find_por_id(request):
  usuario = request.get_json()
  bd_mercado_livre = connectDb.connect()
  col = bd_mercado_livre.usuario

  doc = col.find({"_id": ObjectId(usuario["id"])})

  retorno = []
  for x in doc:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))

  return json.dumps(retorno)
  

def inserir(request):
  usuario = request.get_json()
  bd_mercado_livre = connectDb.connect()
  col = bd_mercado_livre.usuario
  col.insert_one(usuario)
  
  return json.dumps({
    "status": "Usuario inserido",
    "usuario":json.loads(json_util.dumps(usuario))
  })
  
def delete(request):
  usuario = request.get_json()
  bd_mercado_livre = connectDb.connect()
  col = bd_mercado_livre.usuario
  print(usuario)

  try:
    col.delete_one({"_id": ObjectId(usuario["id"])})
    return json.dumps({"status": "Usuario deletado"})
  except:
    return json.dumps({"message": "Ocorreu um erro"})


def inserir_amostra():
  bd_mercado_livre = connectDb.connect()
  bd_mercado_livre.usuario.insert_many([{
    "nome":"Gabriel Camargo Leite",
    "cpf":"123.456.789",
    "endereco":[{
      "rua":"José dos Santos",
      "numero":112,"estado":"SP",
      "cidade":"São José dos Campos",
      "principal":True
    },{
      "rua":"José dos Santos",
      "numero":112,
      "estado":"SP",
      "cidade":"São José dos Campos",
      "principal":False
    }],
    "carrinho":[{
      "produto1":{
        "nome":"Tinta para carros",
        "desc":"pinta carros",
        "preco":59.99,
        "a-vista":50,
        "prazo":65.99,
        "uuid-vendedor":"6229d65857dd0e593464069b"
      }}],
      "email":"gabriel.cleite@hotmail.com"
    }])
  return jsonify(message="success")