class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []  # 創建一個 Stack 對象
        for asteroid in asteroids:  # 遍歷 asteroids 數組
            #會碰撞的狀況(前後是一正一負)
            while stack and asteroid < 0 < stack[-1]:  # 如果當前小行星與 Stack 最上面的元素都存在，並且當前小行星是負數，Stack 最上面的元素是正數
                if stack[-1] < -asteroid:  # 如果 Stack 最上面的元素比當前小行星的小，則彈出 Stack 最上面的元素，繼續處理當前小行星
                    stack.pop()
                    continue # asteroids = [10,2,-5]的例子
                elif stack[-1] == -asteroid:  # 如果 Stack 最上面的元素和當前小行星大小相同，則彈出 Stack 最上面的元素，並且跳出 while 循環
                    stack.pop( )#當前小行星已經銷毀了，不會再和其他小行星碰撞。 # asteroids =[8,-8]的例子
                break 
                # 如果 while 循環正常結束，將當前小行星壓入 Stack 中
            else: # 如果while被 break 中斷，則不會執行 else 
                stack.append(asteroid)
        return stack  # 返回 Stack 中剩下的小行星