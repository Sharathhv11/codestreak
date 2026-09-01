class myStack:
    def __init__(self, n):
        # Define Data Structures
        self.limit = n
        self.stack = []

    
    def isEmpty(self):
        # Check if stack is empty
        return len(self.stack) == 0

    
    def isFull(self):
        # Check if stack is full
        return len(self.stack) == self.limit

    
    def push(self, x):
        # Insert x at the top of the stack
        if( len(self.stack) >= self.limit ):
            return False
        self.stack.append(x)
        return True

    
    def pop(self):
        # Removes an element from the top of the stack
        if( not len(self.stack)  ):
            return -1
        return self.stack.pop()

    
    def peek(self):
        # Returns the top element of the stack
        if( not len(self.stack)  ):
            return -1
        return self.stack[-1]
        