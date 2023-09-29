# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        current = head
        
        # 遍歷linked list並把所有節點的值push到stack中
        while current is not None:
            stack.append(current.val)
            current = current.next
        
        # 再次遍歷linked list並比較節點的值與stack中pop出的值
        current = head
        while current is not None:
            if current.val != stack.pop():
                return False
            current = current.next
        
        return True
        