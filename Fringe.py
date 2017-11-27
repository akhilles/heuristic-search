from heapq import heappush,heappop,heapify

class Fringe():

    h = []
    def __init__(self):
        self.count = 0
        self.h = []

    def insert(self, value, priority):
        heappush(self.h, (priority, self.count, value))
        self.count +=1

    def is_in(self, value):
        for i in self.h:
            if(i[2] == value):
                return True
        return False
    
    def pop(self):
        self.count -=1
        return heappop(self.h)[2]

    def minkey(self):
        return self.h[0][0]

    def remove(self, value):
        item = None
        for i in self.h:
            if (i[2] == value):
                item = i
        self.h.remove(item)
        heapify(self.h)
        self.count -=1

    def top(self):
        return self.h[0][2]

    # def update(self, value, priority):
    #     i = self.h.index(value)
    #     self.h.remove(value)
    #     heappush(self.h, (priority, self.count, value))

    def isEmpty(self):
        return len(self.h) == 0