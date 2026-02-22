import doctest
from copy import deepcopy


# https://leetcode.com/problems/subsets
def subsets(nums: list[int]) -> list[list[int]]:
    """
    >>> subsets([1,2,3])
    [[], [3], [2], [3, 2], [1], [3, 1], [2, 1], [3, 2, 1]]
    >>> subsets([0])
    [[], [0]]
    """
    if not nums:
        return [[]]

    wo = subsets(nums[1:])
    w = deepcopy(wo)
    for subset in w:
        subset.append(nums[0])

    return wo + w


if __name__ == "__main__":
    doctest.testmod()
