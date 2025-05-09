from sentence_transformers import SentenceTransformer
from pymongo import MongoClient
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

mongo = MongoClient(os.getenv("MONGO_CONNECTION_STRING"))
db = mongo["mtgdb"]
collection = db["edhdecks"]

def add_embeddings_to_db():
    for doc in collection.find():
        print("Embedding description "+str(count)+" of 2111... "+str(2111-count)+" remaining")
        description = doc["description"]
        embedding = model.encode(description).tolist()
        print("Adding to database...")
        collection.update_one(
            {"_id": doc["_id"]},
            {"$set": {"embedding": embedding}}
        )