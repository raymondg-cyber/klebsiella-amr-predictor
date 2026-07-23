import requests

def get_card_ontology():
    response = requests.get("https://mcmaster.ca")
    if response.status_code == 200:
        return response.json()
    raise RuntimeError("Could not connect to CARD Repository.")