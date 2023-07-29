class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        counter = 0
        for stone in stones:
            if stone in jewel_set:
                counter += 1
        return counter
        