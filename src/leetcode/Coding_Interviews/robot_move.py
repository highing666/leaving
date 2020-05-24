# -*- coding: utf-8 -*-


class Solution:

    def moving_count(self, m: int, n: int, k: int) -> int:
        if m <= 0 or n <= 0 or k < 0:
            return 0
        visited = [None] * m * n

        return self.moving_count_core(m, n, k, 0, 0, visited)

    def moving_count_core(self, m, n, k, i, j, visited):
        count = 0
        if self.check(m, n, k, i, j, visited):
            visited[i * n + j] = True
            count = (1 + self.moving_count_core(m, n, k, i, j - 1, visited)
                     + self.moving_count_core(m, n, k, i - 1, j, visited)
                     + self.moving_count_core(m, n, k, i, j + 1, visited)
                     + self.moving_count_core(m, n, k, i + 1, j, visited))

        return count

    def check(self, m, n, k, i, j, visited):
        if (0 <= i < m and 0 <= j < n
                and self.get_digit_sum(i) + self.get_digit_sum(j) <= k
                and not visited[i * n + j]):
            return True

        return False

    @staticmethod
    def get_digit_sum(n):
        sums = 0
        while n > 0:
            sums += n % 10
            n //= 10

        return sums


if __name__ == "__main__":
    test_solution = Solution()
    a, b, c = 3, 1, 0
    print(test_solution.moving_count(a, b, c))
