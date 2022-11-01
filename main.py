import heapq
import copy
import time
import numpy as np
import pandas as pd

seen = []

class eightprob:
    initialState = [[1,6,7],[5,0,3],[4,8,2]]
    def goaltest(self, state):
        if state == [[1,2,3],[4,5,6],[7,8,0]]:
            return True
        else:
            return False

class Node:
    def __init__(self, problem, cost, depth, hVal):
        self.problem = problem
        self.cost = cost
        self.depth = depth
        self.hVal = hVal
    def __lt__(self, Hval):
        return self.hVal < Hval.hVal

def left(node: Node):
    for i in range (len(node.problem)):
        for j in range (len(node.problem[i])):
            if node.problem[i][j] == 0:
                if (i - 1) >= 0:
                    node.problem[i][j], node.problem[i-1][j] = node.problem[i-1][j], node.problem[i][j]
                    return node
    return None

def right(node: Node):
    for i in range (len(node.problem)):
        for j in range (len(node.problem[i])):
            if node.problem[i][j] == 0:
                if (i + 1) < len(node.problem[i]):
                    node.problem[i][j], node.problem[i+1][j] = node.problem[i+1][j], node.problem[i][j]
                    return node
    return None

def up(node: Node):
    for i in range (len(node.problem)):
        for j in range (len(node.problem[i])):
            if node.problem[i][j] == 0:
                if (j - 1) >= 0:
                    node.problem[i][j], node.problem[i][j-1] = node.problem[i][j-1], node.problem[i][j]
                    return node
    return None

def down(node: Node):
    for i in range (len(node.problem)):
        for j in range (len(node.problem[i])):
            if node.problem[i][j] == 0:
                if (j + 1) < len(node.problem[j]):
                    node.problem[i][j], node.problem[i][j+1] = node.problem[i][j+1], node.problem[i][j]
                    return node
    return None

def AstarWMisplaced(node: Node):

    goalState = [[1,2,3],[4,5,6],[7,8,0]]

    #initialState = [[1,2,3],[4,5,6],[0,7,8]]

    misplacedHeuristic = 0
    for x in range (len(node.problem)):
        for y in range (len(node.problem[x])):
            if node.problem[x][y] != goalState[x][y] and node.problem[x][y] != 0:
                misplacedHeuristic += 1
                # print("changedVal")
    return misplacedHeuristic

def AstarWManhattan(node: Node):
    return None


# function general-search(problem,Queueing-Function)
def generalSearch (problem, QFunc):
    
    #nodes = MAKE-QUEUE(MAKE-NODE(problem, initial state))
    initialNode = Node(problem.initialState, 0, 0, 0)
    
    states = [] #creating the makeQueue called states 
    heapq.heappush(states, initialNode) #putting the first node inside the queue 
    nodeCount = 0 
    #loop do 
    while states:
        
        
        currentState = states.pop(0)  #nodes = remove-front(nodes) 
        # nodeCount = nodeCount + 1
        
        #for row in currentState.problem: 
            #print(row)
        #print(currentState.problem)
        nodeCount += 1

        if nodeCount > 50000:
            print("took too long")
            return None
        #if problem.currentstate = problem.goalstate then return node
        if problem.goaltest(currentState.problem):
            print("Solution Found!")
            print('How many nodes expanded = ', nodeCount)
            print('depth: ', currentState.depth)
            print('Max Queue size: ', len(states))
            return currentState
        #nodes = Queueing function(nodes, expand(nodes, problem.Operators))
        states = QueueFunc(currentState, states, QFunc)
        #print("\n")
    else:
        print("fail")
        return None #if empty(nodes) then return failure 


def QueueFunc(node: Node, nodes, hx):
    
    # print(type(hx))
    global seen

    #Expand Function for each Operator 
    branchNodeUp = copy.deepcopy(node)
    branchNodeUp = up(copy.deepcopy(branchNodeUp))
    if branchNodeUp is not None:
        branchNodeUp.depth += 1
        if (hx == 1):
            #print('UDS')
            branchNodeUp.cost += 1
            branchNodeUp.hVal += 1
        if (hx == 2):
            #print("A*")
            #print(branchNode.depth)
            branchNodeUp.cost = AstarWMisplaced(branchNodeUp) + branchNodeUp.depth
            #print(branchNodeUp.cost)
            #print(branchNodeUp.cost)

        if (branchNodeUp.problem) not in seen: 
            heapq.heappush(nodes, branchNodeUp)
            seen.append(branchNodeUp.problem)

    branchNodeDown = copy.deepcopy(node)
    branchNodeDown = down(copy.deepcopy(branchNodeDown))
    if branchNodeDown is not None:
        branchNodeDown.depth += 1
        if (hx == 1):
            branchNodeDown.cost += 1
            branchNodeDown.hVal += 1
        if (hx == 2):
            branchNodeDown.cost = AstarWMisplaced(branchNodeDown) + branchNodeDown.depth
            #print(branchNodeDown.cost)
            # print(branchNodeDown.cost)
        #heapq.heappush(nodes, branchNodeDown)

        if (branchNodeDown.problem) not in seen: 
            heapq.heappush(nodes, branchNodeDown)
            seen.append(branchNodeDown.problem)
    
         

    branchNodeLeft = copy.deepcopy(node)
    branchNodeLeft = left(copy.deepcopy(branchNodeLeft))
    if branchNodeLeft is not None:
        branchNodeLeft.depth += 1
        if (hx == 1):
            branchNodeLeft.cost += 1
            branchNodeLeft.hVal += 1
            #print(branchNodeLeft.cost)
        if (hx == 2):
           branchNodeLeft.cost = AstarWMisplaced(branchNodeLeft) + branchNodeLeft.depth
           #print(branchNodeLeft.cost)
            #print(branchNodeLeft.cost)
            #print(branchNodeLeft.cost)
        #heapq.heappush(nodes, branchNodeLeft)

        if (branchNodeLeft.problem) not in seen: 
            heapq.heappush(nodes, branchNodeLeft)
            seen.append(branchNodeLeft.problem)
         
        
    branchNodeRight = copy.deepcopy(node)
    branchNodeRight = right(copy.deepcopy(branchNodeRight))
    if branchNodeRight is not None:
        branchNodeRight.depth += 1
        if (hx == 1):
            branchNodeRight.cost += 1
            branchNodeRight.hVal += 1
            #print(branchNodeRight.cost)
        if (hx == 2):
            branchNodeRight.cost = AstarWMisplaced(branchNodeRight) + branchNodeRight.depth
            #print(branchNodeRight.cost)
            #print(branchNodeRight.cost)
            #print(branchNodeRight.cost)
        #heapq.heappush(nodes, branchNodeRight)

        if (branchNodeRight.problem) not in seen: 
            #print("New node adding to shaun")
            heapq.heappush(nodes, branchNodeRight)
            seen.append(branchNodeRight.problem)
    
    nodes = sorted(nodes, key=lambda n: (n.cost, n.depth))
    #nodes = sorted(nodes, key=lambda n: (n.cost))
    return nodes

def main():
    
    puts = []
    print("Samarth's 8-Puzzle solver")
    choice = input("Please input 1 to input your own puzzle, or inputs 2-9 to test out in-built puzzles from depths 0-24 ")

    prob = eightprob()

    #node2 = Node([[1,2,4],[3,0,6],[7,8,5]], 0, 0, 0)
    #goalState = [[1,2,3],[4,5,6],[7,8,0]]
    #initialState = [[1,2,3],[4,5,6],[0,7,8]]
    #print(AstarWMisplaced(node2))

    if choice == "2":
        generalSearch(prob, 2)



main()


#Mover Functions 

# initial state node

# first find out where 0 is 

# then see all possible ways to move that 0

# store all ways to move that 0 into a data structure 

# go to the first node in that data structure and check if its the goal state

# goal state node 


#print(game1)




