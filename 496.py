class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mapping = {}
        
        for num in nums2:
            while stack and stack[-1] < num:
                mapping[stack.pop()] = num
            stack.append(num)
            
        while stack:
            mapping[stack.pop()] = -1
            
        return [mapping[num] for num in nums1]