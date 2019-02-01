"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
        618. 搜索图中节点
    给定一张 无向图，一个 节点 以及一个 目标值，返回距离这个节点最近 且 值为目标值的节点，如果不能找到则返回 NULL。
    在给出的参数中, 我们用 map 来存节点的值

    样例
    2------3  5
     \     |  |
      \    |  |
       \   |  |
        \  |  |
          1 --4
    给出 节点1，目标值为 50

    有个哈希表的值为[3,4,10,50,50]，表示:
    节点1的值为3
    节点2的值为4
    节点3的值为10
    节点4的值为50
    节点5的值为50

    返回 节点4
    注意事项
    保证答案唯一
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """
    def searchNode(self, graph, values, node, target):
        # write your code here
        #给定Node,找全部的neighbour，遍历，BFS
        if (graph is None) or (node is None):
            return ""
        from collections import deque
        que = deque([node])
        mark = set([])
        while que != None:
            node = que.popleft()
            if values[node] == target:
                return node
            for n in node.neighbors:
                if n in values:
                    if values[n] == target:
                        return n
                    mark.add(n)
                    que.append(n)

        return None