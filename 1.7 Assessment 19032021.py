import requests as rq
import json

URL = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
cards = {}
players = []

def createDeck():
    deck = rq.get(url=URL)
    deck = deck.json()
    return deck["deck_id"]

deck_id = createDeck()

# ________________________________________________________________________________________
#                                   FUNCTIONS
def shuffleDeck(id):
    deck = rq.get(url="https://deckofcardsapi.com/api/deck/"+str(id)+"/shuffle/?deck_count=1")
    deck = deck.json()
    print("SUCCESS! The deck has been shuffled.")

def drawCard(id, player, count): 
    card = rq.get(url="https://deckofcardsapi.com/api/deck/"+str(id)+"/draw/?count="+str(count))
    card = card.json()
    cards[player] = card["cards"]["value"], card["cards"]["suit"]
    print(str(player)+" a ", card["cards"]["value"], " of ", card["cards"]["suit"])

def createPlayers(names):
    for x in names:
        players.append(x)

createPlayers(input().split(", "))
print(players)
drawCard(deck_id, players[0], 1)
