"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self,root):
        if not root:
            return []
        queue = [root]
        output = []
        while queue:
            level = []
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.pop(0)
                level.append(node.val)
                
                for child in node.children:
                    queue.append(child)

            output.append(level)
        return output

# queue = [root]  
# queue = [1]  
#第一次while循環：
# level = []
# level_size = 1 （ queue 中只有一個節點：1）
# 取出 1，放入 level => level = [1]
# 將 1 的子節點 2, 3, 4, 5 放入 queue => queue = [2, 3, 4, 5]
# result.append([1]) => [[1]]

# queue = [2, 3, 4, 5]
# 第二次循環：
# level = []
# level_size = 4 （queue 中有 4 個節點：2, 3, 4, 5）
# 取出 2, 3, 4, 5，放入 level => level = [2, 3, 4, 5]
# 將這些節點的子節點 6, 7, 8, 9, 10 放入 queue => queue = [6, 7, 8, 9, 10]
# result.append([2, 3, 4, 5]) [[1],[2, 3, 4, 5]]

# queue = [6, 7, 8, 9, 10]
# 第三次循環：
# level = []
# level_size = 5 （因為 queue 中有 5 個節點：6, 7, 8, 9, 10）
# 取出 6, 7, 8, 9, 10，放入 level => level = [6, 7, 8, 9, 10] 
# 將這些節點的子節點 11, 12, 13 放入 queue => queue = [11, 12, 13]
# result.append([6, 7, 8, 9, 10]) [[1],[2, 3, 4, 5],[6, 7, 8, 9, 10]]
