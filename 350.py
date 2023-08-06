class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        result = []
        print(counter1)
        for num in nums2:
            if counter1[num] >= 1:
                result.append(num)
                counter1[num] -=1
        return result

