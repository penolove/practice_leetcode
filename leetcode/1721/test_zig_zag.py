import unittest
import logging
import timeit
from collections import deque


LOG = logging.getLogger(__name__)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TestSwapNodesInLinkList(unittest.TestCase):
    """
    https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
    Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
    Output: [7,9,6,6,8,7,3,0,9,5]
    """

    def form_list_node_from_List(self, x: list) -> ListNode:
        first = None
        prev = None
        now = None
        for i in x:
            now = ListNode(i)
            if prev is not None:
                prev.next = now
            else:
                first = now
            prev = now
        return first

    def list_node_to_list(self, obj):
        result = [obj.val]
        while obj.next is not None:
            obj = obj.next
            result.append(obj.val)
        return result

    def test_forming_task(self):
        obj = self.form_list_node_from_List([7, 9, 6, 6, 7, 8, 3, 0, 9, 5])

        result = self.list_node_to_list(obj)
        self.assertListEqual(result, [7, 9, 6, 6, 7, 8, 3, 0, 9, 5])

    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        end_list = deque([head])
        src_node = head

        count = 1
        iter_cursor = head
        while iter_cursor.next is not None:
            count += 1
            iter_cursor = iter_cursor.next

            if count == k:
                src_node = iter_cursor
                print(src_node.val)

            end_list.append(iter_cursor)
            if len(end_list) > k:
                end_list.popleft()

        end_node = end_list.popleft()

        tmp = src_node.val
        src_node.val = end_node.val
        end_node.val = tmp

        return head

    def test_1(self):
        obj = self.form_list_node_from_List([1, 2, 3, 4, 5])

        result = self.list_node_to_list(self.swapNodes(obj, 2))
        self.assertListEqual(result, [1, 4, 3, 2, 5])


    def test_2(self):
        obj = self.form_list_node_from_List([1])

        result = self.list_node_to_list(self.swapNodes(obj, 1))
        self.assertListEqual(result, [1])

    def test_3(self):
        obj = self.form_list_node_from_List([100, 90])

        result = self.list_node_to_list(self.swapNodes(obj, 2))
        self.assertListEqual(result, [90, 100])
