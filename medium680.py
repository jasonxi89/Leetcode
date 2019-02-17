class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """
    def splitString(self, s):
        if len(s) == 0:
            return [[]]
        if len(s) == 1:
            return [[s]]
        result1 = self.splitString(s[1:])
        result2 = self.splitString(s[2:])
        result = []
        for r1 in result1:
            result.append([s[0]] + r1)
        for r2 in result2:
            print(r2)
            result.append([s[:2]] + r2)
        return result

if __name__ =="__main__":
    pass