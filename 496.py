class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [] # 暫存還沒有找到右邊第一個比它大的數字的元素
        mapping = {} #存每一個數字的“下一個更大元素
        
        # nums1 = [4,1,2], nums2 = [1,3,4,2]
        #                           ^        stack = [1] stack.append(num)
        #                             ^      stack[-1] < num，stack 的頂部是 1，1 < 3， 3 是 1 的下一個更大元素。將 1 從 stack 中移除並在 mapping 中設置映射
        #                                     stack = []  mapping = {1: 3} ，然後將 3 放入 stack，stack = [3]
        #                               ^    stack[-1] < num，stack 的頂部是 3，3 < 4， 4 是 3 的下一個更大元素。將 3 從 stack 中移除並在 mapping 中設置映射
        #                                     stack = []  mapping = {1: 3, 3: 4} ，然後將 4 放入 stack，stack = [4]
         #                                 ^    stack[-1] < num，stack 的頂部是 4， 2比4小 不能為4置映射。直接將 2 放入 stack， stack = [4, 2]
        for num in nums2:
            while stack and stack[-1] < num:
                popednum = stack.pop()
                mapping[popednum] = num
                # mapping[stack.pop()] = num
            stack.append(num)

        #  stack = [4, 2]    mapping = {1: 3, 3: 4, 4: -1, 2: -1}
        # 4 和 2 在nums2的右側都沒有比它們更大的數字，所以它們的“下一個更大元素”都是-1。
        while stack:
                popednum = stack.pop()
                mapping[popednum] = -1
            # mapping[stack.pop()] = -1
        
        # nums1 = [4,1,2]
        # mapping = {4: -1, 1: 3, 2: -1}
        return [mapping[num] for num in nums1]