from flask import jsonify
import simplejson as json
from bson import json_util,ObjectId

import src.connectDb as connectDb

def find_vendedores():
  bd_mercado_livre = connectDb.connect()
  col = bd_mercado_livre.vendedor

  doc = col.find()

  retorno = []
  for x in doc:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))

  return json.dumps(retorno)

def find_por_id(request):
  vendedor = request.get_json()
  bd_mercado_livre = connectDb.connect()
  col = bd_mercado_livre.vendedor

  doc = col.find({"_id": ObjectId(vendedor["id"])})

  retorno = []
  for x in doc:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))

  return json.dumps(retorno)

def inserir(request):
  vendedor = request.get_json()
  bd_mercado_livre = connectDb.connect()
  col = bd_mercado_livre.vendedor
  col.insert_one(vendedor)
  
  return json.dumps({
    "status": "vendedor inserido",
    "vendedor":json.loads(json_util.dumps(vendedor))
  })
  
def delete(request):
  vendedor = request.get_json()
  bd_mercado_livre = connectDb.connect()
  col = bd_mercado_livre.vendedor

  try:
    col.delete_one({"_id": ObjectId(vendedor["id"])})
    return json.dumps({"status": "vendedor deletado"})
  except:
    return json.dumps({"message": "Ocorreu um erro"})


def inserir_amostra():
  bd_mercado_livre = connectDb.connect()
  bd_mercado_livre.vendedor.insert_many({
    "nome":"João Ferreira",
    "cnpj":"1111111111",
    "email":"jao_ferreira@gmail.com",
    "endereco":[{
      "rua":"epaminondas",
      "numero":"55",
      "estado":"SP",
      "cidade":"São Paulo",
      "principal":True
    },{
      "rua":"marechal rondon",
      "numero":"180",
      "estado":"SP",
      "cidade":"São Paulo",
      "principal":False
    }],
    "telefone":"1239558277"
  })
  return jsonify(message="success")