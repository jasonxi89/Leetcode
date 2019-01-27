class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    给一个升序的数组，以及一个target，找到它在数组中出现的次数。

    样例
    样例1：

    输入：[1,3,3,4,5]和target= 3，
    输出：2。
    样例2：

    输入：[2,2,3,4,6]和target= 4，
    输出：1。
    样例3：

    输入：[1,2,3,4,5]和target= 6，
    输出：0。
    挑战
    时间复杂度在O(logn)内
    """
    def helper(A, target):
        start = 0
        end = len(A)-1
        while start + 1 < end:
            mid = int( (start + end)/2 )
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                end = mid
            elif A[mid] < target:
                start = mid
            if A[start] == target:
                return start
            if A[end] == target:
                return end
        return -1


    def totalOccurrence(self, A, target):
        # write your code here
        if not A:
            return 0

        status = Solution.helper(A, target)

        if status == -1:
            return 0
        else:
            counter = 1
            left, right = status, status
            while left - 1 > -1 and A[left - 1] == target:
                counter += 1
                left -= 1
            while right + 1 < len(A) and A[right + 1] == target:
                counter += 1
                right += 1

        return counter


if __name__ == "__main__":
    A = [1,3,3,4,5]
    print(Solution.totalOccurrence(Solution,A,3))
