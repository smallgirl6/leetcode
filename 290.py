class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        print(words)
        if len(pattern) != len(words):
            return False
        print(list(map(pattern.index,pattern)))
        print(list(map(words.index,words)))
        return list(map(pattern.index,pattern)) == list(map(words.index,words)) 