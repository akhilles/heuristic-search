from search import BaseSearch
from math import sqrt
import os
import numpy as np
import generate
import math

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

class Admissible(BaseSearch):

    def heuristic(self, v):
        return 0.25*(abs((v[0] - self.goal[0])) + abs((v[1] - self.goal[1])))

class Custom1(BaseSearch):

    def heuristic(self, v):
        M, N = self.grid.shape[0], self.grid.shape[1]
        return abs((v[0] - self.goal[0]))*(M/(M+N)) + abs((v[1] - self.goal[1]))*(N/(M+N))

class Custom2(BaseSearch):

    def heuristic(self, v):
        M, N = self.grid.shape[0], self.grid.shape[1]
        return sqrt((M/(M+N))*(v[0] - self.goal[0]) ** 2 + (N/(M+N))*(v[1] - self.goal[1]) ** 2)



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
    fname = "benchmark-grids/2-8.txt"
    grid,start,goal = np.array(generate.loadFromFile(fname))

    uc = UniformCost()
    astar = AStar()
    asw = AStar()
    man = Manhattan()

    print(uc.search(grid,start,goal))

    print(uc.expandedCount)
    print(uc.pathCost)
    # uc.writeToFile(fname)
    print(astar.search(grid, start, goal, weight=1))
    print(astar.expandedCount)
    print(astar.pathCost)
    # astar.writeToFile(fname)
    print(asw.search(grid, start, goal, weight=2.5))
    print(asw.expandedCount)
    print(asw.pathCost)
    # asw.writeToFile(fname, "grids/gridsol.txt")
    print(man.search(grid, start, goal, weight=1))
    print(man.expandedCount)
    print(man.pathCost)

    adm = Admissible()
    print(adm.search(grid, start, goal, weight=1))
    print(adm.expandedCount)
    print(adm.pathCost)

    cust1 = Custom1()
    print(cust1.search(grid, start, goal, weight=1))
    print(cust1.expandedCount)
    print(cust1.pathCost)

    cust2 = Custom2()
    print(cust2.search(grid, start, goal, weight=1))
    print(cust2.expandedCount)
    print(cust2.pathCost)
