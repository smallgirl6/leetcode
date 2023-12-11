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
        chosen_value = None # 儲存被選中節點的值
        n = 0               # 遍歷過的節點

        while current:
            n += 1
            if random.randint(1, n) == 1: # 生成一個從 1 到 n 的隨機數 如果這個隨機數等於 1
            # 遍歷每個節點時，生成的隨機數有 1/n 的機會等於 1 保證了所有節點被選中的機率是公平
                chosen_value = current.val # 將當前節點的值賦給 chosen_value
            current = current.next

        return chosen_value

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()