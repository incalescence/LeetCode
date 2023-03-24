# Remember, all submissions are being checked for plagiarism.
# Your recruiter will be informed in case suspicious activity is detected.

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(blocks):
    max_difference = 0
    for i in range(len(blocks)):
        # move one frog to the most left position possible and move the other frog to the most right position posible
        left = i 
        while left > 0 and blocks[left - 1] >= blocks[left]:
            left -= 1
        right = i
        while right < len(blocks) -1 and blocks[right + 1] >= blocks[right]:
            right += 1
        max_difference = max(max_difference, right - left + 1)
    return max_difference 
