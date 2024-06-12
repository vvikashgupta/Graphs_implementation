#!/usr/loca/bin/python

import numpy as np
class Graph:
    def __init__(self, vertices, directed=False, weight=0):
        self.vertices = vertices
        self.directed = directed
        self.weight = weight
        
# Let us use matrix solution here
class graphMatrix(Graph):
    def __init__(self, vertices, directed=False, weight=0):
        
        super().__init__(vertices, directed, weight)
        self.matrix = [[0 for i in range(vertices)] for j in range(vertices)]
        
    def addEdge(self, v1, v2):
        if 0<=v1<=self.vertices and 0<=v2<=self.vertices and v1 != v2:
            # Add the edge.
            self.matrix[v1][v2] = 1
            if not self.directed:
                self.matrix[v2][v1] = 1
        else:
            print("Error Vertices out of range. Continue without adding.")
            
    def get_adjacencies(self, v):
        result = []
        if 0<=v<=self.vertices:
            for i in range(self.vertices):
                if self.matrix[v][i]:
                    result.append(i)
        else:
            print('Error wrong vertex')
        return result
    
    def get_indegree(self, v):
        count = 0
        if 0<=v<=self.vertices:
            for i in range(self.vertices):
                if self.matrix[i][v]:
                    count += 1
        else:
            print('Error wrong vertex')
        return count

    def display(self):
        for first_index in range(self.vertices):
            for sec_index in range(self.vertices):
                if self.matrix[first_index][sec_index]:
                    print(f' {first_index} <---> {sec_index}')
        
        
class Solution:
    def validTree(self, n, edges):
        matrix = graphMatrix(n)
        print(f'{n}, {edges}')
        for lst in edges:
            matrix.addEdge(lst[0],lst[1])
            
        from collections import deque, defaultdict
        deq = deque()
        matrix.display() 
        #prepare indegree map of graph.
        dict = defaultdict()
        for i in  range(matrix.vertices) :
            dict[i] = matrix.get_indegree(i)
            print(f'indegree map of {i} is {dict[i]}')
            if dict[i] == 1:
                print(f'Append {i} to deque')
                deq.append(i) # Add to the list the node which has zero inbound edges
        
        #Indegree map is completed. Now find the valididity of the graph.
        print(f'indegree map is {dict}')
        result = []
        while deq:
            vertex = deq.popleft()
            result.append(vertex)
            print(f'Verex traversed is {vertex}')
            for i in matrix.get_adjacencies(i):
                dict[i] -= 1
                if dict[i] == 1: #Now it's indegree are zero.
                    deq.append(i)
        print(f'ree map is {dict} result is {result}')
        print(f'{matrix.vertices} , {len(result)}')
        if len(result) == matrix.vertices:
            return True
        else:
            return False

def main():
    s = Solution()
    print(s.validTree(5, [[0,1],[0,2],[0,3],[1,4]]))
    print('+++++++++++++++')
    print(s.validTree(4, [[0,1],[2,3]]))

if __name__ == '__main__':
    main()

