from flask import jsonify
import simplejson as json
from bson import json_util,ObjectId

import src.connectDb as connectDb

def find_produtos():
  bd_mercado_livre = connectDb.connect()
  col = bd_mercado_livre.produto

  doc = col.find()

  retorno = []
  for x in doc:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))

  return json.dumps(retorno)

def find_por_id(request):
  produto = request.get_json()
  bd_mercado_livre = connectDb.connect()
  col = bd_mercado_livre.produto

  doc = col.find({"_id": ObjectId(produto["id"])})

  retorno = []
  for x in doc:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))
  
  return json.dumps(retorno)

def inserir(request):
  produto = request.get_json()
  bd_mercado_livre = connectDb.connect()
  col = bd_mercado_livre.produto
  col.insert_one(produto)
  
  return json.dumps({
    "status": "produto inserido",
    "produto":json.loads(json_util.dumps(produto))
  })
  
def delete(request):
  produto = request.get_json()
  bd_mercado_livre = connectDb.connect()
  col = bd_mercado_livre.produto

  try:
    col.delete_one({"_id": ObjectId(produto["id"])})
    return json.dumps({"status": "produto deletado"})
  except:
    return json.dumps({"message": "Ocorreu um erro"})


def inserir_amostra():
  bd_mercado_livre = connectDb.connect()
  bd_mercado_livre.produto.insert_many({
    "nome": "Tinta para carros",
    "descricao":"pinta carros",
    "preco":59.99,
    "a-vista":50,
    "prazo":65.99,
    "uuid-vendedor":"6229d65857dd0e593464069b",
    "pagamento":"a-vista",
    "status":"Pendente"
  })
  return jsonify(message="success")