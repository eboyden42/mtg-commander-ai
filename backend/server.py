from flask import Flask, jsonify, request
from flask_cors import CORS
import search

app = Flask(__name__)
CORS(app)

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
            "decklist": str(deck["decklist"]),
            "description": str(deck["description"])
        }
        parsedDecks.append(parsedDeck)

    return jsonify({"message": parsedDecks})

if __name__ == '__main__':
    app.run(debug=True)