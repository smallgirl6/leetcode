class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = [] # 保存那些還未找到"下一個更大的元素"的元素的索引
        res = [-1] * len(nums) # 假設所有元素的"下一個更大的元素"都不存在，都是 -1
        
        for i in range(len(nums) * 2):  # 確保每一個元素都被當作起始點考慮過，並且每個元素的右邊所有的元素都被檢查過
            num = nums[i % len(nums)]   # 當遍歷整個數組兩次時 i 的值將會超過 nums 的長度。但是 nums 是一個循環的數組，當遍歷到數組的終點並想要繼續查找時，需要從數組的開頭重新開始
            # nums = [1,2,3,4,3]
            # i = 0 -> i % 5 = 0 -> nums[0 % 5] = nums[0] = 1
            # i = 1 -> i % 5 = 1 -> nums[1 % 5] = nums[1] = 2
            # i = 2 -> i % 5 = 2 -> nums[2 % 5] = nums[2] = 3
            # i = 3 -> i % 5 = 3 -> nums[3 % 5] = nums[3] = 4
            # i = 5 -> i % 5 = 4 -> nums[4 % 5] = nums[4] = 3
            
            # 1 -> stack是空的，i < len(nums): stack.append(i) ，把1的索引0放入堆疊，現在 stack = [0]
            # 2 -> stack = [0]，nums[stack[-1]] < num: 2比stack頂部的數字（也就是1）大 ，stack.pop()-> 0， res[popednum] = num -> res[0] = 2 -> res = [2, -1, -1, -1, -1]，i < len(nums): stack.append(i) ，把2的索引1放入堆疊，現在 stack = [1]
            # 3 -> stack = [1]，nums[stack[-1]] < num: 3比stack頂部的數字（也就是2）大 ，stack.pop()-> 1， res[popednum] = num -> res[1] = 3 -> res = [2, 3, -1, -1, -1]，i < len(nums): stack.append(i) ，把3的索引2放入堆疊，現在 stack = [2]
            # 4 -> stack = [2]，nums[stack[-1]] < num: 4比stack頂部的數字（也就是3）大 ，stack.pop()-> 2， res[popednum] = num -> res[2] = 4 -> res = [2, 3, 4, -1, -1]，i < len(nums): stack.append(i) ，把4的索引3放入堆疊，現在 stack = [3]
            # 3 -> stack = [2]，nums[stack[-1]] < num: 43比stack頂部的數字（也就是4）小 ，不進入這個循環，i < len(nums): stack.append(i) ，把3的索引4放入堆疊，現在 stack = [3,4]
            # 第二輪
            # 1 -> stack = [3,4]，nums[stack[-1]] < num: 1比stack頂部(4)的數字（也就是3）小 ，不進入這個循環，也不符合if i < len(nums)
            # 2 -> stack = [3,4]，nums[stack[-1]] < num: 2比stack頂部(4)的數字（也就是3）小 ，不進入這個循環，也不符合if i < len(nums)
            # 3 -> stack = [3,4]，nums[stack[-1]] < num: 3等於stack頂部(4)的數字（也就是3） ，不進入這個循環，也不符合if i < len(nums)
            # 4 -> stack = [3,4]，nums[stack[-1]] < num: 4大於stack頂部(4)的數字（也就是3） ，stack.pop()-> 4， res[popednum] = num -> res[4] = 4 -> res = [2, 3, 4, -1, 4]，不符合if i < len(nums)
            # 3 ->  stack = [3]，nums[stack[-1]] < num: 3小於stack頂部(3)的數字（也就是4） 不進入這個循環，不符合if i < len(nums)
            # 最後的結果是：res = [2, 3, 4, -1, 4]

            while stack and nums[stack[-1]] < num: # 當stack不為空，且堆stack頂部的數字小於當前數字時，進入這個循環。
            # nums = [1,2,3,4,3]
            
                popednum = stack.pop()
                res[popednum] = num
            if i < len(nums):  # 確保只在第一次遍歷 nums 數組時將索引加到 stack 中。這是因為，我們已經遍歷了整個數組兩次，所以不需要再次添加索引。
                stack.append(i)
        return res
            
