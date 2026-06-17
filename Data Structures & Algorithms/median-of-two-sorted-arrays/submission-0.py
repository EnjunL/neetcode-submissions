class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2
        total = len(A) + len(B)
        half = total // 2

        #only run binary search on one of them ( A is our smaller arr )
        if len(B) < len(A):
            #swap if B < A
            A,B= B,A

        #binary search on smaller arr
        #half tells us the elements on the left partition
        l,r=0,len(A)-1
        #guarenteed to have median
        while True:
            i = (l+r)//2 # A
            j = half - i - 2 #why 2

            #check bounds
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if i+1 < len(A) else float("inf")
            Bleft = B[j] if j>= 0 else float("-inf")
            Bright =B[j+1] if j+1 < len(B) else float("inf")


            #left partition is correct
            if Aleft <= Bright and Bleft<=Aright:
                #odd
                if total % 2:
                    return min(Aright,Bright)
                #even
              #add left partition's max from both arr with min of right partition of both arr
                #divide via decimal to get median
                return (max(Aleft,Bleft) + min(Aright,Bright)) / 2
            
            #Aleft is too big, too many elements from A, reduce size of left partition from A
            elif Aleft > Bright:
                r = i-1

            #Bleft > Aright
            else:
                l = i+1


