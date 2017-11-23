# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 11:16:23 2017

@author: Isa
"""

import unittest
from Linkedlist import Linkedlist
from Linkedlist import Node
from DoublyLinkedlist import DoubleLinkedlist

class TestLinkedlist(unittest.TestCase):
    def test_Linkedlist_toList(self):
        L = Linkedlist()
        L.add(22)
        L.add(23)
        L.printList() # this prints the list as a string 
        
        self.assertEqual(L.toList(), [23, 22] )
    
    def test_Linkedlist_size(self):
        L = Linkedlist()
        L.add(22)
        L.add(23)
        
        self.assertEqual(L.size(), 2 )
    
    def test_Linkedlist_remove(self):
        L = Linkedlist()
        L.add(22)
        L.add(23)
        L.add(25)
        L.remove(22)
        self.assertEqual(L.toList(), [25, 23] )
    
    def test_Linkedlist_search(self):
        pass

    def test_Linkedlist_show(self):
        L = Linkedlist()
        L.add(5)
        L.add(6)
        L.add(50)
        L.add(30)
        L.show()
        L.remove(50)
        L.remove(5)
        L.show()
        
        
class TestDoublyLinkedlist(unittest.TestCase):
    def test_doublyLinkedlist(self):
        L = DoubleLinkedlist()
        L.add(5)
        L.add(6)
        L.add(50)
        L.add(30)
        L.show()
        L.remove(50)
        L.remove(5)
        L.show()
    
if __name__ == '__main__':
    unittest.main(verbosity=2) 
    
    
    
    
    
    
    
    