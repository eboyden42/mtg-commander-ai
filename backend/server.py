from flask import Flask, jsonify, request
import os
from flask_cors import CORS
import search

app = Flask(__name__)
CORS(app, origins=["https://commander-ai-frontend.onrender.com/"])

@app.route("/search", methods=["POST"])
def run_search():
    data = request.get_json()
    description = data.get("description")
    decks = search.get_deck_from_description(description=description)
    print(decks)

    

    parsedDecks = []
    for deck in decks:
        parsedDeck = {
            "id": str(deck["_id"]),
            "commander": str(deck["commander"]),
            "decklist": deck["decklist"],
            "description": str(deck["description"])
        }
        parsedDecks.append(parsedDeck)

    return jsonify({"message": parsedDecks})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.getenv("PORT"), debug=True)