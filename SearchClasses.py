from search import BaseSearch
from math import sqrt
import os
import numpy as np
import generate
import math
import time

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
        self.pathCost = 0
    # def settings(self, weight):
    #     self.w = weight
    #     self.expandedCount = 0
    #     self.pathCost = 0


class Manhattan(BaseSearch):

    def heuristic(self,v):
        return abs((v[0] - self.goal[0])) + abs((v[1] - self.goal[1]))

def d2Heur(v, goal):
    return sqrt((v[0] - goal[0]) ** 2 + (v[1] - goal[1]) ** 2)


def benchmark(searchClass):
    gridNames = os.listdir("benchmark-grids")
    pathCost = 0
    expandedNodes = 0
    visitedOptimum = 0
    startTime = time.time()
    for name in gridNames:
        print(name + ': ', end='')
        grid,start,goal = np.array(generate.loadFromFile("benchmark-grids/" + name))
        path = searchClass.search(grid, start, goal)
        optimum = max(abs(goal[0]-start[0]), abs(goal[1]-start[1]))
        visitedOptimum += len(path)/optimum
        pathCost += searchClass.pathCost
        expandedNodes += searchClass.expandedCount
    endTime = time.time()
    print('average path cost:      ', pathCost/50)
    print('average expanded nodes: ', expandedNodes/50)
    print('average run time:       ', (endTime-startTime)/50)
    print('average visited/optimum:', visitedOptimum/50)

if(__name__ == '__main__'):
    benchmark(UniformCost())

'''
    fname = "grids/1-1.txt"
    grid,start,goal = np.array(generate.loadFromFile(fname))

    uc = UniformCost()
    astar = AStar()
    asw = AStar()
    man = Manhattan()

    print(uc.search(grid,start,goal))

    print(uc.expandedCount)
    print(uc.pathCost)
    uc.writeToFile(fname)
    print(astar.search(grid, start, goal, weight=1))
    print(astar.expandedCount)
    print(astar.pathCost)
    # astar.writeToFile(fname, "benchmark-grids/1-2sol.txt")
    print(asw.search(grid, start, goal, weight=2.5))
    print(asw.expandedCount)
    print(asw.pathCost)
    # asw.writeToFile(fname, "grids/gridsol.txt")
    print(man.search(grid, start, goal, weight=1))
    print(man.expandedCount)
    print(man.pathCost)
    #
    # fname = "benchmark-grids/4-8.txt"
    # grid, start, goal = np.array(generate.loadFromFile(fname))
    # print(uc.search(grid, start, goal))
    #
    # uc.writeToFile(fname, "benchmark-grids/1-2sol.txt")
'''