import doctest


# https://leetcode.com/problems/valid-anagram
def is_anagram(s: str, t: str) -> bool:
    """
    >>> is_anagram("anagram", "nagaram")
    True
    >>> is_anagram("rat", "car")
    False
    """
    freq: list[int] = [0] * 26
    for c in s:
        freq[ord(c) - ord("a")] += 1
    for c in t:
        freq[ord(c) - ord("a")] -= 1
    return all(map(lambda x: x == 0, freq))


# https://leetcode.com/problems/contains-duplicate
def contains_duplicate(nums: list[int]) -> bool:
    """
    >>> contains_duplicate([1,2,3,1])
    True
    >>> contains_duplicate([1,2,3,4])
    False
    >>> contains_duplicate([1,1,1,3,3,4,3,2,4,2])
    True
    """
    seen: set[int] = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False


if __name__ == "__main__":
    doctest.testmod()
