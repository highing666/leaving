# -*- coding: utf-8 -*-


class Solution:

    @staticmethod
    def reverse_words(s: str) -> str:
        words = s.split(' ')
        result = ''
        temp = []
        for word in words:
            if word:
                temp.append(word)

        while temp:
            result += temp.pop()
            result += ' '

        return result[:-1]


if __name__ == '__main__':
    test_solution = Solution()
    print(test_solution.reverse_words('I am not, a    student.'))
