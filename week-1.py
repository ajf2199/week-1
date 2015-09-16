#Aaron Febuary
#Datamining the City
#Week-1 

import random

gameStake = 50  
cards = range(10)


class Player:
    playerID = 0
    pot = 0.0
    lastCard = 0    
    
       
    def __init__(self, inputID, startingPot):
        self.playerID = inputID
        self.pot = startingPot
        
      
    def play(self, dealerCard):
        self.lastCard = random.choice(cards)
             
        if self < dealerCard:
            self.pot -= gameStake
            return 'player ' + str(self.playerID) + ' Lose, ' + str(self.lastCard) + ' vs ' + str(dealerCard)
        else:
            self.pot += gameStake
            return 'player ' + str(self.playerID) + ' Win, ' + str(self.lastCard) + ' vs ' + str(dealerCard)
    
    def returnPot(self):
        return self.pot
    
    def returnID(self):
        return self.playerID
       


def playHand(players):
    
    for player in players:
        print player.play (random.choice(cards))
       
def checkBalances(players):
    
    for player in players:
        print 'player ' + str(player.returnID()) + ' has $' + str(player.returnPot()) + ' left.' 
        
       
players = []      



for i in range(5):
    players.append(Player(i, 500))

for i in range(10):
    print ''
    print 'start game ' + str(i)
    playHand(players)

print ''
print 'game results:'
checkBalances(players)
