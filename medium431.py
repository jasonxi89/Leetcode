"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

        431. 找无向图的连通块
        找出无向图中所有的连通块。

        图中的每个节点包含一个label属性和一个邻接点的列表。（一个无向图的连通块是一个子图，其中任意两个顶点通过路径相连，且不与整个图中的其它顶点相连。）

        样例
        给定图:

        A------B  C
         \     |  |
          \    |  |
           \   |  |
            \  |  |
              D   E
        返回 {A,B,D}, {C,E}。其中有 2 个连通块，即{A,B,D}, {C,E}

        说明
        Learn more about representation of graphs

        注意事项
        每个连通块内部应该按照label属性排序

        #需要个set判断是不是路过， 遍历node点？neighbour写个queue来搞个顺序
"""

import collections

class Solution:
    """
    @param: nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    # def connectedSet(self, nodes):
    #     # write your code here
    #     visited = {}
    #     que = collections.deque([])
    #     result = []
    #     if not nodes:
    #         return nodes
    #
    #     for node in nodes:
    #         if node not in visited:
    #             que.append(node)
    #             visited[node] = True
    #             linked =[]
    #             while que:
    #                 curr = que.popleft()
    #                 linked.append(curr)
    #                 for neighbor in curr.neighbors:
    #                     #判断邻居走过没有，没走过加循环，走过就再见
    #                     if (neighbor not in visited):
    #                         que.append(neighbor)
    #                         visited.add(neighbor)
    #             result.append(linked)
    #     return result
    def connectedSet(self, nodes):
        # write your code here
        self.visited = {}

        for node in nodes:
            self.visited[node] = False

        res = []
        for node in nodes:
            if not self.visited[node]:
                tmp = []
                self.bfs(tmp, node)
                res.append(sorted(tmp))
        return res

    def dfs(self, tmp, node):
        self.visited[node] = True
        tmp.append(node.label)
        for neighbor in node.neighbors:
            if not self.visited[neighbor]:
                self.dfs(tmp, neighbor)

    def bfs(self, tmp, node):
        q = collections.deque([node])
        tmp.append(node.label)
        self.visited[node] = True
        while q:
            cur = q.popleft()
            for neighbor in cur.neighbors:
                if not self.visited[neighbor]:
                    q.append(neighbor)
                    tmp.append(neighbor.label)
                    self.visited[neighbor] = True




if __name__ =="__main__":
    Solution.connectedSet(Solution,nodes=123)