# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 10:52:26 2017

@author: Isa
"""

class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self): 
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop() 
    
    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)