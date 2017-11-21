import random

COLUMNS = 16
ROWS = 12

SLOW_SPOTS = 8
SLOW_RANGE = 31

RIVERS = 4
RIVER_LENGTH = 20
DIR_CHANGE_LENGTH = 4
DIR_CHANGE_PROB = 1.1

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def pickRiverStarts():
    possiblePoints = []
    for r in range(1, ROWS-1):
        possiblePoints.append((r,0,EAST))
        possiblePoints.append((r,COLUMNS-1,WEST))
    for c in range(1, COLUMNS-1):
        possiblePoints.append((0,c,SOUTH))
        possiblePoints.append((ROWS-1,c,NORTH))
    
    points = random.sample(possiblePoints, RIVERS)
    return points


def buildRiver(r, c, d, grid):
    riverGrid = [[0] * COLUMNS for i in range(ROWS)]
    totalLength = 0
    partialLength = 0
    while True:
        if riverGrid[r][c] == 0:
            riverGrid[r][c] = 1
        else:
            return False
        partialLength += 1
        totalLength += 1

        if partialLength == DIR_CHANGE_LENGTH:
            partialLength = 1
            roll = random.uniform(0,1)
            if roll < DIR_CHANGE_PROB:
                if d % 2 == 0: d = random.choice([1,3])
                else: d = random.choice([0,2])
        
        if d == NORTH: r -= 1
        elif d == EAST: c += 1
        elif d == SOUTH: r += 1
        else: c -= 1

        if r < 0 or c < 0 or r >= ROWS or c >= COLUMNS:
            if totalLength < RIVER_LENGTH: return False
            else: return riverGrid
            

def addSlowTerrain(r, c, grid):
    spread = (SLOW_RANGE-1) / 2
    spread = 2
    rowStart = max(0, r-spread)
    rowEnd = min(r+spread, ROWS-1)
    colStart = max(0, c-spread)
    colEnd = min(c+spread, COLUMNS-1)

    for i in range(rowStart,rowEnd+1):
        for j in range(colStart,colEnd+1):
            if random.choice([True, False]):
                grid[i][j] = '2'

def printGrid(grid):
    for row in grid:
        print(*row, sep=' ')

def generate():
    grid = [['1'] * COLUMNS for i in range(ROWS)]
    points = random.sample(range(ROWS*COLUMNS), SLOW_SPOTS)
    for point in points:
        r = point // COLUMNS
        c = point % COLUMNS
        print(r,c)
        addSlowTerrain(r,c,grid)
    return grid

grid = generate()
points = pickRiverStarts()

riverSuccess = False

while not riverSuccess:
    riverGrid = buildRiver(points[0][0], points[0][1], points[0][2], grid)
    if riverGrid: break

printGrid(grid)
print()
printGrid(riverGrid)