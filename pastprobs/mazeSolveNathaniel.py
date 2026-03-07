diagChange = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
nonDiagChange = [[-1, 0], [0, -1], [0, 1], [1, 0]]
def shortestdistance(grid, startChar = "S", endChar = "X", specList = ["#"], diag = False, isBlackList = True): # grid = 2d list, specList is white/black
    #print(grid)
    if type(endChar) == type([]):
        endPos = endChar
    if type(startChar) == type([]):
        timelines = [[startChar]]
        
    H = len(grid)
    W = len(grid[0])
    for r, row in enumerate(grid):
        for c, spot in enumerate(row):
            if spot == startChar: timelines = [[[r, c]]]
            if spot == endChar: endPos = [r, c]
    count = 0
    while True:
        count+=1
        if count > H*W:
            return False
        changes = nonDiagChange
        if diag: changes = diagChange
        nextTimelines = []
        for timeline in timelines:
            for dr, dc in changes:
                nextR = timeline[-1][0]+dr
                nextC = timeline[-1][1]+dc
                if nextR == H or nextR < 0 or nextC == W or nextC < 0: continue
                
                if [nextR,nextC] == endPos: return timeline + [[nextR,nextC]]
                # Or make a list of all the shortest paths.

                if not isBlackList and grid[nextR][nextC] not in specList and not [nextR,nextC] in timeline:
                    nextTimelines.append(timeline + [[nextR,nextC]])
                if isBlackList and grid[nextR][nextC] not in specList and not [nextR,nextC] in timeline:
                    nextTimelines.append(timeline + [[nextR,nextC]])
        timelines = nextTimelines
import string
def isBlocked(grid, startChar = "S", endChar = "X", specList = ["#"] + list(string.ascii_lowercase.upper()), diag = False, isBlackList = True): # grid = 2d list, specList is white/black
    #print(grid)
    #print(specList)
    if type(endChar) == type([]):
        endPos = endChar
    if type(startChar) == type([]):
        timelines = [[startChar]]
        
    H = len(grid)
    W = len(grid[0])
    for r, row in enumerate(grid):
        for c, spot in enumerate(row):
            if spot == startChar: timelines = [[[r, c]]]
            if spot == endChar: endPos = [r, c]
    count = 0
    while True:
        count+=1
        if count > H*W:
            return False
        changes = nonDiagChange
        if diag: changes = diagChange
        nextTimelines = []
        for timeline in timelines:
            for dr, dc in changes:
                nextR = timeline[-1][0]+dr
                nextC = timeline[-1][1]+dc
                if nextR == H or nextR < 0 or nextC == W or nextC < 0: continue
                
                if [nextR,nextC] == endPos: return True
                # Or make a list of all the shortest paths.

                if not isBlackList and grid[nextR][nextC] not in specList and not [nextR,nextC] in timeline:
                    nextTimelines.append(timeline + [[nextR,nextC]])
                if isBlackList and grid[nextR][nextC] not in specList and not [nextR,nextC] in timeline:
                    nextTimelines.append(timeline + [[nextR,nextC]])
        timelines = nextTimelines

def search(grid, what):
    for r, row in enumerate(grid):
        for c, spot in enumerate(row):
            if spot == what: return [r, c]

with open("pastprobs\\input.txt", "r") as file:
    lines = [list(line) for line in file.read().split("\n")]

lines.pop(0)
#print(isBlocked(lines))

specGrid = []
for r, row in enumerate(lines):
    specGrid.append([])
    for c, spot in enumerate(row):
        if spot in "#" or spot.upper()==spot and spot not in ".S":
            specGrid[r].append("#")
        else:
            specGrid[r].append(".")

def dealWithList(timeLine, pos, first = False):
    print(timeLine)
    for line in specGrid:
        print(line)
    for s, spot in enumerate(timeLine):
        if lines[spot[0]][spot[1]] in "XS" or s==0: continue
        
        if lines[spot[0]][spot[1]] != ".":
            pos = spot
            if not first: print(lines[spot[0]][spot[1]], timeLine)
            if lines[spot[0]][spot[1]].upper() == lines[spot[0]][spot[1]]:
                dealWithList(shortestdistance(specGrid, pos, search(lines, lines[spot[0]][spot[1]].lower())), pos)
            
            if lines[spot[0]][spot[1]].lower() == lines[spot[0]][spot[1]]:
                print(search(lines, lines[spot[0]][spot[1]].upper()))
                specGrid[search(lines, lines[spot[0]][spot[1]].upper())[0]][search(lines, lines[spot[0]][spot[1]].upper())[1]] = "."

#dealWithList(shortestdistance(lines), search(lines, "S"), True)

"""5 6
..S..b
#.#c##
dB.#C.
A#...#
X#D#a."""
"""3 5
S...g
F#G#.
X#.f."""

cur = search(lines, "S")
print(cur)
while isBlocked(lines):
    for position in shortestdistance(lines):
        pos = position
        if lines[pos[0]][pos[1]] in string.ascii_lowercase.upper() and not lines[pos[0]][pos[1]] == "S":
            pass