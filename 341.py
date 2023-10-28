# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]  # # 逆序放入堆疊，以保持正確的遍歷順序

    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger(): #如果stack頂部的元素是一個整數（不是巢狀列表），直接返回True
                return True
            self.stack.pop() #如果是巢狀列表 需要將它移除以檢查其內部的元素
            self.stack.extend(top.getList()[::-1])  # 取得stack頂部元素中的所有子元素，然後將它們逆序加入stack      
        return False #如果迴圈結束而沒有返回True，那麼這意味著巢狀列表中沒有更多的整數，所以方法返回False
         


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())