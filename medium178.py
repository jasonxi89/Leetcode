class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    178. 图是否是树
    给出 n 个节点，标号分别从 0 到 n - 1 并且给出一个 无向 边的列表 (给出每条边的两个顶点), 写一个函数去判断这张｀无向｀图是否是一棵树

    样例
    给出n = 5 并且 edges = [[0, 1], [0, 2], [0, 3], [1, 4]], 返回 true.

    给出n = 5 并且 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], 返回 false.

    注意事项
    你可以假设我们不会给出重复的边在边的列表当中. 无向边　[0, 1] 和 [1, 0]　是同一条边， 因此他们不会同时出现在我们给你的边的列表当中
    """
    # def validTree(self, n, edges):
    #     # write your code here
    #     # 判断入度是不是为1？如果为2就不是树？为0也不是
    #     dic = {n:0 for n in range(n)}
    #     for x,y in edges:
    #         if y in dic:
    #             return False
    #         dic[y] = 1
    #     for x in dic:
    #         if dic[x] ==0:
    #             return False
    #     return True
    # 本来想根据入度出度来算，但是挺傻逼的，因为没有方向性，一个点有三条边很正常。


# class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        if n - 1 != len(edges):
            return False

        self.father = {i: i for i in range(n)}
        self.size = n

        for a, b in edges:
            self.union(a, b)

        return self.size == 1

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.size -= 1
            self.father[root_a] = root_b

    def find(self, node):
        path = []
        while node != self.father[node]:
            path.append(node)
            node = self.father[node]

        for n in path:
            self.father[n] = node

        return node
    #试了几次，炸了，加强版看看吧