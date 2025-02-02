suits = ['hearts', 'diamonds','spades',"clubs"]
ranks = ['9','10','jack','queen','king','ace']

# Find value of cards of the trump [right, left, ace, queen, 10, 9]
trump_value_array = [15, 12, 10, 5, 2, 1, 1]
non_trump_value_array = [7,3,2,1,1,1]

def sister_suit(suit_input):
    # takes string and find is associated with sister suit and returns true or false
    if suit_input == suits[0]:
        sister_suit = suits[1]
    elif suit_input == suits[1]:
        sister_suit = suits[0]
    elif suit_input == suits[2]:
        sister_suit = suits[3]
    elif suit_input == suits[3]:
        sister_suit = suits[2]

    return sister_suit


def evaluate_hand_value(hand):
    # find suit that has highest value

    max_total_suit = []
    total_value = [] 

    hand_trump_output = []
    non_hand_trump_output = []

    for suit in suits:
        hand_trump = [0,0,0,0,0,0,0] 
        hand_trump_value = 0
        non_hand_trump = [0,0,0,0,0,0] 
        non_hand_trump_value = 0

        # Assign trump value for each suit
        for card in hand:
            
            # Trump cards
            if card[0] == 'jack' and card[1] == suit:
                hand_trump[0] = trump_value_array[0]
                hand_trump_value = hand_trump_value + trump_value_array[0]
            if card[0] == 'jack' and card[1] == sister_suit(suit):
                hand_trump[1] = trump_value_array[1]
                hand_trump_value = hand_trump_value + trump_value_array[1]
            if card[0] == 'ace' and card[1] == suit:
                hand_trump[2] = trump_value_array[2]
                hand_trump_value = hand_trump_value + trump_value_array[2]
            if card[0] == 'king' and card[1] == suit:
                hand_trump[3] = trump_value_array[3]
                hand_trump_value = hand_trump_value + trump_value_array[3]
            if card[0] == 'queen' and card[1] == suit:
                hand_trump[4] = trump_value_array[4]
                hand_trump_value = hand_trump_value + trump_value_array[4]
            if card[0] == '10' and card[1] == suit:
                hand_trump[5] = trump_value_array[5]
                hand_trump_value = hand_trump_value + trump_value_array[5]
            if card[0] == '9' and card[1] == suit:
                hand_trump[6] = trump_value_array[6]
                hand_trump_value = hand_trump_value + trump_value_array[6]

            # Non trump card values
            if card[0] == 'ace' and card[1] != suit:
                non_hand_trump[0] = non_hand_trump[0] + non_trump_value_array[0]
                non_hand_trump_value = non_hand_trump_value + non_trump_value_array[0]
            if card[0] == 'king' and card[1] != suit:
                non_hand_trump[1] = non_hand_trump[1] + non_trump_value_array[1]
                non_hand_trump_value = non_hand_trump_value + non_trump_value_array[1]
            if card[0] == 'queen' and card[1] != suit:
                non_hand_trump[2] = non_hand_trump[2] + non_trump_value_array[2]
                non_hand_trump_value = non_hand_trump_value + non_trump_value_array[2]
            if card[0] == 'jack' and card[1] != suit:
                non_hand_trump[3] = non_hand_trump[3] + non_trump_value_array[3]
                non_hand_trump_value = non_hand_trump_value + non_trump_value_array[3]
            if card[0] == '10' and card[1] != suit:
                non_hand_trump[4] = non_hand_trump[4] + non_trump_value_array[4]
                non_hand_trump_value = non_hand_trump_value + non_trump_value_array[4]
            if card[0] == '9' and card[1] != suit:
                non_hand_trump[5] = non_hand_trump[5] + non_trump_value_array[5]
                non_hand_trump_value = non_hand_trump_value + non_trump_value_array[5]

        hand_trump_output.append(hand_trump)
        non_hand_trump_output.append(non_hand_trump) 
        total_value.append(hand_trump_value + non_hand_trump_value)

    max_total_value = max(total_value)
    index_of_best_suit = total_value.index(max_total_value)
    max_total_suit = suits[index_of_best_suit]

    return max_total_value, max_total_suit, hand_trump_output[index_of_best_suit], non_hand_trump_output[index_of_best_suit]


