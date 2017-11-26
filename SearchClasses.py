from search import BaseSearch
from math import sqrt
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


if(__name__ == '__main__'):
    fname = "benchmark-grids/1-2.txt"
    grid,start,goal = np.array(generate.loadFromFile(fname))

    uc = UniformCost()
    astar = AStar()
    asw = AStarWeighted(2.5)
    print(uc.search(grid,start,goal))
    # uc.writeToFile(fname, "benchmark-grids/1-2sol.txt")
    print(astar.search(grid, start, goal))
    astar.writeToFile(fname, "benchmark-grids/1-2sol.txt")
    print(asw.search(grid, start, goal))
