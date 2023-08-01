class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        print(counter)

        result = []
        for num in nums:
            small_then_me = sum(counter[i] for i in counter if i < num)
            result.append(small_then_me)
        return result
