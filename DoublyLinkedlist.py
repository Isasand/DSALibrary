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
 
    
    def getTail(self):
        return self._tail 
    
    def setTail(self, t):
        self._tail = t
        
    def getHead(self):
        return self._head 
    
    def setHead(self, h):
        self._head = h
        
    def insertFirst(self, data):
        newNode = Node(data)
        
        if self.isEmpty():
            self.setTail(newNode)
        else:
            self.getHead().setPrev(newNode)
            newNode.setNext(self._head)
        self.setHead(newNode)
 
    def insertLast(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self._head = self._tail = newNode
        else:
            newNode.setNext(None)
            newNode.setPrev(self.getTail())
            self.getTail().setNext(newNode)
            self.setTail(newNode)
        
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
            if current.getData() == node_value:
                # if it's not the first element
                if current.getNext() == None: 
                    current.getPrev().setNext(None)
                    return 
                
                if not current._prev == None:
                    current.getPrev().setNext(current.getNext())
                    current.getNext().setPrev(current.getPrev())
                
                if current is self._head: 
                    self._head._next._prev = None
                    self.setHead(self.getHead().getNext())
                    return
 
            current = current._next
 
    def show(self):
        print("Show list data:")
        current = self.getHead()
        while current is not None:
            print (current.getPrev().getData()) if hasattr(current.getPrev(), "data") else None,
            print (current.getData()),
            print (current.getNext().getData()) if hasattr(current.getNext(), "data") else None
 
            current = current.getNext()
        print ("*"*50)
 
 