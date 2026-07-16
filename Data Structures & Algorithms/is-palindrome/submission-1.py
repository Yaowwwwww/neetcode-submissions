class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        if len(s) == 1:
            return True
        halfLength = int(len(s) / 2)
        firstHalf = s[:halfLength].lower()
        secondHalf = s[-halfLength:].lower()
        if firstHalf == ''.join(reversed(secondHalf)):
            return True
        return False