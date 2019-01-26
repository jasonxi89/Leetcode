class Solution:
    """
    @param a: The A array
    @param b: The B array
    @param s: The S string
    @return: The answer

    841. 字符串替换
    给定两个相同大小的字符串数组 A 和 B，再给一个字符串 S，所有出现在 S 里的子串 A 都要替换成 B。(注意：从左往右，能替换的必须替换，如果有多种替换方案，替换更长的优先。替换后的字符不能再做替换)

    样例
    给出 A = ["ab","aba"] , B = ["cc","ccc"] , S = "ababa" , 返回 "cccba"。

    按照规则，从左往右能替换的是“ab”或者“aba”,由于“aba”替换的更长，故将”aba”替换为”ccc”。
    给出 A = ["ab","aba"] , B = ["cc","ccc"] , S = "aaaaa" , 返回 "aaaaa"。

    S中没有包含A中的字符串，故不做替换。
    给出 A = ["cd","dab","ab"], B = ["cc","aaa","dd"], S = "cdab", 返回 "ccdd"。

    从左往右，最开始可以发现"cd"可以被替换，故替换后变成了"ccab",接下来可以发现"ab"可以被替换，故替换后的字符串为"ccdd"。
    注意事项
    每个字符串数组的大小不超过100,总字符串长度不超过50000。
    A[i] 和B[i]的长度相等。
    S的长度不超过50000。
    所有字符均为小写字母。
    保证A数组没有相同的字符串


    思路1：a里的排着找是不是在s，找出是否在字串，如果在，则判断长度
    """
    def stringReplace(a, b, s):
        import re
        # Write your code here
        #生成和a一样长度的数组
        a = ["ab", "aba"]
        b = ["cc", "ccc"]
        s = "ababa"
        #rec记录如果a在S里，存在的字符串的长度

        rec = [ 0 for _ in range(len(a))]

        #遍历a中的元素，如果找到了，就保存长度
        for num in range(0,len(a)):
            if s.find(a[num]) != -1:
                rec[num] = len(a[num])

        #遍历rec中的元素，找到最长的元素
        max = 0
        #recN记录最长的出现次数
        recN =[""]
        for num in range(0,len(a)):
            if rec[num] > max:
                max = rec[num]
                recN = [num]
            elif rec[num] == max:
                recN.append(num)
        #如果A的都不在，就直接返回S
        if max ==0:
            return s

        #while虚幻，全部替换
        # for num in range(len(recN)):
        #     while s.find(a[recN[num]]) != -1:
        #         print(s)
        #         print(a[recN[num]])
        #         print(b[recN[num]])
        #         s = s.replace(a[recN[num]], b[recN[num]])
        #
        # return s
        #考虑建1个标识符，如果替换个，来个标记，就再也不替换了
        # replaceable  = [True for _ in len(s)]
        # for num in range(len(recN)):
        #     while s.find(a[recN[num]]) != -1:
        #         recnum = s.find(a[recN[num]])
        #         for i in range(s.find(a[recN[num]]),s.find(a[recN[num]])+max):
        #             if replaceable[i] == False:
        #                 next()
        #         s = s.replace(a[recN[num]], b[recN[num]])
        #
        # return s
        #好像上一个想法也不太靠谱，不如这样，用原来的位置作比较，然后比较,本来想用切割做，但是会不会出现a是abc,bcd这种？切割也没用
        compare = s
        for num in range(len(recN)):
            while compare.find(a[recN[num]]) != -1:
                s = s[0:compare.find(a[recN[num]])] + s[compare.find(a[recN[num]]):].replace(a[recN[num]],b[recN[num]])
                compare = compare.replace(a[recN[num]], '1' * len(str(a[recN[num]])))
        return s



if __name__ == "__main__":
    print(Solution.stringReplace(1,2,3))