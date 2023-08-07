class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        counter = set()
        
        #arr = [2, 4, 3]
        #       ^        counter = {}
        #          ^     檢查4的兩倍（即8）是否在counter中，結果是沒有 4*2 =8
        #                4是一個偶數，會檢查4的一半（即2）是否在counter中，結果是存在的。因此，我們找到了一對符合條件的數字，即2和4。
        #             ^  3是一個奇數，3的一半（即1.5）不可能在arr中
        for num in arr:
            if num * 2 in counter  or (num % 2 == 0 and num // 2 in counter):
                return True
            counter.add(num)
        print(counter)
        return False