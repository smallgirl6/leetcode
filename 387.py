class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        for c in s:
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
            
        for i in range(len(s)):
            if dict[s[i]] == 1:
                return i
        return -1