class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=len(nums1)-1
        
        while(i>=0):
             # Case 1: nums2 still has elements, and we compare
            if n > 0 and (m == 0 or nums2[n-1] >= nums1[m-1]):
                nums1[i] =  nums2[n-1]
                n-=1
            # Case 2: nums1 still has elements
            else:
                nums1[i] = nums1[m-1]
                m-=1
            
            i-=1
