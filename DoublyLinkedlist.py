# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 12:20:53 2017

@author: Isa
"""

from Linkedlist import Node

class DoubleLinkedlist(object):
    def __init__(self):
        self._head = None
        self._tail = None
 
    def insertFirst(self, data):
        newNode = Node(data)
        
        if self.isEmpty():
            self._tail = newNode
        else:
            self._head._prev = newNode
            newNode._next = self._head
        self._head = newNode
 
    def insertLast(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self._head = self._tail = newNode
        else:
            newNode._next = None
            newNode._prev = self._tail
            self._tail._next = newNode
            self._tail = newNode
        
    def fromList(self, l):
        if len(l) == 1:
            if not l[0] == None: 
                return self.add(l[0])
        self.add(l[0])
        self.fromList(l[1:])
    
    def toList(self):
        l = []
        current = self._head
        while not current == None:
            l.append(current.getData())
            current = current.getNext()
        return l
    
    
    def isEmpty(self):
        return self._head == None
    
    def search(self, searchData):
        current = self._head 
        while not current == None:
            if current.getData() == searchData:
                return current 
            current = current.getNext()
        return None
    
    def remove(self, node_value):
        current = self.search(node_value)
 
        while current is not None:
            if current._data == node_value:
                # if it's not the first element
                if current._next == None: 
                    current._prev._next = None
                    return 
                
                if not current._prev == None:
                    current._prev._next = current.getNext()
                    current._next._prev = current.getPrev()
                
                if current is self._head: 
                    self._head._next._prev = None
                    self._head = self._head._next
                    return
 
            current = current._next
 
    def show(self):
        print("Show list data:")
        current = self._head
        while current is not None:
            print (current.getPrev().getData()) if hasattr(current.getPrev(), "data") else None,
            print (current.getData()),
            print (current.getNext().getData()) if hasattr(current.getNext(), "data") else None
 
            current = current.getNext()
        print ("*"*50)
 
 