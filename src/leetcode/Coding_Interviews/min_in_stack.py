# -*- coding: utf-8 -*-


class MinStack:

    def __init__(self):
        self.data = list()
        self.mins = list()


    def push(self, x: int) -> None:
        self.data.append(x)
        if not self.mins or self.mins[-1] >= x:
            self.mins.append(x)

    def pop(self) -> None:
        if self.data.pop() == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.data[-1]

    def min(self) -> int:
        return self.mins[-1]
        
