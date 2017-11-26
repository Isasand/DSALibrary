# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 14:56:15 2017

@author: Isa
"""

from Linkedlist import Node

class DoubleEndedLinkedlist(object):
    def __init__(self):
        self._head = None
        self._tail = None
    
    def insertFirst(self, data, *moreData):
        newNode = Node(data)
        if self.isEmpty():
            self._tail = newNode
        else: 
            newNode.setNext(self._head)
        self._head = newNode 
        
        
        if moreData: 
            if len(moreData) == 1: 
                self.insertFirst(moreData[0]) 
                return 
            else: 
                self.insertFirst(moreData[0])
                self.fromList(list(moreData[1:]))
        
         
    def isEmpty(self):
        return self._head == None
        
    def insertLast(self, data):
        newNode = Node(data) 
        if self.isEmpty(): 
            self._head = newNode 
        else: 
            self._tail.setNext(newNode)
        self._tail = newNode
                       
    def printList(self):
        print("\nDOUBLE ENDED LINKED LIST\n(FIRST --> LAST):")
        current = self._head 
        
        while not current == None: 
            current.displayData() 
            current = current.getNext()
            
    def toList(self): 
        current = self._head 
        l = []
        while not current == None: 
            l.append(current.getData())
            current = current.getNext() 
        return l 
    
    #i allways insert lists from front
    def fromList(self, l): 
        if len(l) == 1: 
            self.insertFirst(l[0])
        else: 
            self.insertFirst(l[0])
            self.fromList(l[1:])
            