def evaluate_best_card(player_hand, lead_suit, trick_turn, trump_suit):
    # Create running EV tracker
    # If have lead suit only cards in that suit have non 0 value
    # If not lead suit all cards have normal value

    hand_value_list = [] 
    best_card_index = 0
    # If lead play higest EV
    if trick_turn == 0:

        i = 0
        for card in player_hand:
            # Trump cards
            if card[0] == 'jack' and card[1] == trump_suit:
                hand_value_list.append(trump_value_array[0])
            if card[0] == 'jack' and card[1] == sister_suit(trump_suit):
                hand_value_list.append(trump_value_array[1])
            if card[0] == 'ace' and card[1] == trump_suit:
                hand_value_list.append(trump_value_array[2])
            if card[0] == 'king' and card[1] == trump_suit:
                hand_value_list.append(trump_value_array[3])
            if card[0] == 'queen' and card[1] == trump_suit:
                hand_value_list.append(trump_value_array[4])
            if card[0] == '10' and card[1] == trump_suit:
                hand_value_list.append(trump_value_array[5])
            if card[0] == '9' and card[1] == trump_suit:
                hand_value_list.append(trump_value_array[6])

            # Non trump card values
            if card[0] == 'ace' and card[1] != trump_suit:
                hand_value_list.append(non_trump_value_array[0])
            if card[0] == 'jack' and card[1] != trump_suit:
                hand_value_list.append(non_trump_value_array[1])
            if card[0] == 'king' and card[1] != trump_suit:
                hand_value_list.append(non_trump_value_array[2])
            if card[0] == 'queen' and card[1] != trump_suit:
                hand_value_list.append(non_trump_value_array[3])
            if card[0] == '10' and card[1] != trump_suit:
                hand_value_list.append(non_trump_value_array[4])
            if card[0] == '9' and card[1] != trump_suit:
                hand_value_list.append(non_trump_value_array[5])



            i += 1

        # Evalue hand list highest value and index of that value
        max_hand_list = max(hand_value_list)
        best_card_index = hand_value_list.index(max_hand_list)
        lead_suit = player_hand[best_card_index][1]
        trick_turn += 1
        
    # If not lead play highest of lead suit or if no lead suit play highest ev card
    elif trick_turn != 0:

        has_lead_suit = 0
        
        # Does the player have a card in the suit lead
        for card in player_hand:
            if card[1] == lead_suit:
                has_lead_suit = 1
        
        for card in player_hand:
            if has_lead_suit:
                # Trump cards
                if card[1] == lead_suit:
                    if card[0] == 'jack' and card[1] == trump_suit:
                        hand_value_list.append(trump_value_array[0])
                    if card[0] == 'jack' and card[1] == sister_suit(trump_suit):
                        hand_value_list.append(trump_value_array[1])
                    if card[0] == 'ace' and card[1] == trump_suit:
                        hand_value_list.append(trump_value_array[2])
                    if card[0] == 'king' and card[1] == trump_suit:
                        hand_value_list.append(trump_value_array[3])
                    if card[0] == 'queen' and card[1] == trump_suit:
                        hand_value_list.append(trump_value_array[4])
                    if card[0] == '10' and card[1] == trump_suit:
                        hand_value_list.append(trump_value_array[5])
                    if card[0] == '9' and card[1] == trump_suit:
                        hand_value_list.append(trump_value_array[6])

                    # Non trump card values
                    if card[0] == 'ace' and card[1] != trump_suit:
                        hand_value_list.append(non_trump_value_array[0])
                    if card[0] == 'jack' and card[1] != trump_suit:
                        hand_value_list.append(non_trump_value_array[1])
                    if card[0] == 'king' and card[1] != trump_suit:
                        hand_value_list.append(non_trump_value_array[2])
                    if card[0] == 'queen' and card[1] != trump_suit:
                        hand_value_list.append(non_trump_value_array[3])
                    if card[0] == '10' and card[1] != trump_suit:
                        hand_value_list.append(non_trump_value_array[4])
                    if card[0] == '9' and card[1] != trump_suit:
                        hand_value_list.append(non_trump_value_array[5])
                else:
                    hand_value_list.append(0)
            else:
                # Trump cards
                if card[0] == 'jack' and card[1] == trump_suit:
                    hand_value_list.append(trump_value_array[0])
                if card[0] == 'jack' and card[1] == sister_suit(trump_suit):
                    hand_value_list.append(trump_value_array[1])
                if card[0] == 'ace' and card[1] == trump_suit:
                    hand_value_list.append(trump_value_array[2])
                if card[0] == 'king' and card[1] == trump_suit:
                    hand_value_list.append(trump_value_array[3])
                if card[0] == 'queen' and card[1] == trump_suit:
                    hand_value_list.append(trump_value_array[4])
                if card[0] == '10' and card[1] == trump_suit:
                    hand_value_list.append(trump_value_array[5])
                if card[0] == '9' and card[1] == trump_suit:
                    hand_value_list.append(trump_value_array[6])

                # Non trump card values
                if card[0] == 'ace' and card[1] != trump_suit:
                    hand_value_list.append(non_trump_value_array[0])
                if card[0] == 'jack' and card[1] != trump_suit:
                    hand_value_list.append(non_trump_value_array[1])
                if card[0] == 'king' and card[1] != trump_suit:
                    hand_value_list.append(non_trump_value_array[2])
                if card[0] == 'queen' and card[1] != trump_suit:
                    hand_value_list.append(non_trump_value_array[3])
                if card[0] == '10' and card[1] != trump_suit:
                    hand_value_list.append(non_trump_value_array[4])
                if card[0] == '9' and card[1] != trump_suit:
                    hand_value_list.append(non_trump_value_array[5])

        max_hand_list = max(hand_value_list)
        best_card_index = hand_value_list.index(max_hand_list)
        trick_turn += 1
        

                
    
    return trick_turn, hand_value_list, best_card_index, lead_suit
        

