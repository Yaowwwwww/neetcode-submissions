class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def add_word(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.add_word(w)

        res = set()
        visited = set()

        def dfs(i, j, n, w):
            if (i < 0) or (j < 0) or (i >= len(board)) or (j >= len(board[0])) or (board[i][j] not in n.children) or ((i,j) in visited):
                return
            
            visited.add((i,j))
            w += board[i][j]
            n = n.children[board[i][j]]
            if n.is_word and w in words:
                res.add(w)

            dfs(i + 1, j, n, w)
            dfs(i - 1, j, n, w)
            dfs(i, j + 1, n, w)
            dfs(i, j - 1, n, w)
            visited.remove((i,j))

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root, "")

        return list(res)