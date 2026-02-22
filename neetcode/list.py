from __future__ import annotations

import doctest
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, lst: list[int]) -> Optional[ListNode]:
        dummy = cls()
        ptr = dummy
        for val in lst:
            ptr.next = cls(val)
            ptr = ptr.next
        return dummy.next

    @classmethod
    def to_list(cls, head: Optional[ListNode]) -> list[int]:
        res: list[int] = []
        while head:
            res.append(head.val)
            head = head.next
        return res


# https://leetcode.com/problems/reverse-linked-list
def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    >>> ListNode.to_list(reverse_list(ListNode.from_list([1,2,3,4,5])))
    [5, 4, 3, 2, 1]
    >>> ListNode.to_list(reverse_list(ListNode.from_list([1,2])))
    [2, 1]
    >>> ListNode.to_list(reverse_list(ListNode.from_list([])))
    []
    """
    prev: Optional[ListNode] = None
    while head:
        tmp = head.next
        head.next = prev
        prev = head
        head = tmp
    return prev


if __name__ == "__main__":
    doctest.testmod()
