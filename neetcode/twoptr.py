import doctest


# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
def two_sum(nums: list[int], target: int) -> list[int]:
    """
    >>> two_sum([2,7,11,15], 9)
    [1, 2]
    >>> two_sum([2,3,4], 6)
    [1, 3]
    >>> two_sum([-1,0], -1)
    [1, 2]
    """
    start, end = 0, len(nums) - 1
    while start < end:
        sum = nums[start] + nums[end]
        if sum < target:
            start += 1
        elif sum > target:
            end -= 1
        else:
            return [start + 1, end + 1]
    raise Exception("no solution found")


# https://leetcode.com/problems/valid-palindrome
def is_palindrome(s: str) -> bool:
    """
    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    >>> is_palindrome("race a car")
    False
    >>> is_palindrome(" ")
    True
    """
    start, end = 0, len(s) - 1
    while start < end:
        if not s[start].isalnum():
            start += 1
        elif not s[end].isalnum():
            end -= 1
        elif s[start].lower() == s[end].lower():
            start += 1
            end -= 1
        else:
            return False
    return True


if __name__ == "__main__":
    doctest.testmod()
