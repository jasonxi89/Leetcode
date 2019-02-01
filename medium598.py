class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    598. 僵尸矩阵
    给一个二维网格，每一个格子都有一个值，2 代表墙，1 代表僵尸，0 代表人类(数字 0, 1, 2)。僵尸每天可以将上下左右最接近的人类感染成僵尸，但不能穿墙。
    将所有人类感染为僵尸需要多久，如果不能感染所有人则返回 -1。

    样例
    给一个矩阵：

    0 1 2 0 0
    1 0 0 2 1
    0 1 0 0 0
    返回 2
    """
    # def zombie(self, grid):
    #     # write your code here
    #     def isValid(grid, x, y):
    #         #判断能不能走，1.不是2，2.不超边界
    #         return (0 <= x < len(grid)) and (0 <= y < len(grid[0]) ) and (grid[x][y] != 2)
    #
    #     DIRECTION =[
    #         (0,1),(1,0),(0,-1),(-1,0)
    #     ]
    #
    #     count = 0
    #     last = []
    #     if not grid:
    #         return None
    #     while last != grid:
    #         last = grid
    #         for x in range(len(grid[0])):
    #             for y in range(len(grid)):
    #                 if grid[y][x] == 1:
    #                     for adjx,adjy in DIRECTION:
    #                         next_x = adjx + x
    #                         next_y = adjy +y
    #                         if isValid(grid,next_x,next_y):
    #                             grid[next_x][next_y] =1
    #         count +=1
    #         print(grid)
    #         if last ==grid:
    #             return -1
    #
    #     return count -1
# 想法对，但是细节处理不够，老师的方法是计数感染的人和墙，比直接比较2个数组靠谱
# class Solution:
#     # @param {int[][]} grid  a 2D integer grid
#     # @return {int} an integer
#
#     def zombie(self, grid):
#         # Write your code here
#         sum_zombie = 0
#         sum_wall = 0
#         n = len(grid)
#         m = len(grid[0])
#         qzombie = []
#         dx = [0,0,-1,1]
#         dy = [1,-1,0,0]
#
#         for i in xrange(n):
#             for j in xrange(m):
#                 if grid[i][j] == 1:
#                     qzombie.append([i,j,0])
#                     sum_zombie += 1
#                 elif grid[i][j] == 2:
#                     sum_wall += 1
#
#         step = 0
#         while qzombie:
#             p = qzombie.pop(0)
#             for i in xrange(4):
#                 x = p[0] + dx[i]
#                 y = p[1] + dy[i]
#                 if x < 0 or x >= n or y < 0 or y >= m:
#                     continue
#                 if grid[x][y] == 0:
#                     grid[x][y] = 1
#                     qzombie.append([x,y,p[2]+1])
#                     sum_zombie += 1
#             if not qzombie:
#                 step = p[2]
#         if sum_zombie + sum_wall != n * m:
#             return -1
#         else:
#             return step
if __name__ =="__main__":
    Solution.zombie(Solution,[[0,1,2,0,0],[1,0,0,2,1],[0,1,0,0,0]])

