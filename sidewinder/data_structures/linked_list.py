#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

# https://www.youtube.com/watch?v=FSsriWQ0qYE


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


linked_list = LinkedList()
linked_list.append('A')
linked_list.append('B')
linked_list.append('C')
linked_list.print_list()

