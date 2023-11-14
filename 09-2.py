#從兩邊開始找
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        n = len(x)
        i,j = 0, n-1
        while i <= j:
            if x[i] != x[j]:
                return False
            i= i+1
            j= j-1
        return True