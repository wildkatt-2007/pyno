# Code for both human and bot players

#Characteristics of a playable character

class Player:
  def __init__(self,Id,Nature,Hand):
    self.id = Id     # Var for identifying player
    self.nature = Nature # =true for human, =false for bot
    self.hand = Hand #List of cards...To be broadcast to and from distributor

  def playCard(self,indexOfCard):
    card = self.hand[indexOfCard] #The card (string) played
    self.hand.remove(card)
    return card
    
  def displayHand(self):
    return self.hand #Can be modified to a func if gui is added
    
  def penalty(self,penaltyType):
  #Le I think this whole method should be implemented on gameLogic file because removit card from deck should not be a work of player....
    if penaltyType == "+2":
      for t in range(1,2):
       _player.self.hand.append(deckCards[0])
       deckCards.remove(deckCards[0])
       
    if penaltyType == "+4":
      for t in range(1,4):
        self.hand.append(deckCards[0])
        deckCards.remove(deckCards[0])

#Creation of human players
listOfPlayers = [Player(i,True,players[i]) for i in range(numberOfHumanPlayers)]
#--------------–--------------------+----

# main Game Logic

import random

# --- DATA ---
zeroes = 4
ones = 8
twos = 8
threes = 8
fours = 8
fives = 8
sixes = 8
sevens = 8
eights = 8
nines = 8
skips = 8
reverses = 8
plusTwos = 8
plusFours = 4 # no colors
wildCards = 4 # no colors
# --- DATA ---

# card code tokens
cardTypes = ["0", "1", "1", "2", "2", "3","3", "4", "4", "5", "5", "6", "6", "7", "7", "8", "8", "9", "9", "Skip", "Skip", "Reverse", "Reverse", "+2", "+2", "+4", "W"]
colors = ["R", "Y", "B", "G"]

numberOfHumanPlayers = 4 #The value just for testing purpose

# cards in each players hand
playerOneHand = []
playerTwoHand = []
playerThreeHand = []
playerFourHand = []
# list for code comfortability in looping
players = [playerOneHand, playerTwoHand, playerThreeHand, playerFourHand]

deckCards = [] # the cards in the deck

# shuffle the cards and place them in deck
def gameShuffle():
    for cardType in cardTypes:
        for color in colors:
            deckCards.append(f"{color}{cardType}")
    random.shuffle(deckCards)        

# serve 7 cards for each player one by one
def distribute():
    for i in range(0,7):
        for player in players:
            player.append(cards[0])
            deckCards.remove(cards[0])

# Helps everyone to take any number of cards from deck easily
def takeCard(_player,numberOfCard):
  pass
# This function collides with the established penalty() method of class...
  
# method to translate card codes into strings that is readable
def translate(cardCode):
    if cardCode.startswith("R"):
        color = "Red "
    if cardCode.startswith("Y"):
        color = "Yellow "
    if cardCode.startwith("B"):
        color = "Blue "
    if cardCode.startswith("G"):
        color = "Green "
    if cardCode.endswith("1"):
        cardValue = "One"
    if cardCode.endswith("2"):
        cardValue = "Two"
    if cardCode.endswith("3"):
        cardValue = "Three"
    if cardCode.endswith("4"):
        cardValue = "Four"
    if cardCode.endswith("5"):
        cardValue = "Five"
    if cardCode.endswith("6"):
        cardValue = "Six"
    if cardCode.endswith("7"):
        cardValue = "Seven"
    if cardCode.endswith("8"):
        cardValue = "Eight"
    if cardCode.endswith("9"):
        cardValue = "Nine"
    if cardCode.endswith("Skip"):
        cardValue = "Skip"
    if cardCode.endswith("Reverse"):
        cardValue = "Reverse"
    if cardCode.endswith("+2"):
        cardValue = "Plus Two"
    if cardCode.endswith("+4"):
        cardValue = "Plus Four"
        color = ""
    if cardCode.endswith("W"):
        cardValue = "Wild"
        color = ""
        
    cardName = str(str(color) + str(cardValue) + " Card")
    return cardName

gameShuffle()
distribute()

#Which card is player playing? = method playCard()
#List of individual players? = listOfPlayers -> a list
#