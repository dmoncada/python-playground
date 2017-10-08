class Stack:
    '''A simple, generic stack data structure.'''

    class StackNode:
        def __init__(self, item, next_node):
            self.item = item
            self.next = next_node

    class EmptyStackException(Exception):
        pass

    def __init__(self):
        '''Initializes self.'''

        self.top = None
        self.count = 0

    def __len__(self):
        '''Returns len(self).'''

        return self.count

    def push(self, item):
        '''push(item) -> None -- Pushes item to the top.'''

        t = self.StackNode(item, self.top)
        self.top = t
        self.count += 1

    def pop(self):
        '''pop() -> item -- removes and returns the item at the top.
        Raises EmptyStackException if the stack is empty.'''

        if not self.top:
            raise self.EmptyStackException('stack is empty')

        item = self.top.item
        self.top = self.top.next
        self.count -= 1

        return item

    def peek(self):
        '''peek() -> item -- returns (without removing) the item at the top.
        Raises EmptyStackException if the stack is empty.'''

        if not self.top:
            raise self.EmptyStackException('stack is empty')

        return self.top.item

    def is_empty(self):
        '''is_empty() -> boolean -- asserts if the stack is empty.'''

        return not self.top
