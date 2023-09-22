class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        i = 0  # 追蹤 target 的索引
        for num in range(1,n+1): # 從 1 到 n 
            if i >= len(target):
                break #  如果我們已經建立了target，則停止
            result.append("Push") # 將當前數字推入STACK
            if num == target[i]: # num = 1 and target = [1,2,3]
                i += 1  # 移動到 target 的下一個元素
            else: # num != target[i] num = 2 and target = [1,3]
                result.append("Pop") #如果當前數字與 target 不匹配，則將其POP
        return result 