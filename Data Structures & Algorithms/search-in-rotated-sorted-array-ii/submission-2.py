class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,r = 0,len(nums)-1

        while l<=r:
            m=(l+r)//2

            if nums[m] == target:
                return True
            if nums[m] == nums[l]:
                l+=1
            #left is sorted:
            elif nums[l] < nums[m]:
                #check if target is within the range
                if nums[l] <= target < nums[m]:
                    #if so, move right border before m
                    r = m-1
                else:
                    #if not, move to the right portion
                    l=m+1
            #right is sorted:
            else :#nums[r] > nums[m]:
                #check if target is within the range
                if nums[m] < target <= nums[r]:
                    #if so, move left border to one after m
                    l = m+1
                else:
                    #if not, move to the left portion
                    r=m-1
                
        return False