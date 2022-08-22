# 8-puzzle-solver

A 8 puzzle solver, that use AI to find the optimized moves to solve the puzzle

## Objective

Build a artificial inteligence capable of solve the n-puzzle game with less movements possible

## Solutions

For this project, we use 4 different solutions, using  the WIDTH search (BFS), DEPTH search (DFS) A\* using hamming distance and A\* using Manhattan distance

## How to run

Create a virtual environment, use ```make install-dependencies``` command to install the python dependencies, then use ```make run <board>``` to run the program

## Board

The board is represented by a string with the rows of the board appended on the end of each line and the empty space is represented by a `_` char, for example:
```
1  2  3
4     6
7  5  8  
```
would be represented by `1234_6758`