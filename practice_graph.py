#import sys,os
from collections import deque
from time import sleep
sleep_time = 30
class Graph():
    def __init__(self, no_of_vertices, directed=False, weigh=1):
        self.no_of_vertices = no_of_vertices
        self.directed = directed
        self.weigh = weigh

class Node():
    def __init__(self, vertaxId):
        self.vertaxId = 0
        self.adjacencies = set()

    def addEdge(self, v):
        if self.vertaxId != v:
            self.adjacencies.add(v)
            return True
        else:
            return False

    def getAdjacencies(self):
        return self.adjacencies

class AdjacentInfo(Graph):
    def __init__(self, no_of_vertices, directed=False, weigh=1):
        super().__init__(no_of_vertices, directed, weigh)
        self.verticeslist = []
        for i in range(no_of_vertices):
            sleep(sleep_time)
            self.verticeslist.append(Node(i))

    def addEdge(self, v1, v2):
        #if 0>= v1 < self.no_of_vertices and 0<= v2 < self.no_of_vertices:
        #    print(f'Incorrect data { v1} or {v2} is outside range of 0, {self.no_of_vertices} ')
        #    return False
        if v1 in self.verticeslist[v2].getAdjacencies():
            print(f' Cyclic dependency. Skip adding this element')
            return False
        else:
            self.verticeslist[v2].addEdge(v1)
            if not self.directed:
                self.verticeslist[v1].addEdge(v2)
        return True

    def get_adjanceies(self, v):
        if 0<= v <= self.no_of_vertices:
            return self.verticeslist[v].getAdjacencies()

    def get_indegree(self, v):
        indegree = 0
        if 0<= v <= self.no_of_vertices:
            for i in range(self.no_of_vertices):
                if v in self.verticeslist[i].getAdjacencies():
                    indegree += 1
        return indegree 

    def printme(self):
        for i in range(self.no_of_vertices):
            print(f' Vertax {i} ---> adjacent to {self.verticeslist[i].getAdjacencies()}')

class Solution():
    def canFinish(self, no_of_course, prereq):
        self.ainfo = AdjacentInfo(no_of_course, directed=True)
        for lst in prereq:
            status = self.ainfo.addEdge(lst[0],lst[1])
            if not status:
                return False

         # Let us build a inorder map here.
        inorder_map = {}
        deq = deque()
        for i in range(self.ainfo.no_of_vertices):
            inorder_map[i] = self.ainfo.get_indegree(i)
            if not inorder_map[i]:
                 deq.append(i)

        result_array = []
        while deq:
            vertax = deq.popleft()
            result_array.append(vertax)
            for v in self.ainfo.verticeslist[vertax].getAdjacencies():
                inorder_map[v] -= 1
                if not inorder_map[v]:
                    deq.append(v)
        
        return True if len(result_array) == self.ainfo.no_of_vertices else False

def main():
    s = Solution()
    print(f'{s.canFinish(2,[[1,0],[0,1]])}')

if __name__ == '__main__':
    main()

 
