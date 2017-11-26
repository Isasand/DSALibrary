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

    def insert(self, x, *moredata):
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
        if moredata: 
            if len(moredata) == 1: 
                self.insert(moredata[0])
                return
            self.insert(moredata[0])
            self.fromList(list(moredata[1:]))
            
    def fromList(self, l):
        if len(l) == 1:
            self.insert(l[0])
        else: 
            self.insert(l[0])
            self.fromList(l[1:])
        
            
    def printHierarchy(self):
        thislevel = [self]
        while thislevel: 
            string = "" 
            nextlevel = [] 
            for n in thislevel: 
                string += str(n.getData()) + " " 
                if n._left: 
                    nextlevel.append(n._left)
                if n._right: 
                    nextlevel.append(n._right)
                thislevel = nextlevel  
            print(string)
        return
        
    def toList(self):
        root = [self] 
        l = []
        while root:
            nextLevel= []
            for node in root: 
                l.append(node.getData())
                if node._left: 
                    nextLevel.append(node._left)
                if node._right: 
                    nextLevel.append(node._right)
                root = nextLevel
        return l 
        
    def getDepth(self): 
        root = [self]
        depth = 0
        while root: 
            nextLevel = []
            for node in root: 
                if node._left:
                    nextLevel.append(node._left)
                if node._right: 
                    nextLevel.append(node._right) 
                root = nextLevel
            depth += 1
        return depth 
            
            
    #TODO: fix this function ( the right childs )
    def printStructure(self):
        thislevel = [self]
        a = '                                 '
        while thislevel: 
            string = "" 
            nextlevel = [] 
            l =  int(len(a)/ 2)
            a = a[:l]
            for n in thislevel: 
                if n.getData() > self.getData():
                    string += " " *7
                string += a +str(n.getData())
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
    
    def delete(self, x, parent=None ):
        if x < self.getData():
            self._left = self._left.delete( x, self )
        elif x > self.getData():
            self._right = self._right.delete( x, self )
        else:
            # x == self.data - ta bort
            if parent==None:
                self.setData( None )
            elif not self._left:
                return self._right
            elif not self._right:
                return self._left
            else:
                (psucc, succ) = self._right._findMin( self )
                if psucc._left == succ:
                    psucc._left = succ._right
                else:
                    psucc._right = succ._right
                succ._left = self._left
                succ._right = self._right
                return succ
        return self

    
    def _findMin(self, parent):
        if self._left: 
            return self._left._findMin(self)
        else: 
            return (parent, self)
            
                