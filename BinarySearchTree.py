# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 19:04:31 2017

@author: Isa
"""

class BinarySearchTree(object):
    
    def __init__(self, data):
        self._data = data
        self._left = None 
        self._right = None
        
        
    def getData(self):
        return self._data
    
    def setData(self, argData):
        self._data = argData
        
    def isEmpty(self):
        return self._left == self._right == self._data == None
    
    def size(self):
        sz = 0
        if self._left:
            sz +=self._left.size()
        if self.getData():
            sz += 1
        if self._right:
            sz += self._right.size()
        return sz

    def insert(self, x):
        if self.isEmpty():
            self.setData(x)
        elif x < self.getData():
            if self._left:
                self._left.insert(x)
            else:
                self._left = BinarySearchTree(x)
        else:
            if self._right:
                self._right.insert(x)
            else:
                self._right = BinarySearchTree(x)
    
    def printStructure(self):
        thislevel = [self]
        a = '                                 '
        while thislevel: 
            string = "" 
            nextlevel = [] 
            l =  int(len(a)/ 2)
            a = a[:l]
            childs = 0
            for n in thislevel: 
                if childs == 0 and n.getData() > self.getData():
                    string += " " * 10
                    childs +=1
                string += a +str(n.getData())
                childs += 1
                #print(a + str(n.getData())),
                if n._left: 
                    nextlevel.append(n._left)
                
                if n._right: 
                    nextlevel.append(n._right)
                thislevel = nextlevel  
            print(string)
               
        return
        
    def search(self, key):
        if self is None or self.getData() == key: 
            return self.getData()
        
        if self.getData() < key :
            return self._right.search(key)
        return self._left.search(key)
        
    def delete(self, x, parent = None):
        if x < self.getData() : # sök till vänster
            self._left = self._left.delete(x, self)
        elif x > self.getData(): 
            self._right = self._right.delete(x, self)
        else: # hittat 
            #hantera 0 barn 1 barn, 2 barn 
            if parent == None: 
                self.setData(None) 
            elif not self._left: 
                return self._right 
            elif not self._right: 
                return self._left 
            else: #två barn 
                (psucc, succ) = self._right._findMin(self)
            succ.left = self._left 
            succ.right = self._right 
        return self
    
    def _findMin(self, parent):
        if self._left: 
            return self._left._findMin(self._left, self)
        else: 
            return (parent, self)
            
                