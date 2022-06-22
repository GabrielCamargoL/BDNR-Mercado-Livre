from datetime import date, timedelta
import datetime
import json

import src.connectCassandra as connectCassandra
import src.controllers.redisController as relatorio_redis
 
cursor = connectCassandra.connect()

ASTRA_DB_KEYSPACE = "mercadolivre"
ASTRA_DB_TABLE = "usuario"


def show():
  result = cursor.execute("SELECT * FROM mercadolivre.relatorio")
  if(not result):
    return json.dumps({"message":"Dados não encontrados"})
  
  result = result[0]
  return json.dumps({
    "nome":result.backup_dia,
    "dados": json.dumps({result.dados})
  })


def insert():
  hoje = date.today()
  hoje_formatado = str(hoje.strftime("%d/%m/%Y"))
  
  json_redis = relatorio_redis.relatorio_geral()
  print(str(json.dumps(json_redis)))
  cursor.execute(f'INSERT INTO mercadolivre.relatorio(id, backup_dia, dados) VALUES ({datetime.datetime.now().timestamp()}, {hoje_formatado}, {str(json.dumps(json_redis))})')

  return json.dumps(json_redis)