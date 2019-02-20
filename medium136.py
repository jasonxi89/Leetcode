class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        results = []
        self.dfs(s,[],results)
        return results


    def dfs(self, s, stringlist, results):
        if len(s) == 0:
            # 深度copy stringlist
            results.append(list(stringlist))
            return
        for i in range(1, len(s)+1):
            prefix = s[:i]
            if self.is_pali(prefix):
                stringlist.append(prefix)
                self.dfs(s,stringlist,results)
                stringlist.pop()



    def is_pali(self,s):
        return s == s[::-1]


