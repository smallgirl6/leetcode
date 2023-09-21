# STACK
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                # 先將右子樹推入STACK，因為STACK是後進先出
                # 左子樹會先被處理
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return result