import doctest


# https://leetcode.com/problems/binary-search
def search(nums: list[int], target: int) -> int:
    """
    >>> search([-1,0,3,5,9,12], 9)
    4
    >>> search([-1,0,3,5,9,12], 2)
    -1
    """
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    doctest.testmod()
