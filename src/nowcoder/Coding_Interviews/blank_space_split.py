# -*- coding -*-

class Solution:

    def __init__(self):
        super().__init__()
    
    def replace_space(self, s):
        result_s = r''
        for item in s:
            if item == ' ':
                result_s += '%20'
            else:
                result_s += item
        
        return result_s


if __name__ == "__main__":
    test_s = 'We Are Happy'
    test_solution = Solution()
    print(test_solution.replace_space(test_s))
