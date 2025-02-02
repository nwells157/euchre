import evaluate_hand

trump_value_array = [15,14,13,12,11,10,9]
non_trump_value_array = [6,5,4,3,2,1]
suits = ["clubs", 'diamonds', 'hearts', 'spades']

def choose_card_to_play(player_hand, lead_suit, trick_turn, trump_suit):
    # Need to output new player hand, card to be put onto table and iterate trick_turn
    trick_turn, hand_value_list, best_card_index, lead_suit = evaluate_hand.evaluate_best_card(player_hand, lead_suit, trick_turn, trump_suit)
    
    #print(f'With {trump_suit} being trump and the player having {player_hand} the best card to play is {player_hand[best_card_index]}')
    
    played_card = player_hand[best_card_index]
    player_hand.remove(player_hand[best_card_index])



    return trick_turn, player_hand, played_card, lead_suit

def find_trick_winner(tabled_cards, player_order, lead_suit, trump_suit):

    tabled_card_list = []
    trick_winner = ''

    # If a trump was lead
    if lead_suit == trump_suit:
        for card in tabled_cards:
            # Trump cards
            if card[0] == 'jack' and card[1] == trump_suit:
                tabled_card_list.append(trump_value_array[0])
            elif card[0] == 'jack' and card[1] == evaluate_hand.sister_suit(trump_suit):
                tabled_card_list.append(trump_value_array[1])
            elif card[0] == 'ace' and card[1] == trump_suit:
                tabled_card_list.append(trump_value_array[2])
            elif card[0] == 'king' and card[1] == trump_suit:
                tabled_card_list.append(trump_value_array[3])
            elif card[0] == 'queen' and card[1] == trump_suit:
                tabled_card_list.append(trump_value_array[4])
            elif card[0] == '10' and card[1] == trump_suit:
                tabled_card_list.append(trump_value_array[5])
            elif card[0] == '9' and card[1] == trump_suit:
                tabled_card_list.append(trump_value_array[6])
            else:
                tabled_card_list.append(0)

        max_tabled_card_list = max(tabled_card_list)
        index_of_winner = tabled_card_list.index(max_tabled_card_list)
        trick_winner = player_order[index_of_winner]

    elif lead_suit != trump_suit:
        for card in tabled_cards:
            # Trump cards
            if card[1] == lead_suit:
                if card[0] == 'jack' and card[1] == trump_suit:
                    tabled_card_list.append(trump_value_array[0])
                if card[0] == 'jack' and card[1] == evaluate_hand.sister_suit(trump_suit):
                    tabled_card_list.append(trump_value_array[1])
                if card[0] == 'ace' and card[1] == trump_suit:
                    tabled_card_list.append(trump_value_array[2])
                if card[0] == 'king' and card[1] == trump_suit:
                    tabled_card_list.append(trump_value_array[3])
                if card[0] == 'queen' and card[1] == trump_suit:
                    tabled_card_list.append(trump_value_array[4])
                if card[0] == '10' and card[1] == trump_suit:
                    tabled_card_list.append(trump_value_array[5])
                if card[0] == '9' and card[1] == trump_suit:
                    tabled_card_list.append(trump_value_array[6])

                # Non trump card values
                if card[0] == 'ace' and card[1] != trump_suit:
                    tabled_card_list.append(non_trump_value_array[0])
                if card[0] == 'jack' and card[1] != trump_suit:
                    tabled_card_list.append(non_trump_value_array[1])
                if card[0] == 'king' and card[1] != trump_suit:
                    tabled_card_list.append(non_trump_value_array[2])
                if card[0] == 'queen' and card[1] != trump_suit:
                    tabled_card_list.append(non_trump_value_array[3])
                if card[0] == '10' and card[1] != trump_suit:
                    tabled_card_list.append(non_trump_value_array[4])
                if card[0] == '9' and card[1] != trump_suit:
                    tabled_card_list.append(non_trump_value_array[5])
            else:
                tabled_card_list.append(0)

        max_tabled_card_list = max(tabled_card_list)
        index_of_winner = tabled_card_list.index(max_tabled_card_list)
        trick_winner = player_order[index_of_winner]

    return trick_winner

    # If a non trump was lead
            
