class TrieNode:
    def __init__(self):
        self.children = {}
        self.END = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.END = True

    def search(self, word: str) -> bool:
        def dfs(i, root):#i 代表到word第几个c了
            curr = root#用root来推进
            
            #每一个都要尝试 用for快速推进尝试
            for j in range(i, len(word)):
                c = word[j]#当前word中的c
                if c == ".":
                    for child in curr.children.values():
                        if dfs(j + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.END
            
        return dfs(0, self.root)
