"""
https://leetcode.com/problems/redundant-connection/description/

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, with one additional edge added. The added edge has two different vertices chosen from `1` to `n`, and was not an edge that already existed. The graph is represented as an array `edges` of length `n` where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the graph.

Return an edge that can be removed so that the resulting graph is a tree of `n` nodes. If there are multiple answers, return the answer that occurs last in the input.

Example 1:
Graph:
        1 ---- 2
        |     /
        |    /
        |   /
        |  /
        | /
        3
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]



Example 2:
Graph:
        2 ---- 1 ---- 5
        |      |
        |      |
        |      |
        3 ---- 4
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]



Constraints:
* n == edges.length
* 3 <= n <= 1000
* edges[i].length == 2
* 1 <= ai < bi <= edges.length
* ai != bi
* There are no repeated edges.
* The given graph is connected.
"""


class Solution:
    def _is_connected(self, src, target, visited, adj_list):
        visited[src] = True

        if src == target:
            return True

        is_found = False
        for adj in adj_list[src]:
            if not visited[adj]:
                is_found = is_found or self._is_connected(
                    adj, target, visited, adj_list
                )

        return is_found

    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        N = len(edges)

        adj_list = [[] for _ in range(N)]

        for edge in edges:
            visited = [False] * N

            # If DFS returns True, we will return the edge.
            if self._is_connected(edge[0] - 1, edge[1] - 1, visited, adj_list):
                return edge

            adj_list[edge[0] - 1].append(edge[1] - 1)
            adj_list[edge[1] - 1].append(edge[0] - 1)

        return []
