# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 14:28:41 2017

@author: Isa
"""

class Queue :
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item): 
        self.items.insert(0, item)
        
    def dequeue(self):
        return self.items.pop() 
    
    def size(self):
        return len(self.items)