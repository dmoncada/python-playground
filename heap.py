from heapq import heappush, heappop


class MinHeap():
    '''A simple min. heap data structure. Built on top of heapq.'''

    class EmptyHeapException(Exception):
        pass

    def __init__(self, sign=1):
        '''Initializes self.'''

        self.sign = sign
        self.heap = []

    def __len__(self):
        '''Returns len(self).'''

        return len(self.heap)

    def insert(self, value):
        '''insert(item) -> None -- Inserts item to the heap, while keeping the
        min (max, resp.) heap property.'''

        heappush(self.heap, self.sign * value)

    def extract(self):
        '''extract() -> item -- removes and returns the item at the top.
        Raises EmptyHeapException if the heap is empty.'''

        if not self.heap:
            raise self.EmptyHeapException('heap is empty')

        return self.sign * heappop(self.heap)

    def peek(self):
        '''peek() -> item -- returns (without removing) the item at the top.
        Raises EmptyHeapException if the heap is empty.'''

        if not self.heap:
            raise self.EmptyHeapException('heap is empty')

        return self.sign * self.heap[0]

    def is_empty(self):
        '''is_empty() -> boolean -- asserts if the heap is empty.'''

        return not self.heap


class MaxHeap(MinHeap):
    '''A simple max. heap data structure. Inherits from MinHeap.'''

    def __init__(self, sign=-1):
        super().__init__(sign)
