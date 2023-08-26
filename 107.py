class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        output = []
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                current = queue.popleft()
                level.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            output.append(level)
        return output[::-1]

# 先從頂層到底層進行了層序遍歷，最後再把結果翻轉過來
# queue  = [3]
# while queue:：
# level 列表 存放該層的節點值

# level = [3]      queue  = [9, 20]
# level = [9, 20]  queue  = [15, 7]
# level = [15, 7]