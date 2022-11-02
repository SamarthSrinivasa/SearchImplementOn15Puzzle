import heapq
import copy
import time
import numpy as np
import pandas as pd

seen = []

class eightprob():
    #madeInitialState = puts
    #initialState = [[7,1,2],[4,8,5],[6,3,0]]
    initialState = 0
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
    graphxy = [[0,0],[0,1],[0,2]]

    #initialState = [[1,2,3],[4,5,6],[0,7,8]]

    misplacedHeuristic = 0
    for x in range (len(node.problem)):
        for y in range (len(node.problem[x])):
            if node.problem[x][y] != goalState[x][y] and node.problem[x][y] != 0:
                misplacedHeuristic += 1

                # print("changedVal")
    return misplacedHeuristic

def AstarWManhattan(node: Node):


    goalState = [[1,2,3],[4,5,6],[7,8,0]]

    manhat = 0
    #print(manhat)
    for x in range (len(node.problem)):
        for y in range (len(node.problem[x])):
            if goalState[x][y] == 0:
                cor1 = x
                cor2 = y
    #print(cor1)
    #print(cor2)
    for x in range (len(node.problem)):
        for y in range (len(node.problem[x])):
            if node.problem[x][y] != goalState[x][y] and node.problem[x][y] != 0:
                manhat += (abs(cor1 - x) + abs(cor2 - y) + 1)
                #print((abs(cor1 - x) + abs(cor2 - y))
                

    #print(manhat)
    return manhat

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
            #branchNodeUp.depth += 1
        if (hx == 2):
            #print("A*")
            #print(branchNode.depth)
            branchNodeUp.cost = AstarWMisplaced(branchNodeUp) + branchNodeUp.cost
            #print(branchNodeUp.cost)
            #print(branchNodeUp.cost)
        if (hx == 3):
            branchNodeUp.cost = AstarWManhattan(branchNodeUp) + branchNodeUp.cost

        if (branchNodeUp.problem) not in seen: 
            heapq.heappush(nodes, branchNodeUp)
            seen.append(branchNodeUp.problem)

    branchNodeDown = copy.deepcopy(node)
    branchNodeDown = down(copy.deepcopy(branchNodeDown))
    if branchNodeDown is not None:
        branchNodeDown.depth += 1
        if (hx == 1):
            #branchNodeDown.depth += 1
            branchNodeDown.cost += 1
            branchNodeDown.hVal += 1
        if (hx == 2):
            branchNodeDown.cost = AstarWMisplaced(branchNodeDown) + branchNodeDown.cost
            #print(branchNodeDown.cost)
            # print(branchNodeDown.cost)
        #heapq.heappush(nodes, branchNodeDown)
        if (hx == 3):
            branchNodeDown.cost = AstarWManhattan(branchNodeDown) + branchNodeDown.cost
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
           branchNodeLeft.cost = AstarWMisplaced(branchNodeLeft) + branchNodeLeft.cost
           #print(branchNodeLeft.cost)
            #print(branchNodeLeft.cost)
            #print(branchNodeLeft.cost)
        #heapq.heappush(nodes, branchNodeLeft)
        if (hx == 3):
            branchNodeLeft.cost = AstarWManhattan(branchNodeLeft) + branchNodeLeft.cost
        if (branchNodeLeft.problem) not in seen: 
            heapq.heappush(nodes, branchNodeLeft)
            seen.append(branchNodeLeft.problem)
         
        
    branchNodeRight = copy.deepcopy(node)
    branchNodeRight = right(copy.deepcopy(branchNodeRight))
    if branchNodeRight is not None:
        branchNodeRight.depth += 1
        if (hx == 1):
            #branchNodeRight.depth += 1
            branchNodeRight.cost += 1
            branchNodeRight.hVal += 1
            #print(branchNodeRight.cost)
        if (hx == 2):
            branchNodeRight.cost = AstarWMisplaced(branchNodeRight) + branchNodeRight.cost
            #print(branchNodeRight.cost)
            #print(branchNodeRight.cost)
            #print(branchNodeRight.cost)
        #heapq.heappush(nodes, branchNodeRight)
        if (hx == 3):
            branchNodeRight.cost = AstarWManhattan(branchNodeRight) + branchNodeRight.cost
        if (branchNodeRight.problem) not in seen: 
            #print("New node adding to shaun")
            heapq.heappush(nodes, branchNodeRight)
            seen.append(branchNodeRight.problem)
    
    nodes = sorted(nodes, key=lambda n: (n.cost, n.depth))
    #nodes = sorted(nodes, key=lambda n: (n.cost))
    return nodes

