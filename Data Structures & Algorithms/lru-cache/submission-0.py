class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)

        #left = least recently used, right = most recently used
        self.left.next = self.right
        self.right.prev = self.left


    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    #insert right
    def insert(self, node):
        prev = self.right.prev

        node.prev = prev
        node.next = self.right

        prev.next = node
        self.right.prev = node


    def get(self, key: int) -> int:

        #如果已经有 就更新list remove+insert保证最在右边
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:

        # 如果cache已经有则remove更新list
        if key in self.cache:
            self.remove(self.cache[key])

        # cache加入新创建的node
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # 如果大于内存大小，进行左边最不常用的remove，并且更新cache
        if len(self.cache) > self.cap:
            leastUsed = self.left.next
            self.remove(leastUsed)
            del self.cache[leastUsed.key]
