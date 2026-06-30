class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #ptr1 store cur val
        #ptr2 move ahead and check

        slow=0
        fast=0

        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow == fast:
                break
        
        slowstart=0
        while True:
            slow=nums[slow]
            slowstart=nums[slowstart]
            if slow==slowstart:
                break 
        return slow