class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    28. Search a 2D Matrix
    Write an efficient algorithm that searches for a value in an m x n matrix.

    This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.
    样例
    样例  1:
    	输入: [[5]],2
    	输出: false

    	样例解释:
      没有包含，返回false。

    样例 2:
    	输入:
    [
      [1, 3, 5, 7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ],3
    	输出: true

    	样例解释:
    	包含则返回true。

    挑战
    O(log(n) + log(m)) 时间复杂度
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        line = -1
        #如果第一个小于target,就下一行
        for w in range(len(matrix)):
            if matrix[w][0] <= target:
                line = w
            else:
                break

        if line == -1:
            return False

        start , end = 0 , len(matrix[line]) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if matrix[line][mid] == target:
                return True
            if matrix[line][mid] < target:
                start = mid
            elif matrix[line][mid] > target:
                end = mid

        if matrix[line][start] == target or matrix[line][end] == target:
            return True

        return False


