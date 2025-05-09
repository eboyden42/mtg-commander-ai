from pymongo import MongoClient
import os
import openai
# from sentence_transformers import SentenceTransformer

mongo = MongoClient(os.getenv("MONGO_CONNECTION_STRING"))
collection = mongo["mtgdb"]["edhdecks"]

openai.api_key = os.getenv("OPENAI_API_KEY")
# model = SentenceTransformer("all-MiniLM-L6-v2")

def get_deck_from_description(description):
    # embedding = model.encode(description).tolist()
    embedding = get_openai_embedding(description)

    pipeline = [
        {
            "$vectorSearch": {
                "index": "openai_description",
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
                "decklist": 1,
                "description": 1,
                "score": { "$meta": "vectorSearchScore" }
            }
        }
    ]

    results = list(collection.aggregate(pipeline))

    for doc in results:
        print(f"{doc['commander']} (score: {doc['score']:.4f})")
        print(doc['description'])
        print(doc['decklist'])
        print("-" * 60)

    return results

def get_openai_embedding(text):
    response = openai.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )
    return response.data[0].embedding