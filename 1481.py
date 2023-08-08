# 目標是在刪除恰好k個元素後，該數組中保留的唯一（即非重複）整數的最少數量。
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        table = collections.Counter(arr) # ({5: 2, 4: 1} ({4: 1, 3: 3, 1: 2, 2: 1}
        print(table)
        count_arr = sorted(table.values(),reverse=False) # [1,2]  ,  [1,1,2,3] 
        print(count_arr) # [1,2]  ,  [1,1,2,3]
        ans = len(count_arr) # 2 ,4 #代表有ans 種不同的數字
        for num in count_arr :

            if k >= num:   # count_arr:[1,1,2,3]  k = 3                ## count_arr:[1,2]  k = 1
                           #            ^         num = 1              ##            ^     num = 1
                           # count_arr:[1,2,3]  k = 2
                           #            ^       num = 1
                           # count_arr:[2,3]  k = 1
                           #            ^     num = 2   >>>>>> break
                k-=num     # k = 3 num = 1  k => 2                                ## k = 1 num = 1  k => 0
                           # k = 2 num = 1  k => 1 
                ans -= 1   # count_arr:[1,1,2,3]   => ans=4  => ans=3 [1,2,3]   ## count_arr:[1,2]  => ans=2  => ans=1
                           # count_arr:[1,2,3]     => ans=3  => ans=2 [2,3]
            else:
                break
        return ans