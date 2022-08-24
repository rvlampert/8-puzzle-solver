from src.search import search

def bfs(state, config):
    """
    Receives a state (string), performs the WIDTH search and
    returns a list of actions that takes from
    received state up to the goal ("12345678_").
    If there is no solution from the received state, return None
    :param state: str
    :return:
    """
    moves=[]
    solution = search(state,'bfs', config)
    if solution is not None:
        for node in solution:
            moves.append(node.move)
        return (moves, solution)
    return None

def dfs(state, config):
    """
    Receives a state (string), performs the DEPTH search and
    returns a list of actions that takes from
    received state up to the goal ("12345678_").
    If there is no solution from the received state, return None
    :param state: str
    :return:
    """
    moves=[]
    solution = search(state,'dfs', config)
    if solution is not None:
        for node in solution:
            moves.append(node.move)
        return (moves, solution)
    return None

def astar_hamming(state, config):
    """
    Receive a state (string), perform A* search with h(n) = sum of Hamming distances and
    returns a list of actions that takes from
    received state up to the goal ("12345678_").
    If there is no solution from the received state, return None
    :param state: str
    :return:
    """
    moves=[]
    solution = search(state,'a*_h', config)
    if solution is not None:
        for node in solution:
            moves.append(node.move)
        return (moves, solution)
    return None

def astar_manhattan(state, config):
    """
    Receive a state (string), perform A* search with h(n) = sum of Manhattan distances and
    returns a list of actions that takes from
    received state up to the goal ("12345678_").
    If there is no solution from the received state, return None
    :param state: str
    :return:
    """
    moves=[]
    solution = search(state,'a*_m',config)
    if solution is not None:
        for node in solution:
            moves.append(node.move)
        return (moves, solution)
    return None