# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 10:26:40 2017

@author: Isa
"""


import unittest
from Linkedlist import Linkedlist
from DoublyLinkedlist import DoubleLinkedlist
from BinarySearchTree import BinarySearchTree 
from DoubleEndedLinkedlist import DoubleEndedLinkedlist
from graph import Graph

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
    
class TestDoubleEndedLinkedlist(unittest.TestCase): 
    
    def test_insert_last(self): 
        l = DoubleEndedLinkedlist()
        l.insertLast(2)
        l.insertLast(3)
        l.printList() 
        self.assertEqual(l.toList(), [2, 3])

    def test_insert_first(self):
        l = DoubleEndedLinkedlist() 
        l.insertFirst(1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(l.toList(), [7, 6, 5, 4, 3, 2, 1])
    
class TestBinarySearchTree(unittest.TestCase):
    
    def test_binarySearchTree_insert(self):
        tree = BinarySearchTree(10)
        tree.insert(20, 0)
        self.assertEqual(tree.search(20), 20)
        
    def test_binarySearchTree_size(self):
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
        tree.insert(20)
        tree.deleteNode(tree,20)
        self.assertEqual(tree.toList(), [10])
        
    def test_delete_one_child(self):
        tree = BinarySearchTree(10)
        tree.insert(20)
        tree.insert(17)
        tree.insert(11)
        tree.insert(19)
        tree.deleteNode(tree, 19)
        self.assertEqual(tree.toList(), [10,20, 17, 11])
        
    def test_delete_two_childs(self):
        tree = BinarySearchTree(10)
        tree.insert(20, 0, 100, 50, 30, 17)
        print("\ntest tree")
        tree.printHierarchy()
        print("\nDepth")
        print(tree.getDepth())
        tree.deleteNode(tree,20)
        print("\nremoved node with data == 20")
        tree.printHierarchy()
        
class TestGraph(unittest.TestCase): 
    
    def testIsEmpty(self):
        graph = Graph() 
        self.assertEqual(graph.isEmpty(), True)
        
    def testAddVertex(self):
        graph = Graph()
        graph.addVertex("Stockholm")
        graph.addVertex("Göteborg")
        graph.addEdge("Stockholm", "Göteborg")
        self.assertEqual(graph.areNeighbours("Stockholm", "Göteborg"), True)
        
    def testDFSPath(self):
        graph = Graph()
        graph.addVertex("A")
        graph.addVertex("B")
        graph.addVertex("D")
        graph.addEdge("A", "B")
        graph.addEdge("B", "C")
        graph.addVertex("D")
        graph.addEdge("D", "B", weight = 6)
        graph.addEdge("D", "C")
        self.assertEqual(graph.findDFSPath("A", "D"), ['A', 'B', 'D'])
        
    def testTrainProblem(self):
        trainConnections =  Graph()
        trainConnections.addVertex("Stockholm")
        trainConnections.addVertex("Göteborg" )
        trainConnections.addVertex("Linköping")
        trainConnections.addEdge("Stockholm", "Göteborg", weight = 150)
        trainConnections.addEdge("Stockholm", "Linköping", weight = 50)
        trainConnections.addEdge("Linköping", "Göteborg", weight = 50)
        self.assertEqual(trainConnections.findAllPaths("Stockholm", "Göteborg"), [['Stockholm', 'Linköping', 'Göteborg'], ['Stockholm', 'Göteborg']])
        self.assertEqual(trainConnections.findShortestPath("Stockholm", "Göteborg"), ['Stockholm', 'Göteborg'])
        