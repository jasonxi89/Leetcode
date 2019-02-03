"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
    434. 岛屿的个数II
    给定 n，m，分别代表一个2D矩阵的行数和列数，同时，给定一个大小为 k 的二元数组A。起初，2D矩阵的行数和列数均为 0，即该矩阵中只有海洋。
    二元数组有 k 个运算符，每个运算符有 2 个整数 A[i].x, A[i].y，你可通过改变矩阵网格中的A[i].x]，[A[i].y] 来将其由海洋改为岛屿。
    请在每次运算后，返回矩阵中岛屿的数量。

    样例
    给定 n = 3, m = 3， 二元数组 A = [(0,0),(0,1),(2,2),(2,1)].

    返回 [1,1,2,2].

    注意事项
    0 代表海，1 代表岛。如果两个1相邻，那么这两个1属于同一个岛。我们只考虑上下左右为相邻。
"""

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        # write your code here
        #好的 不会做
        pass
