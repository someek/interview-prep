import doctest


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
def max_profit(prices: list[int]) -> int:
    """
    >>> max_profit([7,1,5,3,6,4])
    5
    >>> max_profit([7,6,4,3,1])
    0
    """
    lowest, max_profit = -1, 0
    for p in prices:
        if lowest == -1 or lowest > p:
            lowest = p
        else:
            max_profit = max(max_profit, p - lowest)
    return max_profit


if __name__ == "__main__":
    doctest.testmod()
