class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = {}
        start = 0
        maxlen = 0
        for i in range(len(s)):
            if s[i] in counter:
                start = max(start, counter[s[i]]+1)
            counter[s[i]] = i
            maxlen = max(maxlen,i-start+1)
        return maxlen