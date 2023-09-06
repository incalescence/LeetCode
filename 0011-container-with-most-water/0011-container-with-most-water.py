class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_index = volume = 0 
        right_index = len(height)-1
        while left_index < right_index:
            if height[left_index] < height[right_index]:
                volume = max(volume, (right_index-left_index)*height[left_index])
                left_index += 1
            else:
                volume = max(volume, (right_index-left_index)*height[right_index])
                right_index -= 1
        return volume