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
        self._size = 0
    
    def getSize(self):
        return self._size
    
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
            self._size += 1
        else:
            self.getHead().setPrev(newNode)
            newNode.setNext(self._head)
            self._size += 1
        self.setHead(newNode)
        
        
    def insertLast(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self._head = self._tail = newNode
            self._size += 1 
        else:
            newNode.setNext(None)
            newNode.setPrev(self.getTail())
            self.getTail().setNext(newNode)
            self.setTail(newNode)
            self._size += 1 
            
    #i allways insert lists
    def fromList(self, l):
        if len(l)== 1: 
            self.insertFirst(l[0])
        else:
            self.insertFirst(l[0])
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
    
    def search_by_index(self, index):
        #if index is bigger than size/ 2 of list, then we search backwards
        #otherwise forwards
        if not index > self._size: 
            if index <  self._size / 2 :
                index +=1
                current = self.getHead()
                for i in range(0, index):
                    current = current.getNext() 
                return current
            elif index > self._size / 2:
                index -=1
                current= self.getTail() 
                for i in range(0, index):
                    current = current.getPrev()
                return current
        return
        
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
                    self._size -= 1 
                    return 
                
                if not current.getPrev() == None:
                    current.getPrev().setNext(current.getNext())
                    current.getNext().setPrev(current.getPrev())
                
                if current is self._head: 
                    self._head._next._prev = None
                    self.setHead(self.getHead().getNext())
                    self._size -= 1 
                    return
 
            current = current._next
 
    def show(self):
        print("Show list data:")
        current = self.getHead()
        print("Head: " + str(current.getData()) )
        current = current.getNext()
        
        while current is not None:
            if current == self.getTail(): 
                print("Tail: " + str(current.getData()))
                print ("*"*50)
                return
            
            print (current.getPrev().getData()) if hasattr(current.getPrev(), "data") else None,
            print (" "*6+str(current.getData())),
            print (current.getNext().getData()) if hasattr(current.getNext(), "data") else None
            
            current = current.getNext()
        
 
 