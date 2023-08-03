class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative_sum = 0
        total_subarrays = 0
        counter = {0: 1}
        print(counter)
        for num in nums:              # [1,2,3]
            cumulative_sum += num     #  num =1 cumulative_sum =1 , num =2 cumulative_sum =1+2=3
            print("cumulative_sum "+ str(cumulative_sum))
            diff = cumulative_sum - k #  k = 3 cumulative_sum =1 diff =-2 , k =3 cumulative_sum =3 diff =0
            print("diff "+str(diff))
            total_subarrays += counter.get(diff,0)  # total_subarrays = 0 , counter = {0: 1} total_subarrays = 1
            print("total_subarrays "+str(total_subarrays))
            counter[cumulative_sum] = counter.get(cumulative_sum, 0) + 1  # counter[1] = 0+1 -> counter = {0: 1, 1: 1}
        return total_subarrays

