import requests as rq
import json

URL = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
cards = []
players = []
gameLoop = True
gameOngoing = False

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
    t = 0
    for i in range(len(cards)):
        try:
            for ii in range(len(cards[i][player])):
                t += cards[i][player][ii][1]
        except:
            pass
    return t
 
def drawCard(id, player, count):
    #print("start")
    card = rq.get(url="https://deckofcardsapi.com/api/deck/"+str(id)+"/draw/?count="+str(count))
    card = card.json()
    #card["cards"]["value"], card["cards"]["suit"]
    for c in range(count):
        card_value = card["cards"][c]["value"]
        card_suit = card["cards"][c]["suit"]
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
            #print('1')
            try:
                t[player].append([card_value + " " + card_suit, int(card_number)])
                cards[x] = t
            except:
                pass
        print(str(player)+" drew a ", card_value ," of ", card_suit)
    #print(cards)
    #print("end")
           
def hit(player):
    global deck_id
    drawCard(deck_id, player, 1)
    print(player + "'s total is now " +str(getPlayerTotal(player)))
def createPlayers(names):
    for x in names:
        if x in players:
            pass
        else:
            players.append(x)
            cards.append({x:[]})

def clear():
    i = 100
    while i > 0:
        print(" ")
        i -= 1

def win():
    print("you win!")
    continue_playing = str(input("Would you like to play again? Y/N")).lower()
    if continue_playing.startswith("y"):
        clear()
        cards = []
        players = []
        deck_id = createDeck()
        gameLoop = False
        gameLoop = True
    if continue_playing.startswith("n"):
        gameLoop = False
        print("Thanks for playing!")

def lose():
    print("you lost!")
    continue_playing = str(input("Would you like to play again? Y/N")).lower()
    if continue_playing.startswith("y"):
        clear()
        cards = []
        players = []
        deck_id = createDeck()
        gameLoop = False
        gameLoop = True
    if continue_playing.startswith("n"):
        gameLoop = False
        print("Thanks for playing!")

while gameLoop:
    createPlayers(str(input("Enter your Name:\n")).split(", "))
    for i in players:
        drawCard(deck_id, i, 2)
    gameOngoing = True
    while gameOngoing:
        for player in players:
            turn = player
            while turn == player:
                action = str(input("It is " + player +"'s turn.\n"+player+"'s deck total is "+ str(getPlayerTotal(player)) +"\nAre you going to hit or stand? \nType which action you would like to do. If you need any help type \nhelp.\n"))
                if action.lower() == "hit":
                    hit(player)
                    turn = 0
                    pass
                elif action.lower() == "stand":
                    print(player, "stood.")
                    turn = 0
                    pass
                elif action.lower() == "help":
                    print("debug help")
                else:
                    print("This is not a valid action try again!")
