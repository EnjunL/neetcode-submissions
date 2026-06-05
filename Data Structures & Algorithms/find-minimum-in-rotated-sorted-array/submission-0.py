class Solution:
    def findMin(self, nums: List[int]) -> int:
        #O(n)
        m = nums[0]
        for x in nums:
            if x < m:
                m=x
        return m