class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = { i:num2 for num2, i in enumerate(nums2) }
        print(counter)
        result = []
        for num1 in nums1:
            result.append(counter[num1])
        return result