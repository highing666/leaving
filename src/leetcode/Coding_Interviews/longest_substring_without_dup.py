# -*- coding: utf-8 -*-


class Solution:

    def length_of_longest_substring(self, s: str) -> int:
        dic = {}
        result = 0
        temp = 0
        for j in range(len(s)):
            i = dic.get(s[j], -1)
            dic[s[j]] = j
            if temp < j - i:
                temp += 1
            else:
                temp = j - i
            result = max(result, temp)
        
        return result


if __name__ == "__main__":
    test_solution = Solution()
    print(test_solution.length_of_longest_substring('abcabcbb'))
