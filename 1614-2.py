# Count
class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_count = 0
        for c in s:
            if c =="(":
                count += 1
            elif c == ")":
                count -= 1
            max_count = max(max_count,count)
        return max_count