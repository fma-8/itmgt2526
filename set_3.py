'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "set_3_sample_data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if from_member follows to_member,
        "followed by" if from_member is followed by to_member,
        "friends" if from_member and to_member follow each other,
        "no relationship" if neither from_member nor to_member follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    if to_member in social_graph[from_member]['following'] and from_member in social_graph[to_member]['following']:
        return 'friends'
    elif to_member in social_graph[from_member]['following']:
        return 'follower'
    elif from_member in social_graph[to_member]['following']:
        return 'followed by'
    else:
        return 'no relationship'


def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "set_3_sample_data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    for i in range(len(board)): #horizontal    
        if ''.join(board[i]) == 'X'*len(board):
            return 'X'
        elif ''.join(board[i]) =='O'*len(board):
            return 'O'
        else:
            continue
    
    for i in range(len(board)):   #vertical
        vert = ''
        for y in range(len(board[i])):
            vert += board[y][i]
        
        if vert == 'X'*len(board):
            return 'X'
        elif vert =='O'*len(board):
            return 'O'
        else:
            continue
    
    diag1 = ''
    for i in range(len(board)):
        diag1 += board[i][i]

    if diag1 == 'X'*len(board):
        return 'X'
    elif diag1 =='O'*len(board):
        return 'O'
    else:
        pass

    diag2 = ''
    for i in range(len(board)):
        diag2 += board[i][-1-i]

    if diag2 == 'X'*len(board):
        return 'X'
    elif diag2 =='O'*len(board):
        return 'O'
    else:
        return 'NO WINNER'

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "set_3_sample_data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    total = 0
    keys = list(route_map.keys())
    for i in range(len(keys)):
        if first_stop == keys[i][0]:
            total += route_map[keys[i]]['travel_time_mins']
            if second_stop == keys[i][1]:
                break
            else:
                j = (i + 1) % len(keys)
                while second_stop != keys[j][1]:
                    total += route_map[keys[j]]['travel_time_mins']
                    j = (j + 1) % len(keys)
                total += route_map[keys[j]]['travel_time_mins']
                break
        else:
            continue
    
    return total