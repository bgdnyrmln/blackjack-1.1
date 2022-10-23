import random

class Karta:
    #kartes skaitliska sastavdaļa
    def __init__(self,value,suit):
        self.cost = value
        self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'][value-1]
        self.suit = ['♡', '♦', '♣', '♠'][suit]
    #kartes grafiska sastavdaļa    
    def show(self):
        print()
        print('.───────.')
        print(f'| {self.value:<2}    |')
        print('|       |')
        print(f'|   {self.suit}   |')
        print('|       |')
        print(f'|    {self.value:>2} |')
        print('*───────*') 
        print()
    #kartes skaitliskas sastavdaļas apreķināšana(A,J,Q un K situacijās)
    def price(self):
        if self.cost >= 10:
            return 10
        elif self.cost == 1:
            return 11
        return self.cost




class Koloda:
    def __init__(self):
        self.cards = []
    #kartes ģenerācija
    def generate(self):
        for i in range(1, 14):
            for j in range(4):
                self.cards.append(Karta(i, j))
    def draw(self, iteration):
        cards = []
        for i in range(iteration):
            card = random.choice(self.cards)
            self.cards.remove(card)
            cards.append(card)
        return cards
    def count(self):
        return len(self.cards)