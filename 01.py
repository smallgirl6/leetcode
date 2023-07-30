class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}
        for i,num in enumerate(nums):
            if target - num  in counter:
                return [counter[target - num], i]
            counter[num] = i
        return []
