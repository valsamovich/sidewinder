#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

# Source: https://youtu.be/6oL-0TdVy28


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(self.root, '')
        else:
            print('Traversal type ' + str(traversal_type) + ' is not supported')
            return False

    def preorder_print(self, start, traversal):
        """ Root -> Left -> Right """
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

# Tree representation:
#          1
#        /   \
#       2     3
#      / \   / \
#     4   5 6   7


# Tree setup:
binary_tree = BinaryTree(1)
binary_tree.left = Node(2)
binary_tree.right = Node(3)
binary_tree.left.left = Node(4)
binary_tree.left.right = Node(5)
binary_tree.right.left = Node(6)
binary_tree.right.right = Node(7)

print(binary_tree.print_tree('preorder'))
