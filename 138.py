class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Create node mappings
        node_map = {}
        curr = head
        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next

        # Step 2: Set next and random pointers for new list
        curr = head
        while curr:
            if curr.next:
                node_map[curr].next = node_map[curr.next]
            if curr.random:
                node_map[curr].random = node_map[curr.random]
            curr = curr.next

        return node_map[head]
        