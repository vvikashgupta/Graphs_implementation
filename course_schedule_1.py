#!/usr/local/bin/python


class Graph:
    def __init__(self, num_of_vertax, directed=False, weight=1):
        self.vertaxes = num_of_vertax
        self.directed = directed
        self.weight = weight
        
        
class Node:
    def __init__(self, vertaxId):
        self.vertaxId = vertaxId
        self.adjacencies = set()
        
    def addEdge(self, v):
        if v != self.vertaxId:
            self.adjacencies.add(v)
            print(f'node addEdge {v}, {self.adjacencies}')
        else:
            print("Value Error")
            
    def get_adjacencies(self):
        return self.adjacencies
    
class Adjacentinfo(Graph):
    def __init__(self, vertexes, directed=False, weight=1):
        super().__init__(vertexes, directed, weight)
        self.vertices_lst = []
        for i in range(vertexes):
            self.vertices_lst.append(Node(i))
        
    def addEdge(self, v1, v2):
        print(f'{v1},{v2} {self.vertices_lst[v2].get_adjacencies()} end')
        if v1 in self.vertices_lst[v2].get_adjacencies():
            print("Cyclic dependency exist. Skip adding this node")
            return False
        if 0 <= v1 < self.vertaxes and 0<=v2<self.vertaxes:
            print('call node addEdge')
            self.vertices_lst[v1].addEdge(v2)
        if not self.directed:
            self.vertices_lst[v2].addEdge(v1)
        return True
    
    def get_adjacencies(self, v):
        if 0<v<self.vertaxes:
            return self.vertices_lst[v].get_adjacencies()
        
    def get_indegree(self, v):
        count = 0
        if 0<=v<self.vertaxes:
            for node in self.vertices_lst:
                if node.vertaxId != v and v in node.get_adjacencies():
                    count += 1
        else:
            print(f"Value error. Invalid vertaxId {v} {self.vertaxes}")
        return count
    
    def printme(self):
        for i in range(self.vertaxes):
            print(f' Vertax {i} adjacent ----> {self.get_adjacencies()}')
            
            
        
class Solution:
    def canFinish(self, numCourses, prerequisites) :
        from collections import deque
        self.Ainfo = Adjacentinfo(numCourses, directed=True)
        for lst in prerequisites:
            status = self.Ainfo.addEdge(lst[0],lst[1])
            if not status:
                return False
                
        
        #Let us do a topological sort here.
        inorder_map = {}
        deq = deque()
        for node in self.Ainfo.vertices_lst:
            inorder_map[node.vertaxId] = self.Ainfo.get_indegree(node.vertaxId)
            if not inorder_map[node.vertaxId]:
                deq.append(node.vertaxId)
        
        sorted_array = []
        while deq:
            vertex = deq.popleft()
            sorted_array.append(vertex)
            for v in self.Ainfo.vertices_lst[vertex].get_adjacencies():
                inorder_map[v] -= 1
                if not inorder_map[v]:
                    deq.append(v)
        if len(sorted_array) != self.Ainfo.vertaxes:
            return False
        else:
            return True

def main():
    s = Solution()
    print(f'{s.canFinish(2,[[1,0],[0,1]])}')

if __name__ == '__main__':
    main()
