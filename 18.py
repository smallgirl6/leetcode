class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        result = set()

        if N < 4:
            return []
        # nums = [1,0,-1,0,-2,2]
        #         ---i----         
        #           ----j----    
        #         i=1
        #         　j=0
        #              k=-1
        #                      l=2
        for i in range(N - 3):
            for j in range(i + 1, N - 2):
                k, l = j + 1, N - 1
                while k < l:
        #         i=1
        #         　j=0
        #              k=-1
        #                      l=2
        # ------------------------------- 2
        #           i=0
        #         　   j=-1
        #                 k=0
        #                      l=2  
        # ------------------------------- 1
        #           　 i=-1
        #         　      j=0
        #                    k=-2
        #                      l=2 
        # ------------------------------- -1                
                    s = nums[i] + nums[j] + nums[k] + nums[l]
                    if s == target:
                        result.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1
                    elif s < target:
                        k += 1
                    else:
                        l -= 1
        return list(result)