import doctest
from collections import deque


# https://leetcode.com/problems/number-of-islands
def num_islands(grid: list[list[str]]) -> int:
    """
    >>> num_islands([
    ...   ["1","1","1","1","0"],
    ...   ["1","1","0","1","0"],
    ...   ["1","1","0","0","0"],
    ...   ["0","0","0","0","0"]
    ... ])
    1
    >>> num_islands([
    ...   ["1","1","0","0","0"],
    ...   ["1","1","0","0","0"],
    ...   ["0","0","1","0","0"],
    ...   ["0","0","0","1","1"]
    ... ])
    3
    """
    DIRS = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    rows, cols = len(grid), len(grid[0])
    visited: list[list[bool]] = [[False] * cols for _ in range(rows)]

    def visit(r: int, c: int) -> None:
        visited[r][c] = True
        queue = deque([(r, c)])
        while queue:
            r, c = queue.popleft()
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and grid[nr][nc] == "1"
                    and not visited[nr][nc]
                ):
                    visited[nr][nc] = True
                    queue.append((nr, nc))

    num_islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and not visited[r][c]:
                num_islands += 1
                visit(r, c)
    return num_islands


if __name__ == "__main__":
    doctest.testmod()
