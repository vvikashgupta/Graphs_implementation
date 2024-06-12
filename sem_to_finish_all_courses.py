#!/usr/local/bin/python


class Graph:
    def __init__(self, vertexId):
        self.vertexId = vertexId
        self.adjacent = set()
        
    def addEdge(self, v):
        if v != self.vertexId:
            self.adjacent.add(v)
    
    def getadjacent(self):
        return self.adjacent
    
class graphSet:
    def __init__(self, numvertex, directed=True):
        self.numvertex = numvertex
        self.directed = directed
        self.vertices = []
        for i in range(0,numvertex+1):
            self.vertices.append(Graph(i))
        print("=====Vertices list is ====")
        print(len(self.vertices))
        print(self.vertices)
            
    def checkLoop(self, v1, v2):
        if 0<v1<= self.numvertex or 0<v2<= self.numvertex or v1 != v2:
            for index in range(1,self.numvertex+1):
                adjacent = self.vertices[index].getadjacent()
                if v1 in adjacent and v2 in adjacent:
                    return True
            return False
            
    def addEdge(self, v1, v2):
        if 0<v1<=self.numvertex or 0<v2<=self.numvertex or v1 != v2:
            self.vertices[v1].addEdge(v2)
            if not self.directed:
                self.vertices[v2].addEdge(v1)
            #Here check if there exist a loop in the graph.
        else:
            raise ValueError("Invalid vertexId provided")
            return True # Ignoring this edge.
    
    def getadjacent(self, v):
        if 0<v<= self.numvertex:
            return self.vertices[v].getadjacent()
        
    def getindegree(self, v):
        count = 0
        print(f'get indegree for {v}')
        if 0<v<= self.numvertex:
            for node in self.vertices[1:]:
                if node.vertexId != v and v in node.getadjacent():
                    count += 1
        else:
            print("Value error in vertexId")
        print(f' indegree for {v} is {count}')
        return count

    def display(self):
        for element in self.vertices:
            print(f' VertaxId {element.vertexId} ----> {element.getadjacent()}')
    
class Solution:
    def minimumSemesters(self, N, relations) -> int:
        print(f'{N}, {relations}')
        graph = graphSet(N)
        for lst in relations:
            graph.addEdge(lst[1], lst[0])
        
        from collections import deque, defaultdict
        deq = deque()
        dict = defaultdict()
        graph.display()
    
        result = []
        for i in range(1,graph.numvertex+1):
            dict[i] = graph.getindegree(i)
            if not dict[i]:
                deq.append([i,1])
        print("===========")
        print(dict)
        while deq:
            index, level = deq.popleft()
            result.append([index,level])
            print(f'append index {index} at level {level}')
            for i in range(1,graph.numvertex+1):
                print(f'update the indegree map for {i}')
                if i == index:
                    print('No update. Continue')
                    continue
                print(f'Check {index} in {graph.getadjacent(i)} for index {i}')
                if index in graph.getadjacent(i):
                    dict[i] -= 1
                    if not dict[i]:
                        print(f'deq index {index} at level {level + 1}')
                        deq.append([i, level+1])
        
        print("===========")
        print(f'result{result} , level {level}')
       
        if len(result) == graph.numvertex:
            return level
        else:
            return -1
        
            
        
def main():
    s = Solution()
    print(s.minimumSemesters(3, [[1,3],[2,3]]))


if __name__ == '__main__':
    main()
