#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    """ Definition for singly-linked list. """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    head = ListNode(0)
    curr = head
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return head.next

