from collections import deque

class Solution:
    def findMaxPathScore(self, edges, online, k):
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n
        costs = []

        for u, v, w in edges:
            graph[u].append((v, w))
            indegree[v] += 1
            costs.append(w)

        # Topological Order
        q = deque()
        topo = []

        deg = indegree[:]
        for i in range(n):
            if deg[i] == 0:
                q.append(i)

        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in graph[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    q.append(v)

        if not costs:
            return -1

        values = sorted(set(costs))

        def check(limit):
            INF = float('inf')
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, w in graph[u]:

                    if w < limit:
                        continue

                    if v != n - 1 and not online[v]:
                        continue

                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w

            return dist[n - 1] <= k

        left = 0
        right = len(values) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if check(values[mid]):
                ans = values[mid]
                left = mid + 1
            else:
                right = mid - 1

        return ans