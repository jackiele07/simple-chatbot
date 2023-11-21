import sys
from llama_index.vector_stores import ChromaVectorStore
from llama_index import StorageContext, SimpleDirectoryReader, VectorStoreIndex, load_index_from_storage

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

data_dir = input("Enter data path: ")
if(len(data_dir)<1):
    print("No data found, exit program")
    sys.exit(0)
storage_dir = data_dir + "_storage"
documents = SimpleDirectoryReader(data_dir).load_data()
index = VectorStoreIndex.from_documents(documents)
# store it for later
index.storage_context.persist(persist_dir=storage_dir)