class Solution:

    def possible(self, bloomDay, day, m, k):

        flowers = 0
        bouquets = 0

        for bloom in bloomDay:

            if bloom <= day:
                flowers += 1

                if flowers == k:
                    bouquets += 1
                    flowers = 0

            else:
                flowers = 0

        return bouquets >= m


    def minDays(self, bloomDay, m, k):

        if m * k > len(bloomDay):
            return -1

        low = min(bloomDay)
        high = max(bloomDay)

        ans = -1

        while low <= high:

            mid = (low + high) // 2

            if self.possible(bloomDay, mid, m, k):

                ans = mid
                high = mid - 1

            else:
                low = mid + 1

        return ans