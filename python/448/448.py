#!/usr/bin/env python

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #TODO: how to not use extra space?
        num_set = set(nums)
        return [key for key in range(1,len(nums)+1) if key not in num_set]

sol = Solution()
print sol.findDisappearedNumbers([4,3,2,7,8,2,3,1])
