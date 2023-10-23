# stack
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        stack = [root]
        result = 0
        
        while stack:
            node = stack.pop()
            
            # 當前節點的值在給定範圍內，則將其加入到結果中。
            if low <= node.val <= high:
                result += node.val
            
            # 如果當前節點有左子節點且當前節點的值大於 low，則將左子節點推入棧中。因為有可能左子樹中還有節點的值在給定的範圍內
            if node.left and node.val > low:
                stack.append(node.left)
            
            # 如果當前節點有右子節點且當前節點的值小於 high，則將右子節點推入棧中。因為有可能右子樹中還有節點的值在給定的範圍內
            if node.right and node.val < high:
                stack.append(node.right)
        
        return result