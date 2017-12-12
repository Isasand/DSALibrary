# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 08:57:11 2017

@author: Isa
"""

    
class Graph: 
        def __init__(self): 
            self._table = {} 
            
        def isEmpty(self):
            return self.size()  == 0 
        
        def size(self): 
            return len(self._table.keys())
        
        def addVertex(self, v):
            if v not in self._table.keys(): 
                self._table[v] = set([])
                
        def removeVertex(self, v):
            if v in self._table.keys(): 
                del self._table[v]
            #obs måste också ta bort alla values ,ed v 
            
        def addEdge(self, v1, v2, weight = 1, directed = False):
            if not v1 in self._table.keys(): 
                self.addVertex(v1)
            self._table[v1].add((v2, weight))
            if not directed: 
                if not v2 in self._table.keys():
                    self.addVertex(v2)
                self._table[v2].add((v1, weight))
            #self._table[v1].add(v2)
            
        def removeEdge(self, v1, v2):
            if v2 in self._table[v1]:
                self._table[v1].remove(v2)
            if v1 in self._table[v2]:
                self._table[v2].remove(v1)
            #om grafen är riktad tar vi bort de sista två raderna 
            
        def areNeighbours(self, v1, v2):
            if v1 in self._table.keys():
                for (v, w) in self._table[v1]:
                    if v == v2:
                        return True
            return False
        
        #depth first 
        def findDFSPath(self, v1, v2, visited = []):
            if self.areNeighbours(v1, v2): #base case
                return [v1, v2]
            
            neighbours = self._table[v1]
            for n in neighbours:
                if n not in visited:
                    p = self.findDFSPath(n[0], v2, visited + [v1])
                    if p != None:
                        return [v1] + p #path found
            
            return None #no path found
        
        def isConnected(self):
            for v1 in self._table.keys(): 
                for v2 in self._table.keys(): 
                    #For each pair of nodes, see if there is a path? 
                    if v1 != v2 and not self.findDFSPath(v1, v2):
                        return False
            return True 
        
        def cost(self, v1, v2):
            if v1 in self._table.keys(): 
                for (v, w) in self._table[v1]:
                    if v == v2: 
                        return w 
            return 0 
        
        def findAllPaths(self, start, end, visited = []):
            visited = visited + [start]
            
            if start == end: 
                return [visited]
            
            if start not in self._table.keys():
                return []
            paths = []
            neighbours = self._table[start]
            for node in neighbours:
                if node[0] not in visited:
                    newPaths = self.findAllPaths(node[0], end,visited)
                    for newPath in newPaths: 
                        paths.append(newPath)
            return paths 
            
        def findShortestPath(self, start, end, visited = []):
            visited = visited + [start]
            if start == end: 
                return visited

            if start not in self._table.keys(): 
                return None 
            
            shortest = None 
            neighbours = self._table[start]
            for node in neighbours: 
                if node[0] not in visited: 
                    newPath = self.findShortestPath(node[0], end, visited)
                    if newPath: 
                        if not shortest or len(newPath) < len(shortest):
                            shortest = newPath
            return shortest 
        
        def findCostOfPath(self, path):
            cost = 0
            for i in range(len(path)):
                if i < len(path)-1:
                    cost += self.cost(path[i], path[i+1])
            return cost 
            
        def findCheapestPath(self, start, end, visited = []):
            paths = self.findAllPaths(start, end, visited = [])
            cheapest = 0
            returnPath = ([])
            for path in paths: 
                cost = 0
                cost += self.findCostOfPath(path)
                if cheapest == 0: 
                    cheapest = cost 
                    returnPath = (path, cheapest)
                if cost < cheapest:
                    cheapest = cost
                    returnPath = (path, cheapest)
            return returnPath #cheapest