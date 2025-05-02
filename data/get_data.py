import requests
from pyedhrec import EDHRec

edhrec = EDHRec()

def main():
    commanders = fetch_legal_commanders()
    for i in range(len(commanders)):
         commanders[i] = commanders[i]["name"]
    print(commanders)

    sample = commanders[0]
    decks = edhrec.get_commander_decks(sample)
    print(decks.keys(), len(decks))

    # decklists = get_all_decks(commanders=commanders)

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
