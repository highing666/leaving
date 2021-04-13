# -*- coding: utf-8 -*-

class MyQueue:

    def __init__(self):
        self.stk_a = []
        self.stk_b = []

    def push(self, x: int) -> None:
        for i in range(len(self.stk_a)):
            tmp = self.stk_a.pop()
            self.stk_b.append(tmp)
            i += 1
        self.stk_a.append(x)

        for j in range(len(self.stk_b)):
            tmp = self.stk_b.pop()
            self.stk_a.append(tmp)
            j += 1

    def pop(self) -> int:
        return self.stk_a.pop()

    def peek(self) -> int:
        return self.stk_a[-1]

    def empty(self) -> bool:
        return True if len(self.stk_a) == 0 else False


if __name__ == '__main__':
    obj = MyQueue()
    obj.push(3)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
