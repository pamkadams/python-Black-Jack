# Black Jack Game

# use random library to generate a shuffled deck of cards

import random


# classes: player has bank account and hand

class Player():
    """ Player object contains black jack info for each player - bank account and hand info
    three key variables:
    1. player's hand - list
    2. player's name str
    3. initial bank balance the player starts the game with
    """

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.hand = []

    def winnings(self, amount):
        """
        This method manages the winnings of player.

        :param
        amount: (int) The amount the player won
        :return: (string)
        """

        self.balance += amount
        return "Winnings added to your account"

    def lost_bet(self, amount):
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
            return False
        else:
            return True

    def value_of_hand(self):
        """
        This method sums the value of the hand including the ace being worth 1 vs. 11
        :param
        hand: (list) player's hand of cards
        :return: (int)
        """
        sum = 0
        alt_sum = False
        for card in self.hand:
            if card[1] == 'A':
                alt_sum = True

            sum += card[2]

        if sum == 21:
            return sum
        elif alt_sum and sum - 1 + 11 <= 21:
            return sum - 1 + 11
        else:
            return sum


class Deck():
    """
    The Deck object contains a deck of cards made of suits, faces and values
    - Ace is 1 here but will be tested in the program to see if 11 is better during play
    The initialization of the object will create a random deck of cards
    """

    def __init__(self):
        self.suits = ["Diamond", "Club", "Heart", "Spade"]
        self.faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        deck = []
        for suit in self.suits:
            for i in range(0, len(self.faces)):
                card = (suit, self.faces[i], self.value[i])
                deck.append(card)
        self.random_deck = random.sample(deck, k=52)

    def deal_one(self):
        """
        This method deals one card from the deck.
        :return: card which is a tuple (suit, face, value)
        """
        return self.random_deck.pop()

def win_conditions(computer, player, bet):

    if player.value_of_hand() > 21:
        player.lost_bet(bet)
        print(f'{player.name} loses. Your bank account is now ${player.balance}.')
    elif computer.value_of_hand() > 21:
        player.winnings(bet)
        print(f'Congradulations! Your bank account is now ${player.balance}.')
    elif player.value_of_hand() > computer.value_of_hand():
        player.winnings(bet)
        print(f'Congradulations! Your bank account is now ${player.balance}.')
    elif player.value_of_hand() < computer.value_of_hand():
        player.lost_bet(bet)
        print(f'{player.name} loses. Your bank account is now ${player.balance}.')
    else:
        print("It is a tie. No money changes hand.")

def main():
    # setup game - find out player's name and amount with which they wish to gamble
    print("Welcome to Black Jack!")
    player1 = input("What is your name? ")
    bankroll = int(input("How many chips in dollars do you want to buy? "))
    card_shark = Player(player1, bankroll)
    computer = 'dealer'
    dealer = Player(computer, 10000000)

    # manage game flow
    play = True

    while play:
        if card_shark.balance == 0:
            play = False

        # take bet
        bet = int(input("How much do you want to bet? "))
        # verify player has enough money to bet
        valid_bet = card_shark.check_bet(bet)
        # bet must valid so valid_bet if false creates a loop getting the player to bet a legal amount
        while not valid_bet:
            print(f"Sorry you can not bet that much. You can only bet ${card_shark.balance}.")
            bet = int(input('Enter another bet'))
            card_shark.check_bet(bet)
        print(f'You have placed the bet ${bet}. May the cards be in your favor.')

        # generate a deck and deal/print result fo deal
        deck = Deck()
        card_shark.hand.append(deck.deal_one())
        dealer.hand.append(deck.deal_one())
        card_shark.hand.append(deck.deal_one())
        print('dealer:', dealer.hand)
        print(f'{player1} hand: {card_shark.hand} with value of {card_shark.value_of_hand()}')

        # input from user asking about a 3rd card or not
        another_card = input('Do you want a third card? y/n ')
        if another_card == "y":
            card_shark.hand.append(deck.deal_one())
        print(f"{player1}'s cards are worth {card_shark.value_of_hand()} with this hand: {card_shark.hand}")
        # dealer's turn for additional cards
        while dealer.value_of_hand() < 17:
            dealer.hand.append(deck.deal_one())
        print(f"dealer's hand is {dealer.hand} with a value {dealer.value_of_hand()}")

        win_conditions(dealer, card_shark, bet)
        # check win conditions win conditions


        if card_shark.balance == 0:
            play = False
        else:
            card_shark.hand = []
            dealer.hand = []

    print("Game over. Sorry you have run out of money.")


if __name__ == '__main__':
    main()
