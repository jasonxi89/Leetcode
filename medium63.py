class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean
    63. 搜索旋转排序数组 II
    跟进“搜索旋转排序数组”，假如有重复元素又将如何？

    是否会影响运行时间复杂度？

    如何影响？

    为何会影响？

    写出一个函数判断给定的目标值是否出现在数组中。

    样例
    给出[3,4,4,5,7,0,1,2]和target=4，返回 true
    做错了2次，对于最后选哪段在傻逼，一开始一直在比较转折点和target大小，但是应该比较A[0]和target的值
    """

    def search(self, A, target):
        # write your code here
        if not A:
            return False
        start, end = 0, len(A) - 1
        while start < end:
            mid = (start + end) // 2
            if A[mid] > A[end]:
                start = mid + 1
            elif A[mid] < A[end]:
                end = mid
            else:
                end = end - 1
        print("转折点是",end)

        def helper(A, tartget, startpos, endpos):
            start, end = startpos, endpos
            while start + 1 < end:
                mid = (start + end) // 2
                if A[mid] == target:
                    return True
                elif A[mid] > target:
                    end = mid
                elif A[mid] < target:
                    start = mid
            return (A[start] == target) or (A[end] == target)


        if target >= A[0]:
            return helper(A, target, 0, end - 1)
        else:
            return helper(A, target, end, len(A) - 1)


if __name__ == "__main__":
    # print(Solution.search(Solution,[9,5,6,7,8,9,9,9,9,9,9],8)
    print(Solution.search(Solution,[4,4,4,5,1,4],5))
