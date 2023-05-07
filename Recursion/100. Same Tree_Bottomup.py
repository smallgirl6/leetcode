# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        # 判斷兩個節點是否相等
        def is_node_equal(node1, node2):
            if node1 is None and node2 is None: # 兩個節點都為空，返回 True
                return True
            elif node1 is None or node2 is None: # 其中一個節點為空，則返回 False
                return False
            elif node1.val != node2.val:         # 兩個節點的值不相等，則返回 False
                return False
            else:                                # 否則返回 True。
                return True  
        
        # 判斷以兩個節點為根節點的樹是否相等
        def is_subtree_equal(node1, node2):
            if node1 is None and node2 is None:  # 兩個節點都為空，返回 True
                return True
            elif node1 is None or node2 is None: # 其中一個節點為空，返回 False
                return False
            elif not is_node_equal(node1, node2): # node1 和 node2 的值不相等，返回 False。
                return False
            # 遞歸調用 is_subtree_equal 函數判斷左右子樹是否相等，如果左右子樹都相等，則返回 True；否則，返回 False
            else:
                return is_subtree_equal(node1.left, node2.left) and is_subtree_equal(node1.right, node2.right)
        
        # 判斷 p 和 q 是否相等
        return is_subtree_equal(p, q)




