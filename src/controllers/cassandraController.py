from datetime import date
import src.connectCassandra as connectCassandra
import json
import uuid

cursor = connectCassandra.connect()


ASTRA_DB_KEYSPACE = "mercadolivre"
ASTRA_DB_TABLE = "usuario"

def show():
  result = cursor.execute("SELECT * FROM mercadolivre.usuario")
  result = result[0]
  
  return json.dumps({"nome":f'{result.nome} {result.sobrenome}'})