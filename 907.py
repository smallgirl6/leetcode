class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        #  Since the answer may be large, return the answer modulo 10**9 + 7.大質數
        MOD = 10**9 + 7
        stack = []
        ans = dot = 0  # dot 代表從當前元素到前一個比它小的元素子數組的和

        for i, num in enumerate(arr):
            count = 1
            while stack and stack[-1][0] >= num:  # 移除 stack 頂部所有小於或等於當前元素的元素
                val, cnt = stack.pop()
                count += cnt  # 更新 count 為從當前元素到前一個比它小的元素的距離
                dot -= val * cnt  # 更新 dot

            stack.append((num, count))  # 將當前元素和 count 加入 stack
            dot += num * count  # 更新 dot
            ans = (ans + dot) % MOD  # 更新答案

        return ans