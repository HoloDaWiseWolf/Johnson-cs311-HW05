"""
Homework 5: The Top-K Countdown -- MinHeap.

Copy in your completed MinHeap class from Lab 10 (test_triage.py) --
insert, _sift_up, _sift_down, and extract_min all need to already
work correctly before you start heapify/find_k_largest in top_k.py.
"""

from typing import List


class MinHeap:
    """A binary min-heap backed by a flat Python list. Lower priority number = more critical."""

    def __init__(self) -> None:
        self._data: List[float] = []

    def __len__(self) -> int:
        return len(self._data)

    def insert(self, value: float) -> None:
        """Append `value`, then call _sift_up to restore the heap property."""
        # TODO
        self._data.append(value)
        self._sift_up(len(self._data)-1)
        #raise NotImplementedError

    def _sift_up(self, index: int) -> None:
        """
        Recursive. Perform at most one swap, then recurse toward the
        correct resting position. Do not use a while loop.
        """
        # TODO
        if index == 0:
            return
        parent = (index - 1) // 2
        parent_value = self._data[parent]
        child_value = self._data[index]
        if parent_value <= child_value:
            return 
        self._data[parent] = child_value
        self._data[index] = parent_value
        self._sift_up(parent)
        #raise NotImplementedError

    def _sift_down(self, index: int) -> None:
        """
        Recursive. Perform at most one swap, then recurse toward the
        correct resting position. Do not use a while loop.
        """
        # TODO
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index
        if left_child < len(self._data) and self._data[left_child] < self._data[smallest]:
            smallest = left_child
        if right_child < len(self._data) and self._data[right_child] < self._data[smallest]:
            smallest = right_child
        if smallest != index:
            self._data[index], self._data[smallest] = self._data[smallest], self._data[index]
            self._sift_down(smallest)
        #raise NotImplementedError

    def extract_min(self) -> float:
        """
        Remove and return the smallest (highest-priority) value.
        Move the last element to the root and call _sift_down.
        Correctly handle a heap with 0 or 1 elements.
        """
        # TODO
        _len = len(self._data)
        if _len == 0:
            raise ValueError()
        if _len == 1:
            return self._data.pop()
        old_root = self._data[0]
        self._data[0] = self._data.pop()
        self._sift_down(0)
        return old_root
        #raise NotImplementedError