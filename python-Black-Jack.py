#Black Jack Game

#use random library to generate a shuffled deck of cards

import random

#classes: player has bank account and hand

class Player():
    """ Player object contains black jack info for each player - bank account and hand info
    three key variables:
    1. player's hand - list
    2. player's name str
    3. initial bank balance the player starts the game with
    """

    hand = []

    def __init__(self, name, balance):


        self.name = name
        self.balance = balance



    def winnings(self, amount):
        """
        This method manages the winnings of player.

        :param
        amount: (int) The amount the player won
        :return: (string)
        """

        self.balance += amount
        return "Winnings added to your account"


    def lost_bet (self, amount):
        """
        The method manages the losses of the player.
        :param
        amount: (int) amount player lost
        :return: (str)
        """

        self.balance -= amount
        return "Lost bet deducted from your account"


    def check_bet(self, amount):
        """
        This method verifies if the bet can be covered by bank balance
        :param
        amount: (int)
        :return: (boolean)
        """

        if amount >= self.balance:
            return False
        else:
            return True


    def value_of_hand(self, hand):
        """
        This method sums the value of the hand
        :param
        hand: (list) player's hand of cards
        :return: (int)
        """
        sum = 0;
        for card in hand:
            sum += card[2]
        return sum



class Deck():
    """
    The Deck object contains a deck of cards made of suits, faces and values
    - Ace is 1 here but will be tested in the program to see if 11 is better during play
    """


    def __init__(self):
        self.suits = ["Diamond", "Club", "Heart", "Spade"]
        self.faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#generate a deck and return a shuffled deck to play
    def shuffled_deck(self):
        """

        This method creates and shuffles a deck of cards
        :param

        :return: (list)

         """
        deck = []
        for suit in self.suits:
            for i in range(0, len(self.faces)):
                card = (suit, self.faces[i], self.value[i])
                deck.append(card)
        random_deck = random.sample(deck, k=52)
        return random_deck


def main():

    #setup game - find out player's name and amount with which they wish to gamble
    print("Welcome to Black Jack!")
    player1 = input("What is your name? ")
    bankroll = int(input("How many chips in dollars do you want to buy? "))
    card_shark = Player(player1, bankroll)
    computer = 'dealer'
    dealer = Player(computer, 10000000)

    #manage game flow
    play = True

    while play:
        if card_shark.balance == 0:
            play = False

    #take bet
        bet = int(input("How much do you want to bet? "))
        #verify player has enough money to bet
        valid_bet = card_shark.check_bet(bet)
        while  not valid_bet:
            print(f"Sorry you can not bet that much. You can only bet ${card_shark.balance}.")
            bet = int(input('Enter another bet'))
            card_shark.check_bet(bet)
        print (f'You have placed the bet ${bet}. May the cards be in your favor.')

    #get deck and deal/print result fo deal
        deck = Deck()
        shoe_deck = deck.shuffled_deck()
        card_shark.hand.append(shoe_deck.pop())
       # dealer.hand.append(shoe_deck.pop())
        #card_shark.hand.append(shoe_deck.pop())
        print('dealer:', dealer.hand)
        print('cardshark', card_shark.hand)



    #input from user 3rd card or not

    #deal or not

    #computer turn

    #win conditions

    print("Game over. Sorry you have run out of money.")

if __name__ =='__main__':
    main()