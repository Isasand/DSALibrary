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
 
    def add(self, data):
        newNode = Node(data)
        if self._head is None:
            self._head = self._tail = newNode
        else:
            newNode._prev = self._tail
            newNode._next = None
            self._tail._next = newNode
            self._tail = newNode
 
    def remove(self, node_value):
        current = self._head
 
        while current is not None:
            if current._data == node_value:
                # if it's not the first element
                if current._prev is not None:
                    current._prev._next = current.getNext()
                    current._next._prev = current.getPrev()
                else:
                    # otherwise we have no prev (it's None),
                    #head is the next one, and prev becomes None
                    self._head = current._next
                    current._next._prev = None
 
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
 
 