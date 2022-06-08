import os
from astrapy.collections import create_client

# get Astra connection information from environment variables
ASTRA_DB_ID = str(os.environ.get("DB_ID"))
ASTRA_DB_REGION = str(os.environ.get("DB_REGION"))
ASTRA_DB_APPLICATION_TOKEN = str(os.environ.get("token"))
ASTRA_DB_KEYSPACE = 'mercadolivre'
TEST_COLLECTION_NAME = "test"

def connect():
  # setup an Astra Client and create a shortcut to our test colllection
  astra_client = create_client(
    astra_database_id=ASTRA_DB_ID,
    astra_database_region=ASTRA_DB_REGION,
    astra_application_token=ASTRA_DB_APPLICATION_TOKEN
  )

  return astra_client.namespace(ASTRA_DB_KEYSPACE).collection(TEST_COLLECTION_NAME)