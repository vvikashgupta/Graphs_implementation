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
        for lst in edges:
            matrix.addEdge(lst[0],lst[1])
            
        from collections import deque, defaultdict
        deq = deque()
        print(f'{n}, {edges}')     
        matrix.display()
        def check_loop(i, j):
            nonlocal matrix
            print(f'check_loop {i},{j}')
            for index in range(matrix.vertices):
                if index == i or index == j:
                    continue
                print(f'{index} index,i is {matrix.matrix[index][i]} and index,j is{matrix.matrix[index][j]}')
                if matrix.matrix[index][i] and matrix.matrix[index][j]:
                    print('check_loop return True')
                    return True
                else:
                    print('check_loop return False')
            return False
                
                
        #prepare indegree map of graph.
        dict = defaultdict()
        seen = set()
        deq.append(0)
        while deq:
            ver = deq.popleft()
            print(f' Next vertex to process is {ver}')
            if ver in seen:
                print('Already seen continue')
                continue
            else:
                seen.add(ver)
            for i in matrix.get_adjacencies(ver):
                print(f' Check adjacencies and loop with {i}')
                deq.append(i)
                #matrix.matrix[i][ver] = 0
                if check_loop(i,ver):
                    return False
       
        print(f' return based on {len(seen)}, {matrix.vertices}') 
        if len(seen) == matrix.vertices:
            return True
        else:
            return False
                

def main():
    s = Solution()
    print(s.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]))


if __name__ == '__main__':
   main()
