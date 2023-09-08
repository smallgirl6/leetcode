class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        current_node = root
        total_sum = 0
        
        while stack or current_node:
            while current_node:
                stack.append(current_node)
                current_node = current_node.right
                
            current_node = stack.pop()

            total_sum += current_node.val
            current_node.val = total_sum

            current_node = current_node.left
        
        return root
        