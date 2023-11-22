# Definition for singly-linked list.
# 1
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        carry = 0
        result = None # 返回最終的相加結果
        # 將 l1 和 l2 的數字推入各自的棧
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        # 進行相加，處理是否有剩餘的進位carry。如果最後的 carry 不為零
        while stack1 or stack2 or carry: 
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0

            total = val1 + val2 + carry
            carry = total // 10 # total= 15，totla // 10 = 1，有一個進位。total = 9，total // 10 = 0，沒有進位
            total = total % 10 # total = 15，totla % 10 = 5

            # 創建新節點並將其加入結果鏈表
            currentNode = ListNode(total)
            currentNode.next = result # 將 currentNode.next 指向當前的 result，currentNode 成了新的鏈表頭節點
            result = currentNode # result 指向新的鏈表頭部

        return result
# 2
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 ,stack2 = [],[]
        result = None
        carry = 0 
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        while stack1 or stack2:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            total = total % 10

            currentNode = ListNode(total)
            currentNode.next = result
            result = currentNode
        if carry != 0 : # 處理是否有剩餘的進位carry。如果最後的 carry 不為零
            currentNode = ListNode(carry)
            currentNode.next = result
            result = currentNode
        return result