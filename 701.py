# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root

    @staticmethod
    def build_tree(values, index=0):
        if index < len(values) and values[index] is not None:
            node = TreeNode(values[index])
            node.left = Solution.build_tree(values, 2 * index + 1)
            node.right = Solution.build_tree(values, 2 * index + 2)
            return node
        return None

    @staticmethod
    def tree_to_list(root):
        if not root:
            return []
    
        queue = [root]
        result = []
        while any(queue):
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        while result and result[-1] is None:
            result.pop()
        
        return result 