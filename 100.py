class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue_p , queue_q = [p], [q]

        while queue_p and queue_q:
            node_p, node_q = queue_p.pop(0), queue_q.pop(0)
        
            if not node_p and node_q or node_p and not node_q:
                return False
            if node_p and node_q:
                if node_p.val != node_q.val:
                    return False
                queue_p.append(node_p.left)
                queue_p.append(node_p.right)
                queue_q.append(node_q.left)
                queue_q.append(node_q.right)

        if queue_p or queue_q:
            return False
        return True