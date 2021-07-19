# -*- coding: utf-8 -*-

from bisect import bisect_right, insort

class Solution:
	
	def solve(self, nums):
		d = list()
		ans = 0

		for num in nums:
			i = bisect_right(d, num * 3)
			ans += len(d) - i
			insort(d, num)
		
		return ans
