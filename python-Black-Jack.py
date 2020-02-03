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

        if amount > self.balance:
            print( f"Sorry you can not bet that much. You can only bet ${self.balance}.")
            amount = int(input('Enter another bet'))
            self.check_bet(amount)

        if self.balance == 0:
            print(f"Game over. Sorry you have run out of money.")
            return play = False
        else:
            return ('You have placed the bet ${amount}. May the cards be in your favor.')


    def value_of_hand(self, card1, card2):
        for suit, face, value in card
#I want value of each card and then sum it.


class Deck:
""" The Deck object contains a deck of cards made of suits, faces and values
- Ace is 1 here but will be tested in the program to see if 11 is better during play
    """
    suits = ["Diamond", "Club", "Heart", "Spade"]
    faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    value = [1,2,3,4,5,6,7,8,9,10,10,10,10]

#generate a deck and return a shuffled deck to play
    def shuffled_deck(self):
    """
     This method creates and shuffles a deck of cards
        :param

        :return: (list)
        """
        deck = []
        for suit in suits:
            for i in range(0, len(faces)+1):
                card = (suit, faces[i], value[i])
                deck.append(card)
            shuffled_deck = random.sample(deck, k = 52)
            return shuffled_deck


def main():

    #setup game - find out player's name and amount with which they wish to gamble
    print("Welcome to Black Jack!")
    player1 = input("What is your name?")
    bankroll = int(input("How many chips in dollars do you want to buy?")
    card_shark = Player(player1, bankroll)

    #control flow
    play = True

    while play:
    #take bet
        bet = int(input("How much do you want to bet?"))
        #verify player has enough money to bet
        card_shark.check_bet(bet)

    #get deck and deal/print result fo deal

    #input from user 3rd card or not

    #deal or not

    #computer turn

    #win conditions

if__name__='__main__':
    main()