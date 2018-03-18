class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = sorted(nums)

        if len(nums) == 1:
            if nums[0] == 0:
                return 1
            if nums[0] == 0:
                return 0
        c = 0
        for i in nums:
            if c != i:
                return c
            c = c + 1

        return c
