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

    # Find value of cards of the trump [right, left, ace, queen, 10, 9]
    trump_value_array = [10, 8, 5, 2, 1, 1]

    hand_trump = [0,0,0,0,0,0] 
    hand_trump_value = 0

    suit_value = []

    for suit in suits:
        for card in hand:
            # print(card)
            if card[0] == 'jack' and card[1] == suit:
                hand_trump[0] = trump_value_array[0]
                hand_trump_value = hand_trump_value + trump_value_array[0]
            if card[0] == 'jack' and card[1] == sister_suit(suit):
                hand_trump[1] = trump_value_array[1]
                hand_trump_value = hand_trump_value + trump_value_array[1]
            if card[0] == 'ace' and card[1] == suit:
                hand_trump[2] = trump_value_array[2]
                hand_trump_value = hand_trump_value + trump_value_array[2]
            if card[0] == 'queen' and card[1] == suit:
                hand_trump[3] = trump_value_array[3]
                hand_trump_value = hand_trump_value + trump_value_array[1]
            if card[0] == '10' and card[1] == suit:
                hand_trump[4] = trump_value_array[4]
                hand_trump_value = hand_trump_value + trump_value_array[5]
            if card[0] == '9' and card[1] == suit:
                hand_trump[5] = trump_value_array[5]
                hand_trump_value = hand_trump_value + trump_value_array[5]

        suit_value.append(hand_trump_value)
            

    # print(f'Hand trump array is {hand_trump} and total value {hand_trump_value}')

    return hand_trump_value, best_suit, hand_trump