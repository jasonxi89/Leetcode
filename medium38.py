class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    38. 搜索二维矩阵 II
    写出一个高效的算法来搜索m×n矩阵中的值，返回这个值出现的次数。

    这个矩阵具有以下特性：

    每行中的整数从左到右是排序的。
    每一列的整数从上到下是排序的。
    在每一行或每一列中没有重复的整数。
    样例
    考虑下列矩阵：

    [

        [1, 3, 5, 7],

        [2, 4, 7, 8],

        [3, 5, 9, 10]

    ]

    给出target = 3，返回 2

    挑战
    要求O(m+n) 时间复杂度和O(1) 额外空间
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix:
            return 0

        def helper(A, target):
            start, end = 0, len(A) -1
            while start + 1 < end:
                mid = (start + end) // 2
                if A[mid] == target:
                    return 1
                elif A[mid] < target:
                    start = mid
                elif A[mid] > target:
                    end = mid
            return 0


        count = 0
        print(matrix[0])
        length = len(matrix[0]) -1
        for n in range(0,len(matrix)):
            if matrix[n][0] == target or matrix[n][length] == target:
                count +=1
            elif matrix[n][0] < target or matrix[n][length] > target:
                count +=helper(matrix[n],target)
        return count


if __name__ == "__main__":
    print(Solution.searchMatrix(Solution,[[3,4]],3))

