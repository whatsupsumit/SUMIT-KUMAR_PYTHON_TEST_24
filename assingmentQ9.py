class Solution(object):
	def twoSum(self, nums, target):
		mapping = {}

		for index, val in enumerate(nums):
			difference = target - val
			if difference in mapping:
				return [mapping[difference], index]
			else:
				mapping[val] = index

s = Solution()
print(s.twoSum([2,7,11,15], 9))