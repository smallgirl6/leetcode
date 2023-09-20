class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        stack = [root]
        output = []
        
        while stack:
            node = stack.pop()
            if node:
                output.append(node.val)
                
                # 先將右子樹推入棧，因為棧是後進先出，
                # 這樣可以確保左子樹會先被處理
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        
        return output