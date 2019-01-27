class TwoSum:
    """
    @param number: An integer
    @return: nothing
    607. 两数之和 III-数据结构设计
    设计并实现一个 TwoSum 类。他需要支持以下操作:add 和 find。
    add -把这个数添加到内部的数据结构。
    find -是否存在任意一对数字之和等于这个值

    样例
    add(1);add(3);add(5);
    find(4)//返回true
    find(7)//返回false
    """

    def __init__(self):
        # initialize your data structure here
        self.count = {}

    def add(self, number):
        # write your code here
        if number in self.count:
            self.count[number] += 1
        else:
            self.count[number] = 1

    """

    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        # write your code here
        for num in self.count:
            if value - num in self.count and (value - num != num or self.count[num] > 1):
                return True
        return False


if __name__ == "__main__":
    test  = TwoSum
    test.__init__(test)
    test.add(test,5)
    test.add(test,2)
    print(test.count)