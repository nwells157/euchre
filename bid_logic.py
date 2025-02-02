def bid_turn(current_bid, ev, expected_suit, bid_owner, player_turn, trump_suit):
    # Take current bid and evaluate if expected value is higher
    # than threshold set (possilby per play for aggressive or passive play)

    bid_array = [2,3,4,5,6] # 5 - Shooter, 6 - Loaner || One less than bid value
    bid_thresholds = [10,30,40,60,70]

    # need threshold[0] > bid_array[0] to bid 3
    for i in range(4,0,-1):
        if ev > bid_thresholds[i]:
            # Raise bid
            current_bid += 1
            bid_owner = player_turn
            trump_suit = expected_suit
            break
        
    return current_bid, bid_owner, trump_suit

