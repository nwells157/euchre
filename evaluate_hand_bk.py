suits = ['hearts', 'diamonds','spades',"clubs"]
ranks = ['9','10','jack','queen','king','ace']



def sister_suit(suit_input):
    if suit_input == suits[0]:
        sister_suit = suits[1]
    elif suit_input == suits[1]:
        sister_suit = suits[0]
    elif suit_input == suits[2]:
        sister_suit = suits[3]
    elif suit_input == suits[3]:
        sister_suit = suits[2]

    return sister_suit


def evaluate(hand):


         
    # print(f'The players hand is {hand}')

    total_cards_in_suit = []

    # Choose best suit

    # Find total amount of cards in the same suit
    for suit in suits:
        i = 0
        for card in hand:
            # Find left bowers with sister suit function
            if card[1] == suit or (card[0]=='jack' and suit == sister_suit(card[1])):
                i = i + 1
                
        total_cards_in_suit.append(i)


    largest_same_suit_cards = max(total_cards_in_suit)
    amount_suit_index = []

    i = 0
    tied_largest_same_suit_cards = 0
    # if there are 2 suits that have same number of cards need to loop through to do
    for suit in suits:
        if total_cards_in_suit[i] == largest_same_suit_cards:
            amount_suit_index.append(1)
            tied_largest_same_suit_cards = tied_largest_same_suit_cards + 1
        else:   
            amount_suit_index.append(0)
        i = i + 1
        
    # For when the player has multiple suits with the sam eamount of trump
    if tied_largest_same_suit_cards > 1:
        i = 0
        tied_suits = []
        for suit in suits:
            if amount_suit_index[i] == 1:
                tied_suits.append(suit)
            i = i + 1
        # print(f'The suits tied with {largest_same_suit_cards} cards of the same suit are {tied_suits}')

        # Temp here, needs more logic for multiple best suits to choose between
        best_suit = suits[amount_suit_index.index(1)]

    # When the player has one suit with the most trump     
    else:
        best_suit = suits[amount_suit_index.index(1)]
        # print(f'Largest trump suit is {best_suit} with {largest_same_suit_cards} trump\n')


    # Find value of cards of the trump [right, left, ace, queen, 10, 9]
    trump_value_array = [10, 8, 5, 2, 1, 1]

    hand_trump = [0,0,0,0,0,0] 
    hand_trump_value = 0

    for card in hand:
        # print(card)
        if card[0] == 'jack' and card[1] == best_suit:
            hand_trump[0] = trump_value_array[0]
            hand_trump_value = hand_trump_value + trump_value_array[0]
        if card[0] == 'jack' and card[1] == sister_suit(best_suit):
            hand_trump[1] = trump_value_array[1]
            hand_trump_value = hand_trump_value + trump_value_array[1]
        if card[0] == 'ace' and card[1] == best_suit:
            hand_trump[2] = trump_value_array[2]
            hand_trump_value = hand_trump_value + trump_value_array[2]
        if card[0] == 'queen' and card[1] == best_suit:
            hand_trump[3] = trump_value_array[3]
            hand_trump_value = hand_trump_value + trump_value_array[1]
        if card[0] == '10' and card[1] == best_suit:
            hand_trump[4] = trump_value_array[4]
            hand_trump_value = hand_trump_value + trump_value_array[5]
        if card[0] == '9' and card[1] == best_suit:
            hand_trump[5] = trump_value_array[5]
            hand_trump_value = hand_trump_value + trump_value_array[5]

    # print(f'Hand trump array is {hand_trump} and total value {hand_trump_value}')

    return hand_trump_value, best_suit, hand_trump