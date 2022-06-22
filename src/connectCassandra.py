import os
from astrapy.client import create_astra_client

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# get Astra connection information from environment variables
ASTRA_DB_ID = str(os.environ.get("DB_ID"))
ASTRA_DB_REGION = str(os.environ.get("DB_REGION"))
ASTRA_DB_APPLICATION_TOKEN = str(os.environ.get("token"))
ASTRA_DB_KEYSPACE = 'mercadolivre'
TEST_COLLECTION_NAME = "test"

def connect():
  cloud_config= {'secure_connect_bundle': './secure-connect-fatec.zip'}
  auth_provider = PlainTextAuthProvider('zKYtLKEdlqbsFrwcjslRhtME','+xifG4JQxh_o4ydu2aYRkYL5YIoilwSb63IF57K86n_AriS+5r7Pr8Odri8No.axCapArbUZXBv6eTTsnGim_RG3-0SOx8HGXtjap_QTb03hxYcJDuByHX-Hx4rNmRoI')
  cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
  session = cluster.connect()

  row = session.execute("select release_version from system.local").one()
  if row:
    print(row[0])
  else:
    print("An error occurred.")
  return session