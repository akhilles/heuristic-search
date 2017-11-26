import generate
import numpy as np
from Fringe import Fringe
import sys
from math import sqrt
from abc import ABC, abstractmethod

class BaseSearch:

    def __init__(self):
        self.grid = None
        self.w = 1
        self.fringe = None
        self.goal = None
        self.start = None
        self.parents = None
        self.f = None
        self.g = None
        self.h = None
        self.expandedCount = 0
        self.path = None
        self.pathCost = 0

    def search(self, grid, start, goal, weight=1):
        self.grid= np.array(grid)
        self.fringe = Fringe()
        self.goal = goal
        self.start = start
        self.settings()
        self.w = weight
        self.expandedCount = 0
        self.path = None
        self.pathCost = 0

        #initialize stuff
        grid = self.grid                          #the main grid
        parents = [[None]*grid.shape[1]]*grid.shape[0]
        self.parents = np.array(parents)
        parents = self.parents                         #grid of parents (a grid of tuples that indicate parent position)
        self.visited = np.zeros(grid.shape)
        visited = self.visited                         #1 if visited a position, 0 if not
        self.g = np.ones(grid.shape)*sys.maxsize
        self.f = np.zeros(grid.shape)
        f = self.f
        self.h = np.zeros(grid.shape)
        self.hGrid()
        g = self.g                                     #grid of g values (distance from start)
        h = self.h
        fringe = self.fringe                           #just a priority queue

        g[start] = 0
        parents[start] = start
        fstart = g[start] + h[start]*self.w
        f[start] = fstart
        fringe.insert(start,fstart)

        while(not fringe.isEmpty()):
            s = fringe.pop()
            if(s==goal):
                print('found')
                self.path = self.getPath()
                return self.path
            visited[s] = 1
            for sp in self.expand(s):
                self.expandedCount +=1
                if visited[sp]==0 and grid[sp]!='0':
                    self.updateVertex(s, sp)
        print('not found')
        return parents


    def updateVertex(self, s, sp):
        g = self.g
        if(g[s]+self.points_cost(s,sp) < g[sp]):
            g[sp] = g[s] + self.points_cost(s,sp)
            self.parents[sp] = s
            if(self.fringe.is_in(sp)):
                self.fringe.remove(sp)
            fval = g[sp] + self.h[sp]*self.w
            self.f[sp] = fval
            self.fringe.insert(sp, fval)


    #defines the heuristic for a given vertex
    def heuristic(self, v):
        pass

    def hGrid(self):
        h = self.h
        for r,row in enumerate(h):
            for c,col in enumerate(row):
                h[r,c] = self.heuristic((r,c))*self.w


    #returns the successors to the input vertex as a list
    def expand(self, v):
        M,N = self.grid.shape[0],self.grid.shape[1]
        l = []
        for i in [1,-1]:
            l.append((v[0] + i, v[1]))
            l.append((v[0], v[1] + i))
            l.append((v[0] + i, v[1] + i))
            l.append((v[0] + i, v[1] - i))

        ans = []
        for i in l:
            if(i[0]<M and i[1]<N and i[0]>=0 and i[1]>=0):
                ans.append(i)
        return ans



    def points_cost(self, p1, p2):
        grid = self.grid
        hard = ['2', 'b']
        highway = ['a','b']
        type1 = grid[p1]
        type2 = grid[p2]
        cost = 0
        if(p1==p2):
            return cost

        if(p1[0] == p2[0] or p1[1]==p2[1]):
            cost = 1
        else:
            cost=sqrt(2)

        if(type1 in hard and type2 in hard):
            cost = cost*2
        elif(type1 in hard or type2 in hard):
            cost = (cost+2*cost)/2.0

        if ((p1[0] == p2[0] or p1[1] == p2[1]) and type1 in highway and type2 in highway):
            cost = cost*.25

        return cost

    def getPath(self):
        path = []
        s = self.goal
        while(s!=self.start):
            path.insert(0,s)
            p = self.parents[s]
            self.pathCost += self.points_cost(p,s)
            s = p
        path.insert(0,self.start)

        return path

    def writeToFile(self, input, output):
        grid,start,goal = generate.loadFromFile(input)
        file = open(output, 'w+')

        file.write(self.printGrid(self.f, file)+'\n')
        file.write(self.printGrid(self.g, file)+'\n')
        file.write(self.printGrid(self.h, file)+'\n')
        file.write(','.join(str(x) for x in self.path)+'\n')
        file.write(str(self.expandedCount))
        file.close()



    def printGrid(self, grid, file):
        s = ''
        for r in grid:
            s+=(','.join(str(x) for x in r)+'\n')
        return s

    def settings(self):
        pass



if(__name__ == '__main__'):
    grid,start,goal = np.array(generate.loadFromFile("grids/grid.txt"))
    # grid[(1,18)] = 'a'
    # grid[(1,19)] = 'b'
    # print(grid)
    # print(points_cost( (0,0), (0,19), grid))
    # print(points_cost((0, 0), (0, 18), grid))
    # print(points_cost((0, 0), (1, 1), grid))
    bs = BaseSearch()
    print(bs.search(grid,start,goal))





