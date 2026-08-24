class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        k = 0
        for i in range(n):
            if( nums[i] != nums[k] ):
                nums[k+1],nums[i] = nums[i],nums[k+1]
                k+=1

        return k+1