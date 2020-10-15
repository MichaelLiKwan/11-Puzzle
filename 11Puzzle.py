# n n n n
# n n n n
# n n n n
#
# m m m m
# m m m m
# m m m m
# Figure 1. Input file with 9 lines.
# ***************************
# n n n n
# n n n n
# n n n n
#
# m m m m
# m m m m
# m m m m
#
# d (shallowest goal node when root node has a depth of 0)
# N (total number of nodes generated)
# A A A A A A A ………… (List of actions to be completed where A is an action in the set of {L,R,U,D} - left, right, up, down)(d elements)
# f f f f f f f f …………….. (fvalues of the nodes on the way to the solution from root to goal)(d+1 elements)
# Figure 2. Output file with 12 lines.
def readInput(filename, initial, goal):
    inputFile = open(filename, "r")

    #read first three lines as initial state
    for i in range(3):
        initial.append(inputFile.readline().strip().split(" "))

    #skip the fourth line, which is blank
    inputFile.readline()

    #read last three lines as goal state
    for i in range(3):
        goal.append(inputFile.readline().strip().split(" "))

    inputFile.close()

def writeOutput(filename, initial, goal, d, N, actions, fVals):
    outputFile = open(filename, "w")

    #write initial state
    for i in range(3):
        outputFile.write(" ".join(initial[i]))
        outputFile.write("\n")
    outputFile.write("\n")

    #write goal state
    for i in range(3):
        outputFile.write(" ".join(goal[i]))
        outputFile.write("\n")
    outputFile.write("\n")

    #write d and N
    outputFile.write(str(d))
    outputFile.write("\n")
    outputFile.write(str(N))
    outputFile.write("\n")

    #write actions
    for action in actions:
        outputFile.write(str(action))
        outputFile.write(" ")
    outputFile.write("\n")

    #write fVals
    for fVal in fVals:
        outputFile.write(str(fVal))
        outputFile.write(" ")
    outputFile.write("\n")

    outputFile.close()

def calcManhattanDist(currState, goalState):
    dist = 0
    for cRow in range(len(currState)):
        for cCol in range(len(currState[0])):
            for gRow in range(len(goalState)):
                for gCol in range(len(goalState[0])):
                    if currState[cRow][cCol] == goalState[gRow][gCol]:
                        dist = dist + abs(gRow-cRow)+abs(gCol-cCol)
    return dist

def stateAfterAction(state, action, blankRow, blankCol):
    if action == "U":
        state[blankRow][blankCol],state[blankRow-1][blankCol] = state[blankRow-1][blankCol],state[blankRow][blankCol]
    elif action == "D":
        state[blankRow][blankCol],state[blankRow+1][blankCol] = state[blankRow+1][blankCol],state[blankRow][blankCol]
    elif action == "L":
        state[blankRow][blankCol],state[blankRow][blankCol-1] = state[blankRow][blankCol-1],state[blankRow][blankCol]
    elif action == "R":
        state[blankRow][blankCol],state[blankRow][blankCol+1] = state[blankRow][blankCol+1],state[blankRow][blankCol]
    else:
        print("Invalid Action")
    return state

def solver(initial, goal, N, prioQueue, moves):
    if initial == goal:
        return (d, N, actions, fVals)
    else:
        for move in moves:
            if the blank space is not in the top row:
                append the new state after moving the blank space up to the priority queue

def main():
    initial = []
    state = []
    goal = []
    moves = {"U", "D", "L", "R"}
    d = 0
    N = 0
    actions = [1,2,3,4]
    fVals = [1,2,3,4,5]
    readInput("input.txt", initial, goal)
    writeOutput("output.txt", initial, goal, d, N, actions, fVals)

main()
