"""
Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
        531. 六度问题
        六度分离是一个哲学问题，说的是每个人每个东西可以通过六步或者更少的步数建立联系。

        现在给你一个友谊关系，查询两个人可以通过几步相连，如果不相连返回 -1

        样例
        给出图

        1------2-----4
         \          /
          \        /
           \--3--/
        {1,2,3#2,1,4#3,1,4#4,2,3} s = 1, t = 4 返回 2

        给出图二


        1      2-----4
                     /
                   /
                  3
        {1#2,4#3,4#4,2,3} s = 1, t = 4 返回 -1
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """
    def sixDegrees(self, graph, s, t):
        # write your code here
        from collections import deque
        que = deque([s])
        d = {}
        d[s] = 0
        #while que:就是不为空，就和if not s一样
        while que:
            curr = que.popleft()
            if curr ==t:
                return d[curr]
            for node in curr.neighbors:
                if node not in d:
                    d[node] = d[curr] +1
                    que.append(node)
        return -1

