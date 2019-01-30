class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    433. 岛屿的个数
    给一个01矩阵，求不同的岛屿的个数。

    0代表海，1代表岛，如果两个1相邻，那么这两个1属于同一个岛。我们只考虑上下左右为相邻。

    样例
    在矩阵：

    [
      [1, 1, 0, 0, 0],
      [0, 1, 0, 0, 1],
      [0, 0, 0, 1, 1],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 1]
    ]
    中有 3 个岛.
    """
    def numIslands(self, grid):
        # write your code here
        counter = 0
        def valpoint(grid,m,n):
            return m < len(grid) and n < len(grid[0]) and m > -1 and n > -1


        def helper(grid,m,n):
            if valpoint(grid,m,n) != True or (grid [m][n] == 0) :
                return
            else:
                grid [m][n] = 0
                print("m,n被改了",m,n)
                helper(grid, m + 1, n)
                helper(grid, m - 1, n)
                helper(grid, m, n + 1)
                helper(grid, m, n - 1)

        def printer(grid):
            for m in range(len(grid)):
                print(grid[m])
            print("")



        for m  in range(len(grid)):
            for n in range(len(grid[0])):
                print(m,n,grid[m][n])
                if grid[m][n] == 1:
                    printer(grid)
                    print("我在坐标",m,n,"停下来了")
                    counter += 1
                    helper(grid,m,n)

        return counter

        # from collections import deque
        #
        # class Solution:
        #     """
        #     @param grid: a boolean 2D matrix
        #     @return: an integer
        #     """
        #     def numIslands(self, grid):
        #         if not grid or not grid[0]:
        #             return 0
        #
        #         islands = 0
        #         for i in range(len(grid)):
        #             for j in range(len(grid[0])):
        #                 if grid[i][j]:
        #                     self.bfs(grid, i, j)
        #                     islands += 1
        #
        #         return islands
        #     ###BFS没写出来，写的递归贼傻逼，但是BFS简单很多，先把这个点改成0，
        #     def bfs(self, grid, x, y):
        #         queue = deque([(x, y)])
        #         grid[x][y] = False
        #         while queue:
        #             x, y = queue.popleft()
        #             for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
        #                 next_x = x + delta_x
        #                 next_y = y + delta_y
        #                 if not self.is_valid(grid, next_x, next_y):
        #                     continue
        #                 queue.append((next_x, next_y))
        #                 grid[next_x][next_y] = False
        #
        #     def is_valid(self, grid, x, y):
        #         n, m = len(grid), len(grid[0])
        #         return 0 <= x < n and 0 <= y < m and grid[x][y]


if __name__ =="__main__":
    print(Solution.numIslands(Solution,[[0,1,0],[1,0,1],[0,1,0]]))




