from src.distances import hamming, manhattan

MOVEMENTS = {
    0: [("direita", 1), ("abaixo", 3)],
    1: [("direita", 2), ("abaixo", 4), ("esquerda", 0)],
    2: [("abaixo", 5), ("esquerda", 1)],
    3: [("acima", 0), ("direita", 4), ("abaixo", 6)],
    4: [("acima", 1), ("direita", 5), ("abaixo", 7), ("esquerda", 3)],
    5: [("acima", 2), ("abaixo", 8), ("esquerda", 4)],
    6: [("acima", 3), ("direita", 7)],
    7: [("acima", 4), ("direita", 8), ("esquerda", 6)],
    8: [("acima", 5), ("esquerda", 7)],
}

class Node:
    def __init__(self, state, father=None, move=None, cost=1, total_cost=0):
        self.state = state
        self.father = father
        self.move = move
        self.cost = cost
        self.total_cost = total_cost

def successor(state):
    successors = set()
    empty_place = state.find("_")
    for movement in MOVEMENTS[empty_place]:
        successors.add((movement[0],swap_positions(state,empty_place,movement[1])))
    return successors

def expand(node):
    children_nodes=set()
    possible_successors = successor(node.state)
    for possible_successor in possible_successors:
        children_nodes.add(Node(possible_successor[1],
                            node,possible_successor[0],
                            node.cost+1,
                            node.total_cost))
    return children_nodes

def swap_positions(state,a,b):
    new_value = state[b]
    state = state.replace(state[b],"x")
    state = state.replace(state[a],new_value)
    state = state.replace("x","_")
    return state

def insert_element(set,element,type, config):
    if type=="a*_h":
        element.total_cost = element.cost+hamming(element.state, config)
    elif type=="a*_m":
        element.total_cost = element.cost+manhattan(element.state, config)
    set.insert(0,element)
    return set

def remove_element(set,type):
    if type == 'bfs':
        element = set.pop()
    elif type == 'dfs':
        element = set.pop(0)
    else:
        index = catch_priority(set)
        element = set.pop(index)
    return set, element

def catch_priority(queue):
    index = 0
    smallest = queue[0].total_cost
    for i,node in enumerate(queue):
        if node.total_cost < smallest:
            smallest = node.total_cost
            index = i
    return index


def calculate_solution(node,config):
    solution = []
    while node.father != None:
        solution = insert_element(solution,node,"",config)
        node = node.father
    return solution

def count_inversions(state):
    inversions = 0
    numbers = state.replace("_","")
    for current, number in enumerate(numbers):
        for index in range(current+1,len(numbers)):
            if number>numbers[index]:
                inversions+=1
    return inversions

def search(state,type, config):
    if (count_inversions(state) % 2) == 1:
        return None
    boundary = [Node(state)]
    expanded = set()
    while True:
        if not boundary:
            return None
        boundary,current = remove_element(boundary,type)
        if current.state == config["solution"]:
            return calculate_solution(current,config)
        if current.state not in expanded:
            next_nodes = expand(current)
            expanded.add(current.state)
            for next_node in next_nodes:
                if next_node.state not in expanded:
                    boundary = insert_element(boundary,next_node,type,config)