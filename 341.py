class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]  # reverse the list and use it as a stack

    def next(self) -> int:
        # The hasNext method ensures that the top of stack is an Integer
        # so we can safely pop it and return the Integer.
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]  # peek the top element
            if top.isInteger():
                return True
            
            # If the top element is a list, we will pop it and push its elements onto the stack.
            self.stack.pop()
            self.stack.extend(top.getList()[::-1])  # reverse the list before adding to stack
        
        return False