class Solution:
    def canShip(self, weights, capacity):
        days = 1
        current = 0

        for weight in weights:
            if current + weight <= capacity:
                current += weight
            else:
                days +=1
                current = weight

        return days
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            requiredDays =  self.canShip(weights, mid)
            if requiredDays <= days:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans