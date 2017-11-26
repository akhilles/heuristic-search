import random
import math

COLUMNS = 160
ROWS = 120

SLOW_SPOTS = 8
SLOW_RANGE = 31

RIVERS = 4
RIVER_LENGTH = 100
DIR_CHANGE_LENGTH = 20
DIR_CHANGE_PROB = 0.4

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

NAME = '5'


def pickStartGoal(grid):
    width = 5
    minDist = 100

    possiblePoints = []
    for r in range(ROWS):
        for c in range(COLUMNS):
            if grid[r][c] != '0' and (r < width or c < width or r >= (ROWS-width) or c >= (COLUMNS-width)):
                possiblePoints.append((r,c))
    
    points = random.sample(possiblePoints, len(possiblePoints))

    r1,c1 = points[0]
    r2,c2 = points[1]

    index = 1
    while math.sqrt((r2-r1)**2 + (c2-c1)**2) < minDist:
        #print('FAIL')
        index += 1
        r2,c2 = points[index]
    
    return ((r1,c1),(r2,c2))


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

def buildRivers(grid):
    attempts = 0

    while True:
        points = pickRiverStarts()
        attempts += 1
        riverSuccess = True
        riverGrid = [[0] * COLUMNS for i in range(ROWS)]
        for i in range(RIVERS):
            riverSuccess = riverSuccess and buildRiver(points[i][0], points[i][1], points[i][2], grid, riverGrid)
        if riverSuccess:
            break

    for r in range(ROWS):
        for c in range(COLUMNS):
            if riverGrid[r][c] == 1:
                grid[r][c] = chr(ord(grid[r][c][0]) + 48) + ''
            #print(str(grid[r][c]) + ' ', end='')
        #print()
    return attempts

def buildRiver(r, c, d, grid, riverGrid):
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
            partialLength = 0
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
            else: return True


def addBlockedTerrain(grid):
    possiblePoints = []

    for r in range(ROWS):
        for c in range(COLUMNS):
            if grid[r][c] == '1' or grid[r][c] == '2':
                possiblePoints.append((r,c))
    
    points = random.sample(possiblePoints, int(ROWS * COLUMNS * 0.2))
    for r,c in points:
        grid[r][c] = '0'

def addSlowTerrain(r, c, grid):
    spread = (SLOW_RANGE-1) // 2
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
    slowCenters = []
    for point in points:
        r = point // COLUMNS
        c = point % COLUMNS
        slowCenters.append((r,c))
        addSlowTerrain(r,c,grid)
    attempts = buildRivers(grid)
    addBlockedTerrain(grid)

    #print(start)
    #print(goal)
    #print(slowCenters)
    #printGrid(grid)

    for i in range(10):
        start, goal = pickStartGoal(grid)
        saveToFile(start, goal, slowCenters, grid, NAME+'-'+str(i+1))

    return grid

def saveToFile(start, goal, slowCenters, grid, name):
    f = open('benchmark-grids/' + name + '.txt','w')
    f.write(str(start[0]) + ',' + str(start[1]))
    f.write('\n' + str(goal[0]) + ',' + str(goal[1]))
    for r,c in slowCenters:
        f.write('\n' + str(r) + ',' + str(c))
    for row in grid:
        f.write('\n' + ''.join(row))
    f.close()

def loadFromFile(filename):
    f = open(filename,'r')
    ans = []
    allLines = f.readlines()
    start = allLines[0].split(',')
    start = (int(start[0]),int(start[1]))
    goal = allLines[1].split(',')
    goal = (int(goal[0]), int(goal[1]))
    for r in allLines[10:]:
        a = []
        for c in r:
            if(c!='\n'):
                a.append(c)
        ans.append(a)

    f.close()
    return ans, start, goal

if __name__ == '__main__':
    a = loadFromFile("grids/test1.txt")
    print(a)



    grid = generate()