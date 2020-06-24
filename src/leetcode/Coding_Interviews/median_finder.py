# -*- coding: utf-8 -*-

from heapq import heappush, heappushpop


class MedianFinder:

    def __init__(self):
        self.smaller = []
        self.bigger = []

    def addNum(self, num: int) -> None:
        if len(self.bigger) != len(self.smaller):
            heappush(self.smaller, -heappushpop(self.bigger, num))
        else:
            heappush(self.bigger, -heappushpop(self.smaller, -num))
    
    def findMedian(self) -> float:
        if len(self.bigger) != len(self.smaller):
            return self.bigger[0]
        else:
            return (self.bigger[0] - self.smaller[0]) / 2.0


if __name__ == "__main__":
    test_solution = MedianFinder()
    test_solution.addNum(1)
    test_solution.addNum(2)
    test_solution.addNum(3)
    print(test_solution.findMedian())
    test_solution.addNum(4)
    print(test_solution.findMedian())
