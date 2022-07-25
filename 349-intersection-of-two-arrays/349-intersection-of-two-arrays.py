class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        new_list = []
        for num in nums1:
            if num in new_list:
                continue
            if num in nums2:
                new_list.append(num)
                nums2.remove(num)
        return new_list
        