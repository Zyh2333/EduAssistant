# extensions

from playhouse.postgres_ext import PostgresqlExtDatabase
from chromadb import PersistentClient
import os

db = PostgresqlExtDatabase(None)

chroma_client = None
knowledge_base_collection = None

def initialize_extensions():
    # initialize database
    db.init("eduassistant-v3",
            host="127.0.0.1",
            user="postgres",
            password="123456",
            port="5432")
    
    # initialize chroma
    global chroma_client
    chroma_client = PersistentClient()
    global knowledge_base_collection
    knowledge_base_collection = chroma_client.get_or_create_collection("knowledge_base")

# initialize_extensions()