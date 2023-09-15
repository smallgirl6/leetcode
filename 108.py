class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        stack = [(0, len(nums) - 1, None, 'r')]

        root = None

        while stack:
            l, r, parent, pos = stack.pop()
            if l <= r:
                m = (l + r) // 2
                node = TreeNode(val=nums[m])

                if parent:
                    if pos == 'l':
                        parent.left = node
                    else:
                        parent.right = node

                else:
                    root = node

                stack.append((m + 1, r, node, 'r'))
                stack.append((l, m - 1, node, 'l'))

        return root
