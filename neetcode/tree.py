from __future__ import annotations

import doctest
from collections import deque
from typing import Deque, Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, lst: list[int]) -> Optional[TreeNode]:
        if not lst or not lst[0]:
            return None

        root = cls(lst[0])
        queue = deque([root])
        i = 1

        while queue and i < len(lst):
            node = queue.popleft()
            if i < len(lst) and (lval := lst[i]) is not None:
                node.left = cls(lval)
                queue.append(node.left)
            i += 1
            if i < len(lst) and (rval := lst[i]) is not None:
                node.right = cls(rval)
                queue.append(node.right)
            i += 1

        return root

    @classmethod
    def to_list(cls, root: Optional[TreeNode]) -> list[Optional[int]]:
        if not root:
            return []

        res: list[Optional[int]] = []
        queue: Deque[Optional[TreeNode]] = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append(None)

        while res and res[-1] is None:
            res.pop()

        return res


# https://leetcode.com/problems/invert-binary-tree
def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    >>> TreeNode.to_list(invert_tree(TreeNode.from_list([4,2,7,1,3,6,9])))
    [4, 7, 2, 9, 6, 3, 1]
    >>> TreeNode.to_list(invert_tree(TreeNode.from_list([2,1,3])))
    [2, 3, 1]
    >>> TreeNode.to_list(invert_tree(TreeNode.from_list([])))
    []
    """
    if not root:
        return None

    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


if __name__ == "__main__":
    doctest.testmod()
