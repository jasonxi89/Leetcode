class Solution:
    """
    @param array: an integer array
    @return: nothing
    894. 烙饼排序
    给一个 无序数组，对其排序。只能对数组执行以下操作。

    flip(arr, i): 翻转数组中下标从 0 到 i 的元素
    与传统的排序算法不同，传统的排序算法试图以尽可能少的比较进行排序。我们的目标是用尽可能少的翻转来实现排序。

    样例
    给出 array = [6, 7, 10, 11, 12, 20, 23]
    使用 flip(arr, i) 方法来对数组进行排序

    注意事项
    只能调用flip函数。
    不允许使用任何排序函数或其他排序方法。

    Java：可以调用 FlipTool.flip(arr, i)
    C++： 可以调用 FlipTool::flip(arr, i)
    Python2&3：可以调用 FlipTool.flip(arr, i)
    思路是循环排序，把最小的丢左边？然后i-1
    """
    def pancakeSort(self, array):
        for target in range(len(array) - 1, 0, -1):
            for i in range(target, 0, -1):
                if array[i] > array[0]:
                    FlipTool.flip(array, i)

            FlipTool.flip(array, target)

