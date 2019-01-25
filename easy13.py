class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        if source == "" or target == "":
            return -1
        count = 0
        while True:
            if source.find(target[0]) == -1:
                return count
            count += source.find(target[0])
            if source[source.find(target[0]):source.find(target[0])+len(target)] == target:
                return count
            source = source[source.find(target[0])+1:]





