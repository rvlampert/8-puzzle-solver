from datetime import datetime
import sys
import yaml
from src.algorithms import bfs, dfs, astar_hamming, astar_manhattan

def main():
    input_data = sys.argv[1]
    with open("config.yaml", "r") as f:
      CONFIG = yaml.load(f, Loader=yaml.FullLoader)
    if len(input_data) != len(CONFIG["solution"]) or "_" not in input_data:
      print("invalid input")
    algorithms = [bfs,dfs,astar_hamming,astar_manhattan]
    for algorithm in algorithms:
      print("\nSearch algorithm:",algorithm.__name__)
      movements = []
      start_time = datetime.now()
      movements = algorithm(input_data,CONFIG)
      end_time = datetime.now()
      print("Time:",end_time-start_time)
      print("Moviments: ",len(movements),"\n\n================================")   

if __name__ == '__main__':
    main()