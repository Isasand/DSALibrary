# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 11:00:05 2017

@author: Isa
"""

class Node(object):
    def __init__(self, data):
        self._data = data
        self._next = None
        self._prev = None
        
    def getData(self):
        return self._data
    
    def setData(self, argData):
        self._data = argData
        
    def getNext(self):
        return self._next
    
    def setNext(self, argNext):
        self._next = argNext
        
    def getPrev(self):
        return self._prev
    
    def setPrev(self, argPrev):
        self._prev = ArgPrev
        
class Linkedlist(object):
    def __init__(self):
        self._head = None 
        self._size = 0 
        
    def isEmpty(self):
        return self._head == None
       #could also return self._size == 0
    
    def add(self, data):
        newnode = Node(data)
        newnode.setNext(self._head)
        self._head = newnode
        self._size += 1

    def insert(self, data, after_node):
        newnode = Node(data)
        newnode.setNext(after_node.getNext())
        after_node.setNext(newnode)

    def search(self, searchData):
        current = self._head 
        while not current == None:
            if current.getData() == searchData:
                return current 
            current = current.getNext()
        return None
            
    def remove(self, node): #remove by value
        current = self._head 
        while not current == None:
            if current.getNext().getData() == node: 
                current.setNext(current.getNext().getNext())
                self._size -= 1
                return self
            current = current.getNext() 
        return
     
    def printList(self):
        print(str(self.toList()))
    
    def show(self):
        print("show list data:")
        current = self._head
        while current is not None:
            print (current.getData()),
            print (current.getNext().getData()) if hasattr(current.getNext(), "data") else None
 
            current = current.getNext()
        print ("*"*50)
 
    
    def toList(self):
        l = []
        current = self._head
        while not current == None:
            l.append(current.getData())
            current = current.getNext()
        return l
    
    def size(self):
        return self._size
    