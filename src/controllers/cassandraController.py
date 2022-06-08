from datetime import date
import src.connectCassandra as connectCassandra
import json
import uuid

cursor = connectCassandra.connect()

def show():
  cliff_uuid = str(uuid.uuid4())
  cursor.create(path=cliff_uuid, document={
    "first_name": "Cliff",
    "last_name": "Wicklow",
  })
  
  return json.dumps({"hasError": False, "Message": "acertou"})