from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. Build Trie directly using TrieNode
        root = TrieNode()
        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.endOfWord = True

        ROWS, COLS = len(board), len(board[0])
        res = set()
        visit = set()

        def dfs(r: int, c: int, node: TrieNode, word: str):
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visit or
                board[r][c] not in node.children
            ):
                return

            char = board[r][c]
            next_node = node.children[char]
            word += char

            # Found a valid word
            if next_node.endOfWord:
                res.add(word)
                next_node.endOfWord = False  # Pruning: don't match same word twice

            visit.add((r, c))

            dfs(r - 1, c, next_node, word)
            dfs(r + 1, c, next_node, word)
            dfs(r, c - 1, next_node, word)
            dfs(r, c + 1, next_node, word)

            visit.remove((r, c))

            # Pruning: prune leaf nodes with no more words down this branch
            if not next_node.children:
                del node.children[char]

        # 2. Launch DFS from every grid cell with row/col integer indices
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)