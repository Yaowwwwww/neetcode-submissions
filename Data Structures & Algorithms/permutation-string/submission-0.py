class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 因为固定字符和长度，并未需要频繁比较，因此list更快

        # 1.排除s1大于s2 不可能
        if len(s1) > len(s2):
            return False
        # 2. 初始化两个count的s1长度的window
        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        # 3，初始化matches。O(26)
        matching = 0
        for i in range(26):
            matching += (1 if s1Count[i] == s2Count[i] else 0)

        # 4.设置l和r处理window渐进逻辑 检查matches
        l = 0
        for r in range(len(s1), len(s2)):
            if matching == 26:
                return True
            # 处理右边增加和matching update
            s2Count[ord(s2[r]) - ord('a')] += 1
            if s1Count[ord(s2[r]) - ord('a')] == s2Count[ord(s2[r]) - ord('a')]:
                matching += 1
            elif s2Count[ord(s2[r]) - ord('a')] - 1 == s1Count[ord(s2[r]) - ord('a')]:
                matching -= 1
            # 处理左边减少和matching update
            s2Count[ord(s2[l]) - ord('a')] -= 1
            if s2Count[ord(s2[l]) - ord('a')] == s1Count[ord(s2[l]) - ord('a')]:
                matching += 1
            elif s2Count[ord(s2[l]) - ord('a')] + 1 == s1Count[ord(s2[l]) - ord('a')]:
                matching -= 1
            l += 1
        return matching == 26

        

