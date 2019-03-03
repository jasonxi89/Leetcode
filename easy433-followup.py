from collections import deque
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer

    0/1组成的数组，找到0的矩阵 ，一定是tectangle
    """


    def numIslands(slef,grid):
        if not grid or not grid[0]:
            return None
        result =[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    left_top = [i,j]
                    x, y = i, j
                    while y + 1 < len(grid[0]) and grid[x][y+1] == 0:
                        grid[x][y + 1] = 1
                        y += 1
                    while x +1 < len(grid) and grid[x+1][y] == 0:
                        grid[x + 1][y] =1
                        x += 1
                    right_bot = [x,y]

                    Solution.helper(Solution, grid,left_top,right_bot)


                    result.append([left_top,right_bot])
        return result



    def helper(self, grid, left_top,right_bot):
        for i in range(left_top[0],right_bot[0]+1):
            for j in range(left_top[1],right_bot[1]+1):
                grid[i][j] =1



if __name__ =="__main__":
    print(Solution.numIslands(Solution,[[0,0,0],[0,0,0],[1,1,1],[0,0,0],[0,0,0]]))




