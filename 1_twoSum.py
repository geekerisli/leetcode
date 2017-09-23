#Leetcode is very good, I've tried different version of code
#first I used nested loop, but leetcode just crush my code with a huge array
#Next, I readlly appreciate  Nathan_Fegard's great idea of using hash

class Solution(object):
	def twoSum(self, nums, target):
		if len(nums) < 1:
			return False       
		if len(nums) == 2:
			return[0,1]
		bu_dict = {}       
		for i in range(len(nums)):
			if nums[i] in bu_dict:
				return[bu_dict[nums[i]],i]
			else:
				bu_dict[target-nums[i]] = i
