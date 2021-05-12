import requests as rq
import json
import time
import random

URL = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
cards = []
players = []
winners = []
stand = []
stand_totals = []
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

createPlayers(str(input("Enter your Name:\n")).split(", "))
for i in players:
    drawCard(deck_id, i, 2)
gameOngoing = True
while gameOngoing:
    if len(players) == 1 and len(stand) < 1:
        player = players[0]
        if getPlayerTotal(player) < 21 and getPlayerTotal(player) >= 0:
            if len(player) > 0:
                action = str(input("It is " + player +"'s turn.\n"+player+"'s deck total is "+ str(getPlayerTotal(player)) +"\nAre you going to hit or stand? \nType which action you would like to do. If you need any help type \nhelp.\n"))
                if action.lower() == "hit":
                    hit(player)
                    pass
                elif action.lower() == "stand":
                    print(str(player), "stood.")
                    cpu_hand = round(random.randint(13, 21))
                    if cpu_hand > getPlayerTotal(player):
                        print("Game Over! The CPU had more than you. \nCPU: "+str(cpu_hand)+ " "+player+": "+str(getPlayerTotal(player)))
                        gameOngoing = False
                    elif cpu_hand < getPlayerTotal(player):
                        print("Game Over! You had more than the CPU!\nCPU: "+str(cpu_hand)+ " "+player+": "+str(getPlayerTotal(player)))
                        gameOngoing = False
                    elif cpu_hand == getPlayerTotal(player):
                        print("Game Over! You drew with the CPU!\nCPU: "+str(cpu_hand)+ " "+player+": "+str(getPlayerTotal(player)))
                        gameOngoing = False
                elif action.lower() == "help":
                    print("debug help")
                else:
                    print("This is not a valid action try again!")
        elif getPlayerTotal(player) == 21:
            print("Game Over! You got blackjack.")
            gameOngoing = False
        else:
            print("Game Over! You Busted.")
            gameOngoing = False
    else:
        if len(players) > 0:
            for player in players:
                turn = player
                while turn == player:
                    if getPlayerTotal(player) < 21 and getPlayerTotal(player) >= 0:
                        action = str(input("It is " + player +"'s turn.\n"+player+"'s deck total is "+ str(getPlayerTotal(player)) +"\nAre you going to hit or stand? \nType which action you would like to do. If you need any help type \nhelp.\n"))
                        if action.lower() == "hit":
                            hit(player)
                            turn = 0
                            pass
                        elif action.lower() == "stand":
                            players.remove(player)
                            stand.append(player)
                            turn = 0
                            pass
                        elif action.lower() == "help":
                            print("debug help")
                        else:
                            print("This is not a valid action try again!")
                    elif getPlayerTotal(player) == 21:
                        print("Game Over! "+player+" got blackjack.")
                        gameOngoing = False
                    elif getPlayerTotal(player) > 21:
                        print("Uh oh "+player+"! You Busted.")
                        turn = 0
                        players.remove(player)
        elif len(stand) > 0:
            for player in stand:
                stand_totals.append(getPlayerTotal(players)
            stand_totals.sort()
            for p in stand:
                if getPlayerTotal(p) == stand_totals[len(stand_totals)-1]:
                    print(p+" won! They had the highest hand. \n")
                    gameOngoing = False
