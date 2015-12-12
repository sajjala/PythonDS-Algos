import unittest

from linked_list import LinkedList

#To run: 'python -m unittest test_linked_list'

class TestLinkedList(unittest.TestCase):
    """ Test Behaviro """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add_at_head(self):
        ml = LinkedList()
        ml.addAtHead(1)
        ml.addAtHead(2)
        ml.addAtHead(3)
        ml.addAtHead(4)
        ml.addAtHead(5)
        
        self.assertEqual(ml.getItems(),[5,4,3,2,1])

    def test_add_in_order(self):
        ml = LinkedList()
        ml.addInOrder(1)
        ml.addInOrder(2)
        ml.addInOrder(3)
        ml.addInOrder(4)
        ml.addInOrder(5)
        
        self.assertEqual(ml.getItems(),[1,2,3,4,5])

    def test_reverse_list_iterative(self):
        ml = LinkedList()
        ml.addAtHead(1)
        ml.addAtHead(2)
        ml.addAtHead(3)
        ml.addAtHead(4)
        ml.addAtHead(5)
        
        self.assertEqual(ml.getItems(),[5,4,3,2,1])
        ml.head = ml.reverseListIterative()
        self.assertEqual(ml.getItems(),[1,2,3,4,5])

        ml.head = ml.reverseListIterative()
        self.assertEqual(ml.getItems(),[5,4,3,2,1])

        ml.head = ml.reverseListIterative()
        self.assertEqual(ml.getItems(),[1,2,3,4,5])


        ml = LinkedList()
        ml.addInOrder(1)
        ml.addInOrder(2)
        ml.addInOrder(3)
        ml.addInOrder(4)
        ml.addInOrder(5)
        
        ml.head = ml.reverseListIterative()
        self.assertEqual(ml.getItems(),[5,4,3,2,1])

        ml.head = ml.reverseListIterative()
        self.assertEqual(ml.getItems(),[1,2,3,4,5])

        ml.head = ml.reverseListIterative()
        self.assertEqual(ml.getItems(),[5,4,3,2,1])

        ml.head = ml.reverseListIterative()
        self.assertEqual(ml.getItems(),[1,2,3,4,5])
