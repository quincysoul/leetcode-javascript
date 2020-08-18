"""
Summary:
    Demo using zengtian006's code, displays the ranking system.
    Time Complexity: O(VE)
    Space Complexity: O(VE)
Trick:

Bibliography:https://github.com/zengtian006/LeetCode

Args:

"""


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        self.dic = collections.defaultdict(list)
        for u, v in connections:
            self.dic[u].append(v)
            self.dic[v].append(u)
        self.visit_time = [0] * n
        self.low = [0] * n
        visited = [0] * n
        idx = 0
        self.res = []
        self.dfs(0, None, idx, visited)

        # print(self.low)
        # print(self.ids)
        return self.res

    def dfs(self, cur, par, idx, visited):
        visited[cur] = 1
        self.visit_time[cur] = self.low[cur] = idx
        for nxt in self.dic[cur]:
            if nxt == par:
                continue
            if not visited[nxt]:
                self.dfs(nxt, cur, idx + 1, visited)
                self.low[cur] = min(self.low[cur], self.low[nxt])
                if self.low[nxt] > self.visit_time[cur]:
                    self.res.append([cur, nxt])
            elif visited[nxt]:
                self.low[cur] = min(self.low[cur], self.low[nxt])
