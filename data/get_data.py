import requests
from pyedhrec import EDHRec

edhrec = EDHRec()

def main():
    commanders = fetch_legal_commanders()
    for i in range(len(commanders)):
         commanders[i] = commanders[i]["name"]

    for commander in commanders:
        print(createCommanderDictionary(commander=commander))


def createCommanderDictionary(commander):
    try:
        decks = edhrec.get_commander_decks(commander)
        item = {
            "commander": str(commander),
            "decklist": decks["deck"],
            "description": "None"
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
