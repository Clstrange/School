from math import isclose
import string
from main import Pair
class Node:
    '''Contains letter and number pair along with two links
    for the Binary Search Tree'''
    def __init__(self, item):
        self.left_link = None
        self.right_link = None
        self.data = Pair(item) # letter and number pair
class BST:
    '''Binary Search Tree, linked structure that will be
    used to count the amount of each alphebtic letter in a text'''
    def __init__(self):
        '''Constructor for the BST class'''
        self.root = None # root of tree
        self.leaf = None
        self.p1 = None # pointer one
        self.p2 = None #pointer two
        self.search = None
        self.test = 1
        self.tree_size = 0

    def add(self, item):
        '''Adds a new item to the tree'''
        self.leaf = Node(item)
        if self.root == None:
            self.root = self.leaf
        else:
            self.p1 = self.root
            def recursion():
                if self.leaf.data.letter < self.p1.data.letter:
                    if self.p1.left_link is None:
                        self.p1.left_link = self.leaf
                    else:
                        self.p1 = self.p1.left_link
                        recursion()
                elif self.leaf.data.letter > self.p1.data.letter:
                    if self.p1.right_link is None:
                        self.p1.right_link = self.leaf
                    else:
                        self.p1 = self.p1.right_link
                        recursion()
                else:
                    self.p1.data.count += 1
            recursion()

    def is_empty(self):
        '''Returns True if list is empty and False otherwise'''
        if self.root is None:
            return True
        return False

    def height(self):
        def recursion(leaf):
            if leaf is None:
                return 0
            return 1 + max(recursion(leaf.left_link), recursion(leaf.right_link))
        return recursion(self.root)

    def size(self):
        return len(self.inorder())

    def remove(self, item):
        self.p1 = self.root #lead pointer
        self.p2 = self.p1 #follows p1
        tree_p3 = None #lead pointer
        tree_p4 = None #follows p3
        #locating item to remove
        def recursion(item):
            if item < self.p1.data:
                self.p2 = self.p1
                self.p1 = self.p1.left_link
                recursion(item)
            elif item > self.p1.data:
                self.p2 = self.p1
                self.p1 = self.p1.right_link
                recursion(item)
        recursion(item)
        #Item not located
        if item != self.p1.data:
            return
        #Item has two-children
        if (self.p1.right_link is not None and
        self.p1.left_link is not None):
            tree_p3 = self.p1.right_link
            tree_p4 = tree_p3
            while tree_p3.left_link is not None:
                tree_p4 = tree_p3
                tree_p3 = tree_p3.left_link
            #setting a new parent node
            tree_p4.left_link = None
            tree_p3.right_link = self.p1.right_link
            tree_p3.left_link = self.p1.left_link
        if self.p1 == self.root:
            self.root = tree_p3
            #deleting item
            if self.p1.data.letter < self.p2.data.letter: #left-side
                self.p2.left_link = tree_p3
                self.p1.left_link = None
                self.p1.right_link = None
            else: #right-side
                self.p2.right_link = tree_p3
                self.p1.right_link = None
                self.p1.left_link = None
        #Item has no-children
        elif self.p1.left_link is None and self.p1.right_link is None:
            print(self.p2.data.letter)
            if self.p1.data.letter < self.p2.data.letter: #left-side
                self.p2.left_link = None
            else: #right-side
                self.p2.right_link = None
        #Item has one-child
        else:
            if self.p1.data.letter < self.p2.data.letter: #left-side
                if self.p1.right_link is None:
                    self.p2.left_link = self.p1.left_link
                else:
                    self.p2.left_link = self.p1.right_link
            else:
                if self.p1.right_link is None:
                    self.p2.right_link = self.p1.left_link
                else:
                    self.p2.right_link = self.p1.right_link

    def find(self, item):
        if not isinstance(item, str):
            raise ValueError

        self.p1 = self.root
        def recursion(item):
            if self.p1 is None:
                self.search = False
                return
            if item != self.p1.data.letter:
                if item < self.p1.data.letter:
                    self.p1 = self.p1.left_link
                    recursion(item)
                elif item > self.p1.data.letter:
                    self.p1 = self.p1.right_link
                    recursion(item)
            else:
                if item == self.p1.data.letter:
                    self.search = True
                else:
                    self.search = False

        recursion(item)
        return self.search

    def inorder(self):
        self.p1 = self.root
        balance_lyst = []
        def recursion(next):
            if next is None:
                return
            else:
                recursion(next.left_link)
                balance_lyst.append(next.data)
                recursion(next.right_link)
        recursion(self.p1)
        return balance_lyst

    def preorder(self):
        balance_lyst = []
        self.p1 = self.root
        def recursion(next):
            if next is None:
                return
            else:
                balance_lyst.append(next.data)
                recursion(next.left_link)
                recursion(next.right_link)
        recursion(self.p1)
        return balance_lyst

    def postorder(self):
        self.p1 = self.root
        balance_lyst = []
        def recursion(next):
            if next is None:
                return
            else:
                recursion(next.left_link)
                if next.right_link is not None:
                    recursion(next.right_link)
                balance_lyst.append(next.data)
        recursion(self.p1)
        return balance_lyst

    def rebalance(self):
        balance_lyst = self.inorder()
        self.root = None
        def recursion(balance_lyst):
            mid = len(balance_lyst) // 2
            lower_half = balance_lyst[:mid]
            upper_half = balance_lyst[mid:]
            self.add(balance_lyst[mid])
            if len(balance_lyst) == 1:
                self.add(balance_lyst[mid])

            else:
                recursion(lower_half)
                recursion(upper_half)
        recursion(balance_lyst)
