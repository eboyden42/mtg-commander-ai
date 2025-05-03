import requests
from pyedhrec import EDHRec
import ai
from pymongo import MongoClient
import os

mongo = MongoClient(os.getenv("MONGO_CONNECTION_STRING"))
db = mongo["mtgdb"]
edh_collection = db["edhdecks"]
edhrec = EDHRec()

def main():
    print("Fetching all legal commanders...")
    commanders = fetch_legal_commanders()
    for i in range(len(commanders)):
         commanders[i] = commanders[i]["name"]
         print("Generating description for "+str(commanders[i]))
         item = create_commander_dictionary(commanders[i])
         print("Logging "+str(commanders[i])+" info to db...")
         log_item_to_db(item)


def log_item_to_db(item):
    if item != None:
        edh_collection.insert_one(item)

def create_commander_dictionary(commander):
    try:
        decks = edhrec.get_commander_decks(commander)
        item = {
            "commander": str(commander),
            "decklist": decks["deck"],
            "description": ai.get_description("Commander"+str(commander)+str(decks["deck"]))
        }
        return item
    except:
        pass


def fetch_legal_commanders():
    url = "https://api.scryfall.com/cards/search"
    query = (
        'is:commander legal:commander '
        '(type:"legendary creature" or oracle:"can be your commander")'
    )
    params = {
        "q": query,
        "unique": "cards",  # Avoid duplicate printings
        "order": "name"
    }

    commanders = []
    while url:
        response = requests.get(url, params=params)
        data = response.json()

        for card in data["data"]:
            commanders.append({
                "name": card["name"],
            })

        url = data.get("next_page")  # Pagination

    return commanders

def get_all_decks(commanders):
    decklists = []
    for i in range(len(commanders)):
        try:
            print("Getting decks for "+str(commanders[i]))
            decklists.append(edhrec.get_commander_decks(commanders[i]))
        except:
            print("Decks not found...")
    
    return decklist

main()
