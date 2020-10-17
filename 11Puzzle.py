import heapq, copy

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

# def solver(prioQueue, seenStates, N):
#     if len(prioQueue) == 0:
#         return False
#     else:
#         node = heapq.heappop(prioQueue)
#         fVal = node[0]
#         state = node[1]
#         goal = node[2]
#         blankRow = node[3]
#         blankCol = node[4]
#         actions = node[5]
#         fVals = node[6]

#         if state == goal:
#             return (actions, fVals, N)
#         else:
#             if blankRow != 0:
#                 stateCopy = copy.deepcopy(state)
#                 newState = stateAfterAction(stateCopy, "U", blankRow, blankCol)
#                 strState = str(newState)
#                 if strState not in seenStates:
#                     seenStates[strState] = True
#                     hVal = calcManhattanDist(newState,goal)
#                     newActions = copy.copy(actions)
#                     newActions.append("U")
#                     gVal = len(actions)
#                     fVal = gVal + hVal
#                     newfVals = copy.copy(fVals)
#                     newfVals.append(fVal)
#                     newElement = [fVal, newState, goal, blankRow-1, blankCol, newActions, newfVals]
#                     heapq.heappush(prioQueue, newElement)
#                     N+=1
#             if blankRow != (len(state)-1):
#                 stateCopy = copy.deepcopy(state)
#                 newState = stateAfterAction(stateCopy, "D", blankRow, blankCol)
#                 strState = str(newState)
#                 if strState not in seenStates:
#                     seenStates[strState] = True
#                     hVal = calcManhattanDist(newState,goal)
#                     newActions = copy.copy(actions)
#                     newActions.append("D")
#                     gVal = len(actions)
#                     fVal = gVal + hVal
#                     newfVals = copy.copy(fVals)
#                     newfVals.append(fVal)
#                     newElement = [fVal, newState, goal, blankRow+1, blankCol, newActions, newfVals]
#                     heapq.heappush(prioQueue, newElement)
#                     N+=1
#             if blankCol != 0:
#                 stateCopy = copy.deepcopy(state)
#                 newState = stateAfterAction(stateCopy, "L", blankRow, blankCol)
#                 strState = str(newState)
#                 if strState not in seenStates:
#                     seenStates[strState] = True
#                     hVal = calcManhattanDist(newState,goal)
#                     newActions = copy.copy(actions)
#                     newActions.append("L")
#                     gVal = len(actions)
#                     fVal = gVal + hVal
#                     newfVals = copy.copy(fVals)
#                     newfVals.append(fVal)
#                     newElement = [fVal, newState, goal, blankRow, blankCol-1, newActions, newfVals]
#                     heapq.heappush(prioQueue, newElement)
#                     N+=1
#             if blankCol != (len(state[0])-1):
#                 stateCopy = copy.deepcopy(state)
#                 newState = stateAfterAction(stateCopy, "R", blankRow, blankCol)
#                 strState = str(newState)
#                 if strState not in seenStates:
#                     seenStates[strState] = True
#                     hVal = calcManhattanDist(newState,goal)
#                     newActions = copy.copy(actions)
#                     newActions.append("R")
#                     gVal = len(actions)
#                     fVal = gVal + hVal
#                     newfVals = copy.copy(fVals)
#                     newfVals.append(fVal)
#                     newElement = [fVal, newState, goal, blankRow, blankCol+1, newActions, newfVals]
#                     heapq.heappush(prioQueue, newElement)
#                     N+=1
#             return solver(prioQueue, seenStates, N)

def solver(prioQueue, seenStates, N):
    while len(prioQueue) > 0:
        node = heapq.heappop(prioQueue)
        fVal = node[0]
        state = node[1]
        goal = node[2]
        blankRow = node[3]
        blankCol = node[4]
        actions = node[5]
        fVals = node[6]

        if state == goal:
            return (actions, fVals, N)
        else:
            if blankRow != 0:
                stateCopy = copy.deepcopy(state)
                newState = stateAfterAction(stateCopy, "U", blankRow, blankCol)
                strState = str(newState)
                if strState not in seenStates:
                    seenStates[strState] = True
                    hVal = calcManhattanDist(newState,goal)
                    newActions = copy.copy(actions)
                    newActions.append("U")
                    gVal = len(actions)
                    fVal = gVal + hVal
                    newfVals = copy.copy(fVals)
                    newfVals.append(fVal)
                    newElement = [fVal, newState, goal, blankRow-1, blankCol, newActions, newfVals]
                    heapq.heappush(prioQueue, newElement)
                    N+=1
            if blankRow != (len(state)-1):
                stateCopy = copy.deepcopy(state)
                newState = stateAfterAction(stateCopy, "D", blankRow, blankCol)
                strState = str(newState)
                if strState not in seenStates:
                    seenStates[strState] = True
                    hVal = calcManhattanDist(newState,goal)
                    newActions = copy.copy(actions)
                    newActions.append("D")
                    gVal = len(actions)
                    fVal = gVal + hVal
                    newfVals = copy.copy(fVals)
                    newfVals.append(fVal)
                    newElement = [fVal, newState, goal, blankRow+1, blankCol, newActions, newfVals]
                    heapq.heappush(prioQueue, newElement)
                    N+=1
            if blankCol != 0:
                stateCopy = copy.deepcopy(state)
                newState = stateAfterAction(stateCopy, "L", blankRow, blankCol)
                strState = str(newState)
                if strState not in seenStates:
                    seenStates[strState] = True
                    hVal = calcManhattanDist(newState,goal)
                    newActions = copy.copy(actions)
                    newActions.append("L")
                    gVal = len(actions)
                    fVal = gVal + hVal
                    newfVals = copy.copy(fVals)
                    newfVals.append(fVal)
                    newElement = [fVal, newState, goal, blankRow, blankCol-1, newActions, newfVals]
                    heapq.heappush(prioQueue, newElement)
                    N+=1
            if blankCol != (len(state[0])-1):
                stateCopy = copy.deepcopy(state)
                newState = stateAfterAction(stateCopy, "R", blankRow, blankCol)
                strState = str(newState)
                if strState not in seenStates:
                    seenStates[strState] = True
                    hVal = calcManhattanDist(newState,goal)
                    newActions = copy.copy(actions)
                    newActions.append("R")
                    gVal = len(actions)
                    fVal = gVal + hVal
                    newfVals = copy.copy(fVals)
                    newfVals.append(fVal)
                    newElement = [fVal, newState, goal, blankRow, blankCol+1, newActions, newfVals]
                    heapq.heappush(prioQueue, newElement)
                    N+=1

def main():
    inputFileName = input("Please enter the input filename: ")
    outputFileName = input("Please enter the output filename: ")
    initial = []
    goal = []
    seenStates = {}
    H = []
    heapq.heapify(H)
    N = 1
    actions = []
    readInput(inputFileName, initial, goal)
    state = copy.deepcopy(initial)
    initialVal = calcManhattanDist(state,goal)
    fVals = [initialVal]
    seenStates[str(state)] = True
    #find blankRow and blankCol
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == "0":
                blankRow = i
                blankCol = j
    firstElement = [initialVal, state, goal, blankRow, blankCol, actions, fVals]
    heapq.heappush(H, firstElement)


    res = solver(H, seenStates, N)
    if res == False:
        print("Goal could not be reached")
    else:
        actions = res[0]
        fVals = res[1]
        newN = res[2]
        d = len(actions)
        writeOutput(outputFileName, initial, goal, d, newN, actions, fVals)

main()