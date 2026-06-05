class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''O(n)
        m = nums[0]
        for x in nums:
            if x < m:
                m=x
        return m
        '''
        l,r = 0, len(nums)-1
        m=l#place
        while l<r:
            m=(l+r)//2
            #if middle is bigger than right, minimum must be on the right side
            if nums[m]>nums[r]:
                l=m+1
            #if middle is less than or equal to right, min must be on the left side including m
            else:
                r=m

        return nums[l]