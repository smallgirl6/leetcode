class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        print(list(map(s.index,s)))
        return list(map(s.index,s)) == list(map(t.index,t))