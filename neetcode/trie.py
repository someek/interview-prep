import doctest


# https://leetcode.com/problems/implement-trie-prefix-tree
class Trie:
    """
    >>> t = Trie()
    >>> t.insert("apple")
    >>> t.search("apple")
    True
    >>> t.search("app")
    False
    >>> t.starts_with("app")
    True
    >>> t.insert("app")
    >>> t.search("app")
    True
    """

    class Node:
        def __init__(self, end: bool = False):
            self.next: dict[str, Trie.Node] = {}
            self.end = end

    def __init__(self):
        self.root = Trie.Node()

    def insert(self, word: str) -> None:
        ptr = self.root
        for c in word:
            if c not in ptr.next:
                ptr.next[c] = Trie.Node()
            ptr = ptr.next[c]
        ptr.end = True

    def search(self, word: str) -> bool:
        ptr = self.root
        for c in word:
            if c not in ptr.next:
                return False
            ptr = ptr.next[c]
        return ptr.end

    def starts_with(self, prefix: str) -> bool:
        ptr = self.root
        for c in prefix:
            if c not in ptr.next:
                return False
            ptr = ptr.next[c]
        return True


if __name__ == "__main__":
    doctest.testmod()
