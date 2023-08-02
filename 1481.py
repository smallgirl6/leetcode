class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        table = collections.Counter(arr) # ({5: 2, 4: 1} ({4: 1, 3: 3, 1: 2, 2: 1}
        print(table)
        count_arr = sorted(table.values(),reverse=False) # [1,2]  ,  [1,1,2,3]
        print(count_arr) # [1,2]  ,  [1,1,2,3]
        ans = len(count_arr)
        for num in count_arr :

            if k >= num:   # count_arr:[1,1,2,3]  k = 3                ## count_arr:[1,2]  k = 1
                           #            ^         num = 1              ##            ^     num = 1
                k-=num     # k = 3 num = 1 => 2                        ## k = 1 num = 1 => 0
                ans -= 1   # count_arr:[1,1,2,3]   => ans=4  => ans=3  ## count_arr:[1,2]  => ans=2  => ans=1
            else:
                break
        return ans