class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        #Find Peak 
        #check m, then go left or right parition
        #example arr Peak=4  [1,2,3, 4 ,3,2,1]
        length = mountainArr.length()
        l,r = 0, length-1
        res = float("inf")

        #Find Peak
        while l<r:
            m = (l+r)//2
            mVal = mountainArr.get(m)
            
            #increasing side
            if mVal < mountainArr.get(m+1):
                l = m+1
            #decreasing side
            else:
                r=m
        
        #peak is at r
        #check left first
        peak = r
        l=0
        while l<=r:
            m = (l+r)//2
            mVal = mountainArr.get(m)

            if mVal == target:
                return m
            elif mVal > target:
                r = m-1
            else:
                l = m+1
        #check right is res
        if res == float("inf"):
            l,r=peak+1,length-1
            while l<=r:
                m = (l+r)//2
                mVal = mountainArr.get(m)

                if mVal == target:
                    return m
                elif mVal < target:
                    r = m-1
                else:
                    l=m+1
        return -1


