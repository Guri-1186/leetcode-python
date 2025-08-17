class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    
        num_dict = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in num_dict:
                return [num_dict[difference], index]
            num_dict[num] = index