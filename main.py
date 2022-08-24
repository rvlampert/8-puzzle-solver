from datetime import datetime
import sys
import yaml
import os
from src.board import print_solution
from src.algorithms import bfs, dfs, astar_hamming, astar_manhattan

def main():
  os.system('clear')
  print("="*60)
  input_data = sys.argv[1]
  with open("config.yaml", "r") as f:
    CONFIG = yaml.load(f, Loader=yaml.FullLoader)
  if len(input_data) != len(CONFIG["solution"]) or "_" not in input_data:
    print("invalid input")
  algorithms = [bfs,dfs,astar_hamming,astar_manhattan]
  best_solution = None
  best_moviments = float('inf')
  for algorithm in algorithms:
    print("Searching solution using ",algorithm.__name__, "algorithm...")
    print("\tSearch algorithm:",algorithm.__name__)
    movements = []
    start_time = datetime.now()
    movements, solution = algorithm(input_data,CONFIG)
    if(len(movements) < best_moviments):
      best_moviments=len(movements)
      best_solution = solution
    end_time = datetime.now()
    print("\tTime:",end_time-start_time)
    print("\tMoviments: ",len(movements),"\n","="*60)
  input("press enter to play the solution")
  print_solution(best_solution)

if __name__ == '__main__':
  main()