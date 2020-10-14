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

#READ INPUT FILE ===================================================
inputFile = open("input.txt", "r")
initial = []
state = []
goal = []
d = None
N = None
actions = []
fVals = []

#read first three lines as initial state
for i in range(3):
    initial.append(inputFile.readline().strip().split(" "))

#skip the fourth line, which is blank
inputFile.readline()

#read last three lines as goal state
for i in range(3):
    goal.append(inputFile.readline().strip().split(" "))

inputFile.close()
#====================================================================

#WRITE OUTPUT FILE ===================================================
outputFile = open("output.txt", "w")

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
outputFile.write(d)
outputFile.write("\n")
outputFile.write(N)
outputFile.write("\n")

#write actions
outputFile.write(" ".join(actions))
outputFile.write("\n")

#write fVals
outputFile.write(" ".join(fVals))

outputFile.close()
#====================================================================