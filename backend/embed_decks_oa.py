import openai
from pymongo import MongoClient
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
mongo = MongoClient(os.getenv("MONGO_CONNECTION_STRING"))
collection = mongo["mtgdb"]["edhdecks"]

def add_embeddings_to_db():
    count = 1
    for doc in collection.find():
        print("Embedding..."+str(count))
        count += 1
        description = doc["description"]
        embedding = get_embedding(description)
        collection.update_one(
            {"_id": doc["_id"]},
            {"$set": {"embedding": embedding}}
        )

def get_embedding(text):
    response = openai.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )
    return response.data[0].embedding

add_embeddings_to_db()