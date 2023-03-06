import random 

SUITS = ["Diamonds", "Hearts", "Clubs", "Spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Quenn", "King", "Ace"]

class Card():
  """Class to make and return cards"""
  def __init__(self, new_rank, new_suit):
    self.rank = new_rank
    self.suit = new_suit

  def __repr__(self):
    return self.rank + " of " + self.suit
  
deck = []
for suit in SUITS:
  for rank in RANKS:
    deck.append(Card(rank, suit))
random.shuffle(deck)

p1 = deck[0:10]

ranks_list = {}
for rank in RANKS:
  ranks_list[rank] = 0

for card in p1:
  ranks_list[card.rank] += 1

ranks_list = ranks_list.values()

#replace some of the if.elif statements to make code work
if ranks_list == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1] and flush:
    print("royal flush")
elif straight flush:
    print("straight flush")
elif ranks_list.count(1) == 4:
    print("four of a kind")
elif full house:
    print("full house")
elif flush:
    print("flush")
elif straight:
    print("straight")
elif rank_list.count(3) == 1:
  print("Three of a kind!!!")
elif two_pair:
    print("two pair")
if rank_list.count(2) == 1:
  print("one pair!!!")
else:
  print("Garbage")

#fancy code to check hand amount
