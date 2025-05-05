import backend.search as search

description = input("Enter your search here: ")

deck = search.get_deck_from_description(description=description)
