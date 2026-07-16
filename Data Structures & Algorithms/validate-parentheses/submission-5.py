class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(': ')', '[': ']', '{': '}'}
        for char in s:
            if char in mapping.keys():
                stack.append(char)
            elif char in mapping.values():
                if not stack or stack and mapping.get(stack.pop()) != char:
                    return False
        if stack: 
            return False
        return True