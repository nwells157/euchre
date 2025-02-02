def find_player_turn(turn_counter):
    # Turn counter is the input
    # Player turn is the output and will always lag turn counter
    for i in range(1,5,1):
        if turn_counter == i:
            player_turn = f'player {i}'

    if turn_counter < 4:
        turn_counter += 1
    else:
        turn_counter = 1

    return player_turn, turn_counter


def change_turn_to_winner(winner):
    # Change turn counter to winner
    turn_counter = 0

    if winner == 'player 1':
        turn_counter = 1
    elif winner == 'player 2':
        turn_counter = 2
    elif winner == 'player 3':
        turn_counter = 3
    elif winner == 'player 4':
        turn_counter = 4
    return turn_counter