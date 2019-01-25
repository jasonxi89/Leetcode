class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    # """
    # @method 1
    # def strStr(self, source, target):
    #     return source.find(target)
    # @method 2



    def strStr(self, source, target):
        def compare(pointer, source, target):
            return source[pointer: pointer + len(target)] == target

        if source=="" or target =="":
            return -1
        if source == "" & target == "":
            return 0

        for pointer in range(0,len(source)):
            if source[pointer] == target[0]:
                if compare(pointer, source, target):
                    return pointer
        return -1




