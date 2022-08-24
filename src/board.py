import os
import time

DELAY = 1.5
def print_state(state):
    x = state.replace("_"," ")
    print("╔═══╦═══╦═══╗")
    print(f"║ {x[0]} ║ {x[1]} ║ {x[2]} ║")
    print("╠═══╬═══╬═══╣")
    print(f"║ {x[3]} ║ {x[4]} ║ {x[5]} ║")
    print("╠═══╬═══╬═══╣")
    print(f"║ {x[6]} ║ {x[7]} ║ {x[8]} ║")
    print("╚═══╩═══╩═══╝")

def print_solution(solution):
    for node in solution:
        time.sleep(DELAY)
        os.system('clear')
        print_state(node.state)