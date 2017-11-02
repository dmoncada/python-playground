#!/usr/bin/env python3

from heap import MinHeap, MaxHeap
from random import randint


class RunningMedian():
    '''
    Maintains the median of a set of numbers, even as new ones are added.

    Numbers are distributed in a couple of (max and min) heaps; at any moment,
    all numbers less than (or equal to, if the set contains an odd number of
    items) the median are stored in the max heap, while the rest is kept in the
    min heap. The median is found by peeking both heaps.
    '''

    def __init__(self):
        self.minheap = MinHeap()
        self.maxheap = MaxHeap()

    # If heaps have the same num. of items, add the new number to the max heap.
    # Otherwise, add the new number to the min heap. Note that, when adding a
    # number, a transfer (from the max to the min heap or viceverse) might be
    # required.
    def add_number(self, new):
        if len(self.minheap) == len(self.maxheap):
            if not self.minheap.is_empty() and new > self.minheap.peek():
                self.maxheap.insert(self.minheap.extract())
                self.minheap.insert(new)
            else:
                self.maxheap.insert(new)
        else:
            if new < self.maxheap.peek():
                self.minheap.insert(self.maxheap.extract())
                self.maxheap.insert(new)
            else:
                self.minheap.insert(new)

    def find_median(self):
        if self.maxheap.is_empty():
            return 0

        if len(self.maxheap) == len(self.minheap):
            return (self.maxheap.peek() + self.minheap.peek()) / 2

        return self.maxheap.peek()


if __name__ == '__main__':
    rm = RunningMedian()
    numbers = [randint(10, 99) for i in range(10)]

    for i, number in enumerate(numbers):
        rm.add_number(number)
        median = rm.find_median()

        print(f'adding {numbers[i]} -> {sorted(numbers[:i + 1])}, '
              f'median is: {median}')
