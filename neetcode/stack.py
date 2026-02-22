import doctest


# https://leetcode.com/problems/valid-parentheses
def is_valid(s: str) -> bool:
    """
    >>> is_valid("()")
    True
    >>> is_valid("()[]{}")
    True
    >>> is_valid("(]")
    False
    >>> is_valid("([])")
    True
    >>> is_valid("([)]")
    False
    """
    bracket_map = {")": "(", "}": "{", "]": "["}
    stack: list[str] = []
    for c in s:
        if c in bracket_map:
            if not stack or stack[-1] != bracket_map[c]:
                return False
            stack.pop()
        else:
            stack.append(c)
    return not stack


if __name__ == "__main__":
    doctest.testmod()
