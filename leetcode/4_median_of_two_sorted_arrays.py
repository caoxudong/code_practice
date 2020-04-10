"""
https://leetcode.com/problems/median-of-two-sorted-arrays/

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lengthOfArray1 = len(nums1)
        indexOfArray1 = 0
        tempNumOfArray1 = 0
        lengthOfArray2 = len(nums2)
        indexOfArray2 = 0
        tempNumOfArray2 = 0
        newNums = []
        lengthOfAllNums = lengthOfArray1 + lengthOfArray2

        while (indexOfArray1 < lengthOfArray1) or (indexOfArray2 < lengthOfArray2) :
            if indexOfArray1 < lengthOfArray1 :
                tempNumOfArray1 = nums1[indexOfArray1]
            else :
                tempNumOfArray1 = None
            if indexOfArray2 < lengthOfArray2 :
                tempNumOfArray2 = nums2[indexOfArray2]
            else : 
                tempNumOfArray2 = None

            if tempNumOfArray1 is None :
                indexOfArray2 += 1
                newNums.append(tempNumOfArray2)
            else :
                if tempNumOfArray2 is None :
                    indexOfArray1 += 1
                    newNums.append(tempNumOfArray1)
                else :
                    if tempNumOfArray1 < tempNumOfArray2 :
                        indexOfArray1 += 1
                        newNums.append(tempNumOfArray1)
                    else :
                        indexOfArray2 += 1
                        newNums.append(tempNumOfArray2)
        
        if lengthOfAllNums & 1 :
            targetIndex = lengthOfAllNums >> 1
            return float(newNums[targetIndex])
        else :
            targetIndex = lengthOfAllNums >> 1
            return (float(newNums[targetIndex - 1] + newNums[targetIndex]) / 2)

if __name__ == '__main__' :
    obj = Solution()
    nums = [
        [[1,3], [2]], 
        [[1,2,3,4],[5,6,7,8]],
        [[1,3,5,7,9],[0,2,4,6,8]],
        [[3,6,7], [1,7,9]],
        [[1,2], [3,4]]
        ]
    for e in nums:
        print(obj.findMedianSortedArrays(e[0], e[1]))
