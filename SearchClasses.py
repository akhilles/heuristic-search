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


if(__name__ == '__main__'):
    grid,start,goal = np.array(generate.loadFromFile("benchmark-grids/1-2.txt"))

    uc = UniformCost()
    astar = AStar()
    asw = AStarWeighted(2.5)
    print(uc.search(grid,start,goal))
    print(astar.search(grid, start, goal))
    print(asw.search(grid, start, goal))
