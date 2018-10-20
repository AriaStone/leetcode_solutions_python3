
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if (m + n) % 2 == 1:
            mid_left = (m + n - 1) // 2
            mid_right = mid_left
        else:
            mid_left = (m + n) // 2 - 1
            mid_right = (m + n) // 2
            
        num = []
        pointer1 = 0
        pointer2 = 0
        while len(num) <= mid_right:
            if pointer1 ==m and pointer2 == n:
                break
                
            elif pointer1 == m:
                num.append(nums2[pointer2])
                pointer2 += 1
                continue
            elif pointer2 == n:
                num.append(nums1[pointer1])
                pointer1 += 1
                continue
            
            if nums1[pointer1] < nums2[pointer2]:
                num.append(nums1[pointer1])
                pointer1 += 1
            else:
                num.append(nums2[pointer2])
                pointer2 += 1
            
        return (num[mid_left] + num[mid_right])/2