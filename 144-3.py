#STACK2
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        result = []
        while stack or root:
            while root:
                stack.append(root)
                result.append(root.val)
                root = root.left
            root = stack.pop()
            root = root.right
        return result