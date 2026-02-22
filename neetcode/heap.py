import doctest
import heapq


# https://leetcode.com/problems/kth-largest-element-in-a-stream
class KthLargest:
    """
    >>> kl = KthLargest(3, [4, 5, 8, 2])
    >>> kl.add(3)
    4
    >>> kl.add(5)
    5
    >>> kl.add(10)
    5
    >>> kl.add(9)
    8
    >>> kl.add(4)
    8
    """

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap: list[int] = []

        nums.sort(reverse=True)
        for n in nums:
            if k == 0:
                break
            heapq.heappush(self.heap, n)
            k -= 1

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


if __name__ == "__main__":
    doctest.testmod()
