class Solution:
    def asteroidCollision(self, arr):
        lists = arr.copy()
        i = 0

        while i < len(lists) - 1:

            if lists[i] > 0 and lists[i + 1] < 0:

                if lists[i] > -lists[i + 1]:
                    lists.pop(i + 1)

                elif lists[i] < -lists[i + 1]:
                    lists.pop(i)
                    if i > 0:
                        i -= 1

                else:
                    lists.pop(i + 1)
                    lists.pop(i)
                    if i > 0:
                        i -= 1

            else:
                i += 1

        return lists