# RECR +MEMO
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         @lru_cache(None)
#         def recr(i,j):
#             if i >= len(text1) or j >= len(text2):
#                 return 0
#             if text1[i] == text2[j]:
#                 return 1 + recr(i+1,j+1)
#             return max(recr(i+1,j),recr(i,j+1))
#         return recr(0,0)

#DP
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         n1,n2 = len(text1), len(text2)
#         dp = [[0] * (n2+1) for  _ in range(n1+1)]
#         for i in range(n1-1, -1, -1):
#           for j in range(n2-1, -1, -1):
#             if text1[i] == text2[j]:
#               dp[i][j] = 1 + dp[i+1][j+1]
#             else:
#               dp[i][j] = max(dp[i+1][j], dp[i][j+1])
#         return dp[0][0]
#DP good
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1,n2 = len(text1), len(text2)
        dp = [0] * (n2+1) 
        for i in range(n1-1, -1, -1):
          newdp = [0] * (n2+1)
          for j in range(n2-1, -1, -1):
            newdp[j] = dp[j]
            if text1[i] == text2[j]:
              dp[j] = 1 + newdp[j+1]
            else:
              dp[j] = max(dp[j], dp[j+1])
        return dp[0]