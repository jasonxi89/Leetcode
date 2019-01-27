class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    61. 搜索区间
    给定一个包含 n 个整数的排序数组，找出给定目标值 target 的起始和结束位置。

    如果目标值不在数组中，则返回[-1, -1]

    样例
    给出[5, 7, 7, 8, 8, 10]和目标值target=8,

    返回[3, 4]

    挑战
    时间复杂度 O(log n)
    """
    def searchRange(self, A, target):
        # write your code here
        if (not A) or target > A[len(A) - 1] or target < A[0]:
            return [-1,-1]
        start, end = 0, len(A) - 1
        pos = None
        while start + 1 < end:
            mid = (start + end) // 2
            print(A[mid])
            if A[mid] == target:
                pos = mid
                break
            elif A[mid] < target:
                start = mid
            elif A[mid] > target:
                end = mid

        if pos != None:
            start , end = pos, pos
            while (start > -1 and A[start] == target):
                start -= 1
            while  (end < len(A) and A[end] == target):
                end += 1
            return [start + 1,end -1]

        if A[start] == target:
            return [start,start]
        if A[end] == target:
            return [end,end]
        return [-1,-1]


if __name__ == "__main__":
    print(Solution.searchRange(Solution,[9,10,100,101,1002,10203],10203))