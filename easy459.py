class Solution:
    """
    @param A: an integer array sorted in ascending order
    @param target: An integer
    @return: an integer

    459. 排序数组中最接近元素
    在一个排好序的数组 A 中找到 i 使得 A[i] 最接近 target

    样例
    样例1：

    输入：[1, 2, 3] ，target = 2
    输出： 1.
    样例2：

    输入：[1, 4, 6]， target = 3
    输出： 1.
    样例3：

    输入：[1, 4, 6]，target = 5,
    输出： 1 或 2.
    挑战
    O(logn)时间复杂度。

    注意事项
    数组中可以有重复的元素，可以返回任何具有相同值的下标。
    """
    def closestNumber(self, A, target):
        # write your code here
        if not A:
            return -1

        start, end = 0, len(A) -1

        while start + 1 < end:
            mid = int((start + end) / 2 )
            if A[mid] == target:
                return mid
            if A[mid] < target:
                start = mid
            if A[mid] > target:
                end = mid

        if target - A[start] < A[end] - target:
            return start
        else:
            return end


if __name__ =="__main__":
    A = [1,4,8,12,16,28,38]
    print(Solution.closestNumber(Solution, A, 1))
