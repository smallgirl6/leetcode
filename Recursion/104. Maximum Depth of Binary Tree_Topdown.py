class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0 # maximun depth
        def recr(node, curDepth):
            nonlocal ans
            if not node:
                return 
            
            curDepth +=  1
            # 去比較目前記錄的最大深度，若超越了目前記錄的最大深度則更改最大深度的紀錄
            ans = max(ans, curDepth)

            # 遞歸遍歷左子樹和右子樹，分別傳入左子樹和右子樹的根節點以及當前深度加1後的結果。
            recr(node.left, curDepth)
            recr(node.right, curDepth)
            
        recr(root, 0)
        return ans
