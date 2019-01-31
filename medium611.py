"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
from collections import deque
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    611. 骑士的最短路线
    给定骑士在棋盘上的 初始 位置(一个2进制矩阵 0 表示空 1 表示有障碍物)，找到到达 终点 的最短路线，返回路线的长度。如果骑士不能到达则返回 -1 。

    样例
    [[0,0,0],
     [0,0,0],
     [0,0,0]]
     起点是 [2,0] 终点是 [2,2] 返回 2

    [[0,1,0],
     [0,0,0],
     [0,0,0]]
     起点是 [2,0] 终点是 [2,2] 返回 6

    [[0,1,0],
     [0,0,1],
     [0,0,0]]
     起点是 [2,0] 终点是 [2,2] 返回 -1
    说明
    如果骑士的位置为 (x,y)，他下一步可以到达以下这些位置:

    (x + 1, y + 2)
    (x + 1, y - 2)
    (x - 1, y + 2)
    (x - 1, y - 2)
    (x + 2, y + 1)
    (x + 2, y - 1)
    (x - 2, y + 1)
    (x - 2, y - 1)
    注意事项
    起点跟终点必定为空.
    骑士不能穿过障碍物.
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        def isvalid(grid, point):
            #合法的时候，x,y>=0,<len
            return 0 <= point.x < len(grid[0]) and 0 <= point.y < len(grid)

        if not grid or isvalid(grid,source):
            return None

        dirX = [+1, +1, -1, -1, +2, +2, -2, -2]
        dirY = [+2, -2, +2, -2, +1, -1, +1, -1]
        queen = deque[source]
        count = 0

        while not queen:
            level = []
            for point in queen:
                if point == destination:
                    return count
                for i in range(0,8):
                    adj = [point.x + dirX[i],
                           point.y + dirY[i]
                           ]
                    if isvalid(adj):
                        level.append(adj)
            count += 1
            queen = level
        return count -1

# 老师的方法，
#             for dx, dy in DIRECTIONS:
#                 next_x, next_y = x + dx, y + dy
#
# DIRECTIONS = [
#     (-2, -1), (-2, 1), (-1, 2), (1, 2),
#     (2, 1), (2, -1), (1, -2), (-1, -2),
# ]
#
#
# class Solution:
#     """
#     @param grid: a chessboard included 0 (false) and 1 (true)
#     @param source: a point
#     @param destination: a point
#     @return: the shortest path
#     """
#
#     def shortestPath(self, grid, source, destination):
#         queue = collections.deque([(source.x, source.y)])
#         distance = {(source.x, source.y): 0}
#
#         while queue:
#             x, y = queue.popleft()
#             if (x, y) == (destination.x, destination.y):
#                 return distance[(x, y)]
#             for dx, dy in DIRECTIONS:
#                 next_x, next_y = x + dx, y + dy
#                 if (next_x, next_y) in distance:
#                     continue
#                 if not self.is_valid(next_x, next_y, grid):
#                     continue
#                 distance[(next_x, next_y)] = distance[(x, y)] + 1
#                 queue.append((next_x, next_y))
#         return -1
#
#     def is_valid(self, x, y, grid):
#         n, m = len(grid), len(grid[0])
#
#         if x < 0 or x >= n or y < 0 or y >= m:
#             return False
#
#         return not grid[x][y]