import numpy as np
import random
import csv

import evaluate_hand
import turn_controller
import bid_logic
import game_logic

players = []
players_data = []

# Define suits and ranks
suits = ["clubs", 'diamonds', 'hearts', 'spades']
ranks = ['9','10','jack','queen','king','ace']
players_array = ['player 1', 'player 2', 'player 3', 'player 4']


# Create the deck
deck = [(rank,suit) for suit in suits for rank in ranks]

# 24 cards in the deck
total_cards = len(deck) 

# Shuffle the deck
random.shuffle(deck)

# Deal the cards by assigning the player a dictionary of their hand in a list 
players = {f'player {i+1}': [] for i in range(4)}
players_data = {f'player {i+1}': [] for i in range(4)}


# Deal the deck 
for i in range(6):
    for player in players:
        players[player].append(deck.pop())

# Evaluate player n's hand at a time
for player in players:
    max_total_value, max_total_suit, hand_trump, non_hand_trump = evaluate_hand.evaluate_hand_value(players[player])

    print(f'{player} has {players[player]} with a total value {max_total_value} with trump values {hand_trump} and non trump values {non_hand_trump} and would like to go in {max_total_suit}')
    players_data[player].append({'expected_value': max_total_value})
    players_data[player].append({"expected_suit": max_total_suit})

team_one_score = 0
team_two_score = 0

# Start games
for games in range(1):

    # Bid Phase
    print("\nBid Phase")
    current_bid = 2;

    # Random start of turn
    turn_counter = random.randint(1,4);
    bid_owner = ""
    trump_suit = ""

    i = 0
    for player in players:
        
        # Set player turn and iterate turn_counter by 1
        player_turn, turn_counter = turn_controller.find_player_turn(turn_counter)

        # Bid logic, player whos turn it is looks at its EV then picks highest bid it can achieve
        current_bid, bid_owner, trump_suit = bid_logic.bid_turn(current_bid,players_data[player_turn][0]['expected_value'],players_data[player_turn][1]['expected_suit'], bid_owner, player_turn, trump_suit )
        print(f'It is player {player_turn}s turn where {bid_owner} currently has the highest bid with a bid of {current_bid} in {trump_suit}. The next turn is player {turn_counter}')
        i = i + 1



    # Bidding gets turn counter back to dealer so iterate by one to be left of dealer
    lead_suit = ''

    # Game Phase
    print("\nGame Phase")
    # Play all 6 cards
    for turn in range(6):

        # Trick turn reset each round    
        tabled_card = []
        turn_order = []
        trick_turn = 0

        # Go around table
        for player in players:

            player_turn, turn_counter = turn_controller.find_player_turn(turn_counter)
            # Lead card played

            turn_order.append(player_turn)
            trick_turn, hand_value_list, played_card, lead_suit = game_logic.choose_card_to_play(players[player_turn], lead_suit, trick_turn, trump_suit)

            tabled_card.append(played_card)
            print(f'{player_turn} played {played_card} with the lead being {lead_suit} with all cards on table being {tabled_card}')

        trick_winner = game_logic.find_trick_winner(tabled_card, turn_order, lead_suit, trump_suit)
        
        if trick_winner == 'player 1' or trick_winner == 'player 3':
            team_one_score += 1
        elif trick_winner == 'player 2' or trick_winner == 'player 4':
            team_two_score += 1

        # Change turn
        print(trick_winner)
        turn_counter = turn_controller.change_turn_to_winner(trick_winner)


        print(f'Team one score: {team_one_score} and Team two score: {team_two_score}')



with open('player_hand.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['rank','suit']) # Write header
    writer.writerows(players['player 1']) # Write player 1's hand

print("\n")