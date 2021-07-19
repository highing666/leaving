# -*- codinng: utf-8 -*-

from typing import List, Tuple
from loguru import logger


class Solution:

    def __init__(self) -> None:
        self.total_result = []
        self.digits = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
        self.visited = []

    def read_binary_watch(self, turn_on: int) -> List[str]:
        self.total_result = []
        self.visited = [False for _ in range(len(self.digits))]
        self.dfs(turn_on, 0, 0)

        return self.total_result
    
    def dfs(self, turn_on: int, step: int, start: int):
        if turn_on == step:
            self.total_result.append(self.to_time_str())
            return
        
        for i in range(start, len(self.digits)):
            self.visited[i] = True
            if not self.is_time():
                self.visited[i] = False
                continue
            self.dfs(turn_on, step + 1, i + 1)
            self.visited[i] = False

    def calculate_time(self) -> Tuple[int, int]:
        hour_sum, minute_sum = 0, 0
        for i in range(len(self.visited)):
            if self.visited[i]:
                if i < 4:
                    hour_sum += self.digits[i]
                else:
                    minute_sum += self.digits[i]
        
        return hour_sum, minute_sum
    
    def is_time(self) -> bool:
        hour_sum, minute_sum = self.calculate_time()
        if 0 <= hour_sum <= 11 and 0 <= minute_sum <= 59:
            return True
        else:
            return False
    
    def to_time_str(self) -> str:
        hour_sum, minute_sum = self.calculate_time()
        time_str = '' + str(hour_sum) + ':'
        if minute_sum < 10:
            time_str += '0' + str(minute_sum)
        else:
            time_str += str(minute_sum)
        
        return time_str


if __name__ == '__main__':
    test_solution = Solution()
    res = test_solution.read_binary_watch(3)
    logger.debug(res)
