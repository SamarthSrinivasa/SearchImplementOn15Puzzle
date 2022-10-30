# function general - search(problem, QUEUEING-FUNCTION)
# nodes = MAKE-QUEUE(MAKE-NODE(problem.INITIAL-STATE))
# loop do
# if EMPTY(nodes) then return "failure"
#     node = REMOVE-FRONT(nodes)
# if problem.GOAL-TEST(node.STATE) succeeds then return node
#     nodes = QUEUEING-FUNCTION(nodes, EXPAND(node, problem.OPERATORS))
# end

# function UniformCostSearch - search(specific 8 board(IS), h(n) = 0)
# nodes = MAKE-QUEUE(MAKE-NODE(problem.INITIAL-STATE))
#
# loop do
# if EMPTY(nodes) then return "failure"
#     node = REMOVE-FRONT(nodes)
# if problem.GOAL-TEST(node.STATE) succeeds then return node
#     nodes = QUEUEING-FUNCTION(nodes, EXPAND(node, problem.OPERATORS))
# end

import heapq
import copy
import time
import numpy as np
import pandas as pd

class Node:
    def __init__(self, problem, cost, depth):
        self.problem = problem
        self.cost = cost
        self.depth = depth

def down(node: Node):
    for i, row in enumerate(node.problem):
        for j, col in enumerate(row):
            if col == 0:
                if i == 2:
                    return None
                node.problem[i][j], node.problem[i+1][j] = node.problem[i+1][j], node.problem[i][j]
                return node

    return -1,-1

def up(node: Node):
    for i, row in enumerate(node.problem):
        for j, col in enumerate(row):
            if col == 0:
                if i == 0:
                    return None
                node.problem[i][j], node.problem[i-1][j] = node.problem[i-1][j], node.problem[i][j]
                return node

    return -1,-1

def right(node: Node):
    for i, row in enumerate(node.problem):
        for j, col in enumerate(row):
            if col == 0:
                if i == 2:
                    return None
                node.problem[i][j], node.problem[i][j+1] = node.problem[i][j+1], node.problem[i][j]
                return node

    return -1,-1

def left(node: Node):
    for i, row in enumerate(node.problem):
        for j, col in enumerate(row):
            if col == 0:
                if i == 0:
                    return None
                node.problem[i][j], node.problem[i][j-1] = node.problem[i][j-1], node.problem[i][j]
                return node

    return -1,-1

#def generalSearch ()



def main():
    
    print("Hey Welcome to Samarth's 8-Puzzle solver")
    print("Please input 1 to input your own puzzle, or ")

    game1 = [[1,2,3],
            [4,0,5],
            [6,7,8]]

    root = Node(game1, 0, 0)

    rightnode = right(root)

    print("Hey")
    for row in root.problem:
        print(row)
    
main()


#Mover Functions 

# initial state node

# first find out where 0 is 

# then see all possible ways to move that 0

# store all ways to move that 0 into a data structure 

# go to the first node in that data structure and check if its the goal state

# goal state node 


#print(game1)




