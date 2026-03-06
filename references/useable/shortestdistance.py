diagChange = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
nonDiagChange = [[-1, 0], [0, -1], [0, 1], [1, 0]]
from sys import exit

def shortestdistance(grid, startChar = "S", endChar = "X", specList = ["#"], diag = False, isBlackList = True): # grid = 2d list, specList is white/black
    
    H = len(grid)
    W = len(grid[0])
    for r, row in enumerate(grid):
        for c, spot in enumerate(row):
            if spot == startChar: timelines = [[[r, c]]]
            if spot == endChar: endPos = [r, c]
    count = 0
    while True:
        count+=1
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

if __name__ == "__main__":
    griddy = [["X", "#", "S"], [".", "#", "."], [".", ".", "."]]
    print(shortestdistance(griddy))