import math

class Solution:
    def minEatingSpeed(self, piles, h):

        low = 1
        high = max(piles)

        ans = high

        while low <= high:

            mid = (low + high) // 2

            hours = 0

            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours <= h:
                ans = mid
                high = mid - 1

            else:
                low = mid + 1

        return ans