def main():

    prob = eightprob()
    puts = []
    print("Samarth's 8-Puzzle solver")
    choice = input("Press 1 if you want to input a puzzle, Press 2 for set depth puzzles" + '\n')
    if choice == "1":
        print("Enter your puzzle, using a zero to represent the blank. " + "Please only enter valid 8 puzzles. Enter the puzzle demilimiting " +"the numbers with a space. Press enter only when finished." + '\n')
        puzzle_row_one = input("Enter the first row: ")
        puzzle_row_two = input("Enter the second row: ")
        puzzle_row_three = input("Enter the third row: ")
    
        puzzle_row_one = puzzle_row_one.split()
        puzzle_row_two = puzzle_row_two.split()
        puzzle_row_three = puzzle_row_three.split()
        for i in range(0, 3):
            puzzle_row_one[i] = int(puzzle_row_one[i])
            puzzle_row_two[i] = int(puzzle_row_two[i])
            puzzle_row_three[i] = int(puzzle_row_three[i])
        puts = [puzzle_row_one, puzzle_row_two, puzzle_row_three]

        prob.initialState = puts

        choice2 = input("If you want to run Uniform Cost, press 1, if you want to run Misplaced Tile Heuristic, press 2, and if you want to run the Manhattan Heuristic, press 3" + '\n')

        if choice2 == "1":
            generalSearch(prob, 1)
        if choice2 == "2":
            generalSearch(prob, 2)
        if choice2 == "3":
            generalSearch(prob, 3)
    if choice == "2":
        depthNum = input("Enter a depth: 0,2,4,8,13,16,20 or 24" + '\n')
        if depthNum == 0:
            prob.initialState = [[1,2,3],[4,5,6],[7,8,0]]
        if depthNum == 2:
            prob.initialState = [[1,2,3],[4,5,6],[0,7,8]]
        if depthNum == 4:
            prob.initialState = [[1,2,3],[5,0,6],[4,7,8]]
        if depthNum == 8:
            prob.initialState = [[1,3,6],[5,0,2],[4,7,8]]
        if depthNum == 12:
            prob.initialState = [[1,3,6],[5,0,7],[4,8,2]]
        if depthNum == 16:
            prob.initialState = [[1,6,7],[5,0,3],[4,8,2]]
        if depthNum == 20:
            prob.initialState = [[7,1,2],[4,8,5],[6,3,0]]
        if depthNum == 24:
            prob.initialState = [[0,7,2],[4,6,1],[3,5,8]]
        if depthNum == 31:
            prob.initialState = [[8,6,7],[2,5,4],[3,0,1]]

        choice2 = input("If you want to run Uniform Cost, press 1, if you want to run Misplaced Tile Heuristic, press 2, and if you want to run the Manhattan Heuristic, press 3" + '\n')

        if choice2 == "1":
            generalSearch(prob, 1)
        if choice2 == "2":
            generalSearch(prob, 2)
        if choice2 == "3":
            generalSearch(prob, 3)

main()


#Mover Functions 

# initial state node

# first find out where 0 is 

# then see all possible ways to move that 0

# store all ways to move that 0 into a data structure 

# go to the first node in that data structure and check if its the goal state

# goal state node 


#print(game1)




