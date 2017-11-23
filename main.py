# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 11:16:23 2017

@author: Isa
"""

import unittest
from Linkedlist import Linkedlist
from DoublyLinkedlist import DoubleLinkedlist

class TestLinkedlist(unittest.TestCase):
    def test_Linkedlist_toList(self):
        L = Linkedlist()
        L.add(22, 23)
        
        self.assertEqual(L.toList(), [23, 22] )
    
    def test_Linkedlist_size(self):
        L = Linkedlist()
        L.add(22, 23)
        
        self.assertEqual(L.size(), 2 )
    
    def test_Linkedlist_remove(self):
        L = Linkedlist()
        L.add(22, 23, 25, 26, 27, 28)
        L.remove(22)
        self.assertEqual(L.toList(), [28, 27, 26, 25, 23] )
    
    def test_Linkedlist_search(self):
        L = Linkedlist()
        L.add(22, 23)
        self.assertEqual(L.search(23).getData(), 23 )

    def test_Linkedlist_show(self):
        L = Linkedlist()
        L.add(5, 6, 50, 30)
        #L.show()
        L.remove(50)
        L.remove(5)
        #L.show()
        
    def test_Linkedlist_reversed(self):
        L = Linkedlist()
        L.add(5, 6, 50, 30)
        L.reverse(L.getHead())
        self.assertEqual(L.toList(), [5, 6, 50, 30] )
    
    def test_Linkedlist_fromlist(self):
        l = [1, 2, 3, 4, 5]
        L = Linkedlist()
        L.fromList(l)
        self.assertEqual(L.toList(), [5,4,3,2,1] )
        
        
class TestDoublyLinkedlist(unittest.TestCase):
    def test_doublyLinkedlist(self):
        L = DoubleLinkedlist()
        L.insertFirst(5)
        L.insertFirst(6)
        L.insertFirst(30)
        L.insertFirst(50)
        L.show()
        #L.remove(50)
        #L.remove(5)
        #L.show()
        P = DoubleLinkedlist()
        P.insertLast(5)
        P.insertLast(6)
        P.insertLast(30)
        P.insertLast(50)
        P.show()
    
if __name__ == '__main__':
    unittest.main(verbosity=2) 
    
    
    
    
    
    
    
    