import requests as rq
import json

URL = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
cards = []
players = []
gameLoop = True

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

def getPlayerTotal(player):
    for i in range(len(cards)):
        return cards
    else:
        pass
        
def drawCard(id, player, count):
    print("start")
    card = rq.get(url="https://deckofcardsapi.com/api/deck/"+str(id)+"/draw/?count="+str(count))
    card = card.json()
    #card["cards"]["value"], card["cards"]["suit"]
    for c in range(count):
        card_value = card["cards"][c]["value"]
        card_suit = card["cards"][c]["suit"]
        if len(cards) > 0:
            if card_value == "JACK":
                card_number = 11
            elif card_value == "QUEEN":
                card_number = 12
            elif card_value == "KING":
                card_number = 13
            elif card_value == "ACE":
                card_number = 1
            else:
                card_number = card_value
            for x in range(len(cards)):
                t = cards[x]
                print('1')
                t[player].append([card_value + " " + card_suit, int(card_number)])
                cards[x] = t                    
        print(str(player)+" drew a ", card_value ," of ", card_suit)
    print(cards)
    print("end")
            
def hit(player):
    global deck_id
    drawCard(deck_id, player, 1)
    

def createPlayers(names):
    for x in names:
        players.append(x)
        cards.append({x:[]})
        

while gameLoop:
    createPlayers(str(input()).split(", "))
    print(cards)
    for i in players:
        drawCard(deck_id, i, 2)
