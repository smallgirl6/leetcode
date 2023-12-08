class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)
        ### 回文字串時，通常每個字元都應該成對出現。 
        # abba 中，'a' 和 'b' 都是成對出現的。
        # 但可以允許有一個字符出現奇數次，比如 "abcba"，的 'c' 就是只出現一次的字符，它位於回文串的中心。
        # 如果字串中至少有一個字元出現了奇數次，has_odd 就會被設為 True，在建構回文字串時，使用這個奇數次出現的字元作為中心。
        has_odd = False
        ans = 0
        for length in counter.values():
            if length % 2 ==1: # 檢查出現的次數是否為奇數。
                ans += length -1 # 回文除中心字元外，其他字元都應成對出現，所以將 length 減 1（變成偶數），然後將其加到 ans。 取最多的成對字元用於建立回文。
                has_odd =True
            else:
                ans += length
        return ans +int(has_odd)        
