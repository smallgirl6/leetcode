class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-1,0,1,2,-1,-4]
        nums.sort()
        print(nums) # [-4, -1, -1, 0, 1, 2]
        ret = []
        for i in range(len(nums)-2):  # [             i ,l,r]
                                      #                  ^まで
            # i 必須大於 0 ，i=0，則 i-1 會是 -1，在 Python 中，-1 會回傳列表的最後一個元素
            # 如果發現當前的數與前一個數相同，就跳過這一次迴圈
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i+1, len(nums)-1   # [-4, -1, -1, 0, 1, 2]
                                             # [ i , l           ,r]
            while left < right:              # [             i ,l,r]
                sum = nums[i] + nums[left] +nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -=1
                else:
                    ret.append([nums[i], nums[left], nums[right]]) 
                    while  left < right and nums[left] == nums[left+1]: # 下一個跟自己的值一樣的話就在找下一個
                        left += 1
                    while left < right and nums[right] == nums[right-1]:# 下一個跟自己的值一樣的話就在找下一個
                        right -= 1
                    left += 1
                    right -= 1
        return ret
            