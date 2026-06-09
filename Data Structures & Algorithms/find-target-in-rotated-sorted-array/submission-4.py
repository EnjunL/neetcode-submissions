class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        m=1#ph
        while l <= r:#looking for target, not narrowing candidate range
            m=(l+r)//2
            if nums[m] == target:
                return m
            #only search the "sorted" half: 3,4,5 and 1,2

            if nums[l] <= nums[m]: #left half is sorted
                if nums[l] <= target < nums[m]:
                    #narrow down search space
                    r = m-1
                else: #move search space to the other side
                    l = m+1
            else: #right half is sorted
                if nums[m] < target <= nums[r]:
                    #narrow down search space
                    l=m+1
                else: #move search space to the other side
                    r = m-1
        return -1


                
            
