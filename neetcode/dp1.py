import doctest


# https://leetcode.com/problems/climbing-stairs
def climb_stairs(n: int) -> int:
    """
    >>> climb_stairs(2)
    2
    >>> climb_stairs(3)
    3
    """
    if n <= 2:
        return n

    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        cur = prev1 + prev2
        prev2, prev1 = prev1, cur
    return prev1


if __name__ == "__main__":
    doctest.testmod()
