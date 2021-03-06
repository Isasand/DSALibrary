# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 11:00:05 2017

@author: Isa
"""
#for the single linked list we dont use the prev member of the nodes

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
        self._prev = argPrev
    
    def displayData(self): 
        print(self._data)
        
class Linkedlist(object):
    def __init__(self):
        self._head = None 
        self._size = 0 
        
    def isEmpty(self):
        return self.getHead() == None
       #could also return self._size == 0
    
    def getHead(self):
        return self._head
    
    def setHead(self, h):
        self._head = h
        
    #takes one or more arguments
    def add(self, data, *mult):
        newnode = Node(data)
        newnode.setNext(self.getHead())
        self.setHead(newnode)
        self._size += 1
        
        if mult: 
            if len(mult) == 1: 
                if not mult[0] == None:
                    self.add(mult[0])
                return
            self.add(mult[0])
            self.fromList(list(mult[1:]))
         
    #add from list 
    def fromList(self, l):
        if len(l) == 1:
            if not l[0] == None: 
                return self.add(l[0])
        self.add(l[0])
        self.fromList(l[1:])
        
    def insert(self, data, after_node):
        newnode = Node(data)
        after_node = self.search(after_node)
        newnode.setNext(after_node.getNext())
        after_node.setNext(newnode)

    def search(self, searchData):
        current = self._head 
        while not current == None:
            if current.getData() == searchData:
                return current 
            current = current.getNext()
        return None
         
    def search_byIndex(self, index):
        if not index > self._size :
            current = self.getHead()
            for i in range(0, index):
                current = current.getNext()
            return current 
        
    def remove(self, node): #remove by value
        current = self.getHead()
        
        if self.search(node) is self.getHead():
            self.setHead(self.getHead().getNext())
            return
        
        while current is not None:
            #if it is the tail we need to find the previous one
            if current._next == None: 
                self.search_byIndex(self.size()-2)._next = None
                self._size -= 1
                return 
                
            elif current.getNext().getData() == node: 
                
                current.setNext(current.getNext().getNext())
                self._size -= 1
                return
            current = current.getNext() 
        return
     
    def printList(self):
        print(str(self.toList()))
    
    #pass the self._head as node here
    def reverse(self, node):
        if node.getNext() == None:
            self._head = node
            return 
        self.reverse(node.getNext())
        temp = node.getNext()
        temp.setNext(node)
        node.setNext(None)
        
        
    def show(self):
        print("SINGLE LINKED LIST\n(First -> Last)")
        current = self._head
        print("Head: " + str(current.getData()) )
        current = current.getNext()
        while current is not None:
           
            print (" "*6+str(current.getData())),
            print (current.getNext().getData()) if hasattr(current.getNext(), "data") else None
 
            current = current.getNext()
        print ("*"*10)
 
    
    def toList(self):
        l = []
        current = self._head
        while not current == None:
            l.append(current.getData())
            current = current.getNext()
        return l
    
    def size(self):
        return self._size
    