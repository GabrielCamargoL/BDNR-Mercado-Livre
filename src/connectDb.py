from pymongo import MongoClient

def connect():
  client = MongoClient("mongodb+srv://GabrielCamargoL:06111997s20@cluster0.rpjin.mongodb.net/myFirstDatabase?authSource=admin&replicaSet=atlas-kgm265-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true")
  db_mercado_livre = client['mercado-livre']

  return db_mercado_livre
