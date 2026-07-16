class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #s加入hashmap
        hashmap = dict()
        for char in s:
            if char not in hashmap:
                hashmap[char] = 1
            hashmap[char] += 1
        
        #t加入hashmap1
        hashmap1 = dict()
        for char in t:
            if char not in hashmap1:
                hashmap1[char] = 1
            hashmap1[char] += 1

        #判断是否一样
        if hashmap == hashmap1:
            return True
        return False

        
            