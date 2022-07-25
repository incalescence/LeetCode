class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
 
        list_1 = []
        for num in nums1:
            if num in list_1:
                continue
            if num not in nums2:
                list_1.append(num)
        list_2 = []
        for num in nums2:
            if num in list_2:
                continue
            if num not in nums1:
                list_2.append(num)
        return [list_1,list_2]