from dotenv import load_dotenv
import anthropic
import os

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic(api_key=api_key)

SYSTEM = "You are a master deckbuilder for the game magic the gathering. I need you to create a description of the commander decklist that I give you. The description should be detailed and include things such as color scheme and deck type."

def getDescription(cards):
    response = client.messages.create(
        model="claude-3-5-haiku-20241022",
        max_tokens=1000,
        system=SYSTEM,
        messages=[
            {
                "role": "user",
                "content": str(cards)
            }
        ]
    )

    return response.content[0].text