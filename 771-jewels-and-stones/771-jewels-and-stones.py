class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewels_list = list(jewels)
        stones_list = list(stones)
        for stone in stones_list:
            if stone in jewels_list:
                count += 1
        return count 
        