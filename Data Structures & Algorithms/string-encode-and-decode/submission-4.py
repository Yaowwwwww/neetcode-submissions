class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            result += f"{len(i)}:{i}"
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        index = 0
        while index < len(s):
            j = s.find(":",index)
            length = int(s[index:j])
            result.append(s[j+1:j+1+length])
            index = j+1+length
        return result