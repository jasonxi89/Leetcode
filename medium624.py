from queue import Queue


class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    624. 移除子串
    给出一个字符串 s 以及 n 个子串。你可以从字符串 s 中移除 n 个子串中的任意一个，使得剩下来s的长度最小，输出这个最小长度。

    样例
    给出s = ccdaabcdbb，子串为 ["ab","cd"]
    返回 2.

    解释:
    ccdaabcdbb -> ccdacdbb -> cabb -> cb (长度为 2)
    """

    def minLength(self, s, dict):
        # Write your code here

        que = Queue.Queue()
        #que用来保存剩下的
        que.put(s)
        hash = set([s])
        min = len(s)


        while que != None:
            s = que.get()
            for sub in dict:
                found = s.find(sub)
                if found != -1:
                    new_s = s[:found] + s [found + len(sub)]
                    if new_s not in hash:
                        if len(new_s) < min:
                            min = len(new_s)
                        que.put(new_s)
                        hash.add(new_s)

                    found = s.find(sub, found + 1)




        return min
