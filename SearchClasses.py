from search import BaseSearch
from math import sqrt
import os
import numpy as np
import generate
import math
from Fringe import Fringe
import time
import sys

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

class Custom3(BaseSearch):

    def heuristic(self, v):
        return max(abs((v[0] - self.goal[0])) , abs((v[1] - self.goal[1])))

class Sequential(BaseSearch):

    def searchAll(self, grid, start, goal, w1=1, w2=1):#goal,start
        self.searches = [Admissible(), Manhattan(), Custom1(), Custom2(), Custom1()]
        self.w1 = w1
        self.w2 = w2
        self.grid = np.array(grid)
        self.start = start
        self.goal = goal
        self.expandedCount = 0
        self.pathCost = 0
        self.path = None

        for searcher in self.searches:
            searcher.grid = self.grid
            searcher.start = self.start
            searcher.goal = self.goal
            searcher.path = None
            searcher.pathCost = 0
            searcher.fringe = Fringe()
            searcher.parents = [[None]*self.grid.shape[1]]*self.grid.shape[0]
            searcher.parents = np.array(searcher.parents)
            searcher.visited = np.zeros(self.grid.shape)
            searcher.g = np.ones(self.grid.shape)*sys.maxsize
            searcher.h = np.zeros(self.grid.shape)
            searcher.f = np.zeros(self.grid.shape)

            searcher.g[start] = 0
            searcher.parents[searcher.start], searcher.parents[searcher.goal] = None,None
            fstart = searcher.g[searcher.start] + searcher.heuristic(start) * self.w1
            searcher.f[searcher.start] = fstart
            searcher.fringe.insert(searcher.start, fstart)

        open0 = self.searches[0].fringe
        admis = self.searches[0]
        while(open0.minkey() < sys.maxsize):
            for i,searcher in enumerate(self.searches):
                if(searcher.fringe.minkey() <= self.w2*open0.minkey() ):
                    if(searcher.g[searcher.goal] <= searcher.fringe.minkey()):
                        if(searcher.g[searcher.goal] < sys.maxsize):
                            self.path = searcher.getPath()
                            self.pathCost += searcher.pathCost
                            return searcher.getPath()
                    else:
                        s = searcher.fringe.top()
                        self.expandState(s, i)
                        searcher.visited[s] = 1
                else:
                    if(self.searches[0].g[self.goal] <= open0.minkey()):
                        if(admis.g[self.goal] < sys.maxsize):
                            self.path = admis.getPath()
                            self.pathCost += admis.pathCost
                            return admis.getPath()
                    else:
                        s = open0.top()
                        self.expandState(s, 0)
                        admis.visited[s] = 1

    def key(self, s, i):
        return self.searches[i] + self.searches[i].heuristic(s)

    def expandState(self, s, i):
        self.expandedCount += 1
        searcher = self.searches[i]
        fringe = self.searches[i].fringe
        fringe.remove(s)
        for sp in searcher.expand(s):
            if(searcher.g[s] + searcher.points_cost(s,sp) < searcher.g[sp]):
                searcher.g[sp] = searcher.g[s] + searcher.points_cost(s,sp)
                searcher.parents[sp] = s
                if(searcher.visited[sp] == 0 and searcher.grid[sp] != '0'):
                    if (fringe.is_in(sp)):
                        fringe.remove(sp)
                    fval = searcher.g[sp] + searcher.heuristic(sp) * self.w1
                    searcher.f[sp] = fval
                    fringe.insert(sp, fval)


def benchmark(searchClass, weight=1):
    gridNames = os.listdir("benchmark-grids")
    pathCost = 0
    expandedNodes = 0
    visitedOptimum = 0
    startTime = time.time()
    for name in gridNames:
        #print(name + ': ', end='')
        grid,start,goal = np.array(generate.loadFromFile("benchmark-grids/" + name))
        instance = searchClass()
        path = instance.search(grid, start, goal, weight=weight)
        optimum = max(abs(goal[0]-start[0]), abs(goal[1]-start[1]))
        visitedOptimum += len(path)/optimum
        pathCost += instance.pathCost
        expandedNodes += instance.expandedCount
    endTime = time.time()

    print('-', searchClass.__name__ + ',', 'w:', weight)
    print('average path cost:      ', pathCost/50)
    print('average expanded nodes: ', expandedNodes/50)
    print('average run time:       ', (endTime-startTime)/50)
    print('average visited/optimum:', visitedOptimum/50)

def benchmarkSeq(w1=1, w2=1):
    searchClass = Sequential
    gridNames = os.listdir("benchmark-grids")
    pathCost = 0
    expandedNodes = 0
    visitedOptimum = 0
    startTime = time.time()
    for name in gridNames:
        #print(name + ': ', end='')
        grid,start,goal = np.array(generate.loadFromFile("benchmark-grids/" + name))
        instance = searchClass()
        path = instance.searchAll(grid, start, goal, w1=w1, w2=w2)
        optimum = max(abs(goal[0]-start[0]), abs(goal[1]-start[1]))
        visitedOptimum += len(path)/optimum
        pathCost += instance.pathCost
        expandedNodes += instance.expandedCount
    endTime = time.time()

    print('-', searchClass.__name__ + ',', 'w1:', w1, 'w2:', w2)
    print('average path cost:      ', pathCost/50)
    print('average expanded nodes: ', expandedNodes/50)
    print('average run time:       ', (endTime-startTime)/50)
    print('average visited/optimum:', visitedOptimum/50)

if(__name__ == '__main__'):
    uc = UniformCost()
    astar = AStar()
    asw = AStar()
    man = Manhattan()

    # grid, start, goal = np.array(generate.loadFromFile("grids/1-1.txt"))
    # seq = Sequential()
    # print(seq.searchAll(grid, start, goal, w2=1.2))
    # print(seq.expandedCount)
    # print(seq.pathCost)
    #
    # print(uc.search(grid,start,goal))
    # print(uc.expandedCount)
    # print(uc.pathCost)


    weights1 = [1, 1.5, 2]
    weights2 = [1, 1.2, 1.5]

    for w1 in weights1:
        for w2 in weights2:
            benchmarkSeq(w1,w2)

    # weights = [0,1,1.5,2.5]
    # classes = [Admissible, Manhattan, Custom1, Custom2, Custom3]
    #
    # for c in classes:
    #     for w in weights:
    #         benchmark(c,w)
