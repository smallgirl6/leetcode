# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: Calculate the length of the linked list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Step 2: Determine the basic size and extras
        baseSize, extra = divmod(length, k)

        # Step 3: Split the list into parts
        result = []
        curr = head
        for i in range(k):
            partHead = curr
            # If this part needs an extra node
            if i < extra:
                for j in range(baseSize + 1 - 1):  # We subtract 1 because we need (size-1) connections
                    if curr:
                        curr = curr.next
            else:
                for j in range(baseSize - 1):
                    if curr:
                        curr = curr.next
            # Detach the current part from the rest of the list
            if curr:
                nextPart = curr.next
                curr.next = None
                curr = nextPart
            # Append the part to the result list
            result.append(partHead)

        return result