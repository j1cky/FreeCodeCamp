from collections import Counter


# ------------- Pattern case -------------------------

def find_shortest_repeating_pattern(opp_list):
    n = len(opp_list)

    # Start with increasing pattern lengths
    for pattern_length in range(1, n // 2 + 1):
        # Candidate pattern is the first `pattern_length` elements
        pattern = opp_list[:pattern_length]

        # Check if the entire list is composed of this pattern
        is_repeating = True
        for i in range(0, n, pattern_length):
            if opp_list[i:i + pattern_length] != pattern[:n - i]:
                is_repeating = False
                break

        # If the pattern is repeating, return it
        if is_repeating:
            return pattern, True

    # If no repeating pattern is found, return the whole list as pattern
    return opp_list, False

def predict_next_move_in_pattern_case(shortest_pattern, opp_list): # used only in case pattern found 


    # isolate the last unfinished pattern
    unfinished_pattern = shortest_pattern[:len(opp_list) % len(shortest_pattern)]


    continuation = shortest_pattern[len(unfinished_pattern):len(unfinished_pattern)+1]

    next_move = continuation[0]
    # print("Next move is :", next_move)
    return next_move

def player(prev_play, opponent_history=[], my_history=[], plays = [0], second_strategy=[False]):
    # prev_play is the adversaire's play at the previous game
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    plays[0] += 1
    guess = 'R'

    if prev_play =='':
        second_strategy[0] = False
        opponent_history.clear()  
        plays[0] = 0
        my_history.clear() 
        my_history.append(guess)
        return guess

    opponent_history.append(prev_play)

    # Counter my last guess twice (if R choose S)
    guess =  ideal_response[ideal_response[my_history[-1]]]

    # at game 20 check if i am losing then switch strategy
    if plays[0]==20 :
        i_lose = 0
        for i in range(19):
            if opponent_history[i] == ideal_response[my_history[i]]:
                i_lose += 1

        second_strategy[0] = True if i_lose > 10 else False





    if second_strategy[0]:
        cheated_history = ["R"] + my_history
        my_biplays_history = [ cheated_history[i]+cheated_history[i+1] for i in range(len(cheated_history)-1) ]

        counter = Counter(my_biplays_history)

        # Limit to 9 keys (if there are more than 9 unique strings)
        my_ex_plays_dict = dict(counter.most_common(9))

        letter_n_moins_un = my_history[-1]


        potential_plays = [
            letter_n_moins_un + "R",
            letter_n_moins_un + "P",
            letter_n_moins_un + "S",
        ]

        sub_order = {
            k: my_ex_plays_dict[k]
            for k in potential_plays if k in my_ex_plays_dict
        }

        prediction = max(sub_order, key=sub_order.get)[-1:]

        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
        abbey_responce =  ideal_response[prediction]

        guess = ideal_response[abbey_responce]










    # Find the shortest repeating pattern
    shortest_pattern, existing_pattern = find_shortest_repeating_pattern(opponent_history)

    # if the shortest pattern is not the whole list then predict next move
    if existing_pattern:
        repeating_player_next_move = predict_next_move_in_pattern_case(shortest_pattern, opponent_history)    
        guess =  ideal_response[repeating_player_next_move]

    my_history.append(guess)

    return guess
