# Code inspiration for structure/syntax came from:
# https://github.com/gsamarakoon/Fun-projects-for-Python/blob/master/A%20game%20of%20BlackJack.ipynb
# and
# https://www.askpython.com/python/examples/blackjack-game-using-python
# There are elements from these sources I chose not to use, such as the chips/betting.

import random

# create a dictionary to store the values of each card
card_values = {
    'Ace': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10
}

# create a list of card suits
card_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# create a list to hold the deck of cards
deck = []

# create a function to create the deck of cards
def create_deck():
    for suit in card_suits:
        for card, value in card_values.items():
            deck.append((card + ' of ' + suit, value))

# create a function to shuffle the deck
def shuffle_deck():
    random.shuffle(deck)

# create a function to deal a card
def deal_card(hand):
    card = deck.pop()
    hand.append(card)

# create a function to calculate the value of a hand
def calculate_hand(hand):
    total = 0
    aces = 0
    for card in hand:
        total += card[1]
        if card[0].startswith('Ace'):
            aces += 1
    while total <= 11 and aces > 0:
        total += 10
        aces -= 1
    return total

# create a function to play the game
def play_game():
    print('Welcome to Blackjack!')
    create_deck()
    shuffle_deck()
    player_hand = []
    dealer_hand = []
    deal_card(player_hand)
    deal_card(dealer_hand)
    deal_card(player_hand)
    deal_card(dealer_hand)
    print('Player hand: ', player_hand[0][0], 'and', player_hand[1][0])
    print('Dealer hand: ', dealer_hand[0][0], 'and one face-down card')
    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)
    while player_total < 21:
        action = input('Would you like to hit or stand? ')
        if action == 'hit':
            deal_card(player_hand)
            print('Player hand: ', end='')
            for card in player_hand:
                print(card[0], end=', ')
            print('')
            player_total = calculate_hand(player_hand)
            if player_total >= 21:
                break
        elif action == 'stand':
            break
    if player_total > 21:
        print('Bust! You lose.')
        return
    print('Dealer hand: ', end='')
    for card in dealer_hand:
        print(card[0], end=', ')
    print('')
    while dealer_total < 17:
        deal_card(dealer_hand)
        dealer_total = calculate_hand(dealer_hand)
        print('Dealer hand: ', end='')
        for card in dealer_hand:
            print(card[0], end=', ')
        print('')
    if dealer_total > 21:
        print('Dealer bust! You win!')
    elif dealer_total > player_total:
        print('Dealer wins!')
    elif dealer_total < player_total:
        print('You win!')
    else:
        print('A tie! Dealer wins!')

# start the game
while True:
    play_game()
    answer = input("Would you like to play again? (y/n): ")
    if answer != 'y':
        break
        
#restart the game
replay_game()