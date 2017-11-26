# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 11:16:23 2017

@author: Isa
"""

import unittest
from Linkedlist import Linkedlist
from DoublyLinkedlist import DoubleLinkedlist
from BinarySearchTree import BinarySearchTree 


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
        #we can remove both tail and head here
        L = Linkedlist()
        L.add(22, 23, 25, 26, 27, 28)
        L.remove(22)
        self.assertEqual(L.toList(), [28, 27, 26, 25, 23] )
    
    def test_Linkedlist_search(self):
        L = Linkedlist()
        L.add(22, 23)
        self.assertEqual(L.search(23).getData(), 23 )

    def test_Linkedlist_reversed(self):
        L = Linkedlist()
        L.add(5, 6, 50, 30)
        L.reverse(L.getHead())
        self.assertEqual(L.toList(), [5, 6, 50, 30] )
    
    def test_Linkedlist_fromlist(self):
        l = [1, 2, 3, 4, 5]
        L = Linkedlist()
        L.fromList(l)
        self.assertEqual(L.toList(), [5, 4, 3, 2, 1] )
        
    def test_Linkedlist_insert(self):
        l = Linkedlist()
        l.add(22, 24, 25)
        l.insert(20, 22)
        self.assertEqual(l.toList(), [25, 24, 22, 20])
        
    
    def test_Linkedlist_show(self):
        L = Linkedlist()
        L.add(1, 2, 3, 4)
        L.show()
        
class TestDoublyLinkedlist(unittest.TestCase):
    
    def test_doublyLinkedlist_insert_first(self):
        L = DoubleLinkedlist()
        L.insertFirst(5, 6, 30, 50, 60, 3)
        L.show()
        self.assertEqual(L.toList(), [3, 60, 50, 30, 6, 5] )
      
    def test_doublyLinkedlist_insert_last(self):
        
        P = DoubleLinkedlist()
        P.insertLast(5)
        P.insertLast(6)
        P.insertLast(30)
        P.insertLast(50)
        
        self.assertEqual(P.toList(), [5, 6, 30, 50] )
    
    def test_doublyLinkedlist_remove(self):
        #we remove both the head and the tail here to see that it works
        L = DoubleLinkedlist()
        L.insertFirst(6, 5, 30, 50)
        L.remove(6)
        L.remove(50)
        self.assertEqual(L.toList(), [30,5])
    
    def test_doublyLinkedList_search_byValue(self):
        L = DoubleLinkedlist()
        L.insertFirst(6, 5, 30, 50)
        self.assertEqual(L.search(50).getData(), 50)
        
    def test_doublyLinkedList_search_backwards(self):
        L = DoubleLinkedlist()
        L.insertFirst(1, 2, 3, 4, 5)
        self.assertEqual(L.search_by_index(4).getData(), 4)
        
    def test_doublyLinkedlist_search_forwards(self):
        L = DoubleLinkedlist()
        L.insertFirst(1, 2, 3, 4, 5)
        self.assertEqual(L.search_by_index(2).getData(), 2)
    
    def test_doublyLinkedlist_fromList(self):
        l = [1,2,3,4]
        L= DoubleLinkedlist() 
        L.fromList(l)
        self.assertEqual(L.toList(), [4, 3, 2, 1])
        
class testBinarySearchTree(unittest.TestCase):
    
    def test_binarySearchTree_insert(self):
        tree = BinarySearchTree(10)
        tree.insert(20, 0)
        self.assertEqual(tree.search(20), 20)
        
    def test_binarySearchTree_size(self):
        #obviously the size starts at 0 and you will get the size - 1 out of the size function 
        #i will rewrite it 
        tree = BinarySearchTree(10)
        tree.insert(20, 0)
        self.assertEqual(tree.size(), 2)
    
    def test_binarySearchTree_printHierarchy(self):
        tree = BinarySearchTree(10)
        tree.insert(20, 0, 100, 50, 30, 7, 2, 3, 1, 9, 6, 60, 110, 17)
        tree.printHierarchy()
    
    def test_binaryTree_toList(self):
        tree = BinarySearchTree(10)
        tree.insert(20, 0, 100, 50)
        self.assertEqual(tree.toList(), [10, 0, 20, 100, 50])
        
        
    def test_delete_leaf(self):
        tree = BinarySearchTree(10)
        self.assertEqual(tree.delete(10).getData(), None)
        
    def test_delete_one_child(self):
        tree = BinarySearchTree(10)
        tree.insert(20)
        self.assertEqual(tree.delete(10).getData(), None)
        
    def test_delete_two_childs(self):
        tree = BinarySearchTree(10)
        tree.insert(20, 0, 100, 50, 30, 17)
        print("\ntest tree")
        tree.printHierarchy()
        print("\nDepth")
        print(tree.getDepth())
        tree.delete(20)
        print("\nremoved node with data == 20")
        tree.printHierarchy()
        
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2) 
    
    
    
    
    
    
    
    