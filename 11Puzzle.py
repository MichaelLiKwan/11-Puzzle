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

readFile = open("input.txt", "r")
state = []
goal = []

#read first three lines as initial state
for i in range(3):
    state.append(readFile.readline().strip().split(" "))

#skip the fourth line, which is blank
readFile.readline()

#read last three lines as goal state
for i in range(3):
    goal.append(readFile.readline().strip().split(" "))

readFile.close()