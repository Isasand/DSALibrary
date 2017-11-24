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
    
    def pre_order_walk(self, root):
        print(self.getData())
        if root._left:
            self.pre_order_walk(root._left)
        self.pre_order_walk(root._right)