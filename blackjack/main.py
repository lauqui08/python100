import random

card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_card = []
dealer_card = []


# deal a card function
def deal_card():
    """This function will return a card from deck"""
    return random.choice(card)


# check the winner of the game
def check_winner(player_card, dealer_card):
    """This will print the result of the game"""
    print(f"Your final hand: {player_card}")
    print(f"Computer's final hand: {dealer_card}")
    if sum(player_card) > 21:
        print("Dealer win")
    else:
        if sum(dealer_card) > 21 or sum(player_card) > sum(dealer_card):
            print("Player win")
        elif sum(player_card) == sum(dealer_card):
            print("Draw")
        else:
            print("Dealer win")


def play_black_jack():
    print(f"Your cards: {player_card}")
    print(f"Computer's first card: {dealer_card[0]}")

    # The player where ask if he/she want another card from the deck
    get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    # If the player agree to pull another card from the deck
    if get_another_card.lower() == "y":
        # Player will draw another card from the deck
        player_card.append(deal_card())
        # If the sum of the players deck is greater than 21
        if sum(player_card) > 21:
            # Dealer wins
            check_winner(player_card, dealer_card)
        else:
            play_black_jack()
    elif get_another_card.lower() == "n":
        # dealer_card.append(deal_card())
        if sum(dealer_card) < sum(player_card) and sum(dealer_card) <= 15:
            dealer_card.append(deal_card())
    else:
        print("Invalid command!")

    check_winner(player_card, dealer_card)


is_playing = True
while is_playing:
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        player_card = [deal_card(), deal_card()]
        dealer_card = [deal_card(), deal_card()]
        play_black_jack()
    else:
        is_playing = False