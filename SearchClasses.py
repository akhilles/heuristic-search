from search import BaseSearch
from math import sqrt
import os
import numpy as np
import generate

class UniformCost(BaseSearch):

    def heuristic(self, v):
        return 0

class AStar(BaseSearch):

    def heuristic(self, v):
        return sqrt((v[0] - self.goal[0])**2 +(v[1] - self.goal[1])**2)

class AStarWeighted(AStar):

    def __init__(self, weight):
        super.__init__(super())
        self.w = weight
        self.expandedCount = 0

def benchmark():
    gridNames = os.listdir("benchmark-grids")
    pathLength = 0
    do = ['4-7.txt', '4-8.txt']
    for name in gridNames:
        if name not in do:
            continue
        astar = UniformCost()
        print(name + ': ', end='')
        grid,start,goal = np.array(generate.loadFromFile("benchmark-grids/" + name))
        path = astar.search(grid, start, goal)
        pathLength += len(path)
    print('average path length:', pathLength/50)

if(__name__ == '__main__'):
    fname = "benchmark-grids/1-2.txt"
    grid,start,goal = np.array(generate.loadFromFile(fname))

    uc = UniformCost()
    astar = AStar()
    asw = AStarWeighted(2.5)
    print(uc.search(grid,start,goal))
    uc.writeToFile(fname, "benchmark-grids/1-2sol.txt")