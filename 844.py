class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []  # 創建一個 Stack 對象，用於存儲 s 字符串中的字符
        stack2 = []  # 創建一個 Stack 對象，用於存儲 t 字符串中的字符
        for c in s:  # 遍歷 s 字符串中的每個字符
            if c != '#':  # 如果當前字符不是回刪字符，加入 Stack 中
                stack1.append(c)
            if c == '#' and stack1:  # 如果當前字符是回刪字符，且 Stack 不為空，則pop出 Stack 最上面的元素
                stack1.pop()
        for c in t:  # 遍歷 t 字符串中的每個字符
            if c != '#':  # 如果當前字符不是回刪字符，將其壓入 Stack 中
                stack2.append(c)
            if c == '#' and stack2:  # 如果當前字符是回刪字符，且 Stack 不為空，則pop出 Stack 最上面的元素
                stack2.pop()

        return stack1 == stack2  # 返回比較兩個 Stack 中剩下的元素是否相等的結果