# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        current = self.head
        chosen_value = None
        n = 0

        while current:
            n += 1
            if random.randint(1, n) == 1:
                chosen_value = current.val
            current = current.next

        return chosen_value

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()