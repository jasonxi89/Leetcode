class Solution:
    """
    @param A: an integer array
    @return: nothing
    464. 整数排序 II
    给一组整数，按照升序排序。使用归并排序，快速排序，堆排序或者任何其他 O(n log n) 的排序算法。
    快速排序：快速排序是由东尼·霍尔所发展的一种排序算法。其基本思想是基本思想是，通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的
    关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。


    样例
    例1：

    输入：[3,2,1,4,5]，
    输出：[1,2,3,4,5]。
    例2：

    输入：[2,3,1]，
    输出：[1,2,3]。
    """
    def sortIntegers2(A):
        # write your code here
        if len(A) <= 1:
            return A
        low = []
        high = []

        pivot = A.pop()
        for num in A:
            if num > pivot:
                high.append(num)
            else:
                low.append(num)



        return Solution.sortIntegers2(low) + [pivot] + Solution.sortIntegers2(high)

if __name__ == "__main__":
    print(Solution.sortIntegers2([3,2,1,4,5]))