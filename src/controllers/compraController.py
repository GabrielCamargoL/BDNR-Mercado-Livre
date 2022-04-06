from flask import jsonify
import simplejson as json
from bson import json_util,ObjectId

import src.connectDb as connectDb

def find_compras():
  bd_mercado_livre = connectDb.connect()
  col = bd_mercado_livre.Compra

  doc = col.find()

  retorno = []
  for x in doc:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))

  return json.dumps(retorno)

def find_por_id(request):
  Compra = request.get_json()
  bd_mercado_livre = connectDb.connect()
  col = bd_mercado_livre.Compra

  doc = col.find({"_id": ObjectId(Compra["id"])})

  retorno = []
  for x in doc:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))
  
  return json.dumps(retorno)

def inserir(request):
  Compra = request.get_json()
  bd_mercado_livre = connectDb.connect()
  col = bd_mercado_livre.Compra
  col.insert_one(Compra)
  
  return json.dumps({
    "status": "Compra inserido",
    "Compra":json.loads(json_util.dumps(Compra))
  })
  
def delete(request):
  Compra = request.get_json()
  bd_mercado_livre = connectDb.connect()
  col = bd_mercado_livre.Compra

  try:
    col.delete_one({"_id": ObjectId(Compra["id"])})
    return json.dumps({"status": "Compra deletado"})
  except:
    return json.dumps({"message": "Ocorreu um erro"})


def inserir_amostra():
  bd_mercado_livre = connectDb.connect()
  bd_mercado_livre.Compra.insert_many({
    "usuario": {
      "nome":"Gabriel Camargo Leite",
      "endereco": {
        "rua":"José dos Santos",
        "numero":112,
        "estado":"SP",
        "cidade":"São José dos Campos",
        "principal":True
      },
      "produto":[{
        "nome":"Tinta para carros",
        "descricao":"pinta carros",
        "preco":59.99,
        "a-vista":50,
        "prazo":65.99,
        "uuid-vendedor":"6229d65857dd0e593464069b"
      }],
      "vendedor": {
        "nome":"João Ferreira",
        "endereco": {
          "rua":"Epaminondas",
          "numero":55,
          "estado":"SP",
          "cidade":"São Paulo"
          }
        },
        "total":50,
        "status":"pendente",
        "pagamento":"a vista"
    }
  })
  return jsonify(message="success")