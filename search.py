from pymongo import MongoClient
import os
from sentence_transformers import SentenceTransformer

mongo = MongoClient(os.getenv("MONGO_CONNECTION_STRING"))
collection = mongo["mtgdb"]["edhdecks"]
model = SentenceTransformer("all-MiniLM-L6-v2")
embedding = model.encode("sacrifice golgari graveyard recursion").tolist()

def get_deck_from_description(description):
    embedding = model.encode(description).tolist()

    pipeline = [
        {
            "$vectorSearch": {
                "index": "description",
                "path": "embedding",
                "queryVector": embedding,
                "numCandidates": 100,
                "limit": 5,
                "filter": {}
            }
        },
        {
            "$project": {
                "commander": 1,
                "description": 1,
                "score": { "$meta": "vectorSearchScore" }
            }
        }
    ]

    results = list(collection.aggregate(pipeline))

    for doc in results:
        print(f"{doc['commander']} (score: {doc['score']:.4f})")
        print(doc['description'])
        print("-" * 60)

    return results