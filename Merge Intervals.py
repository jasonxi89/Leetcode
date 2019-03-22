# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        intervals.sort(key = lambda x:x.start)
        merge =[]
        for interval in intervals:
            if not merge or merge[-1].end < inverval.start:
                merge.append(interval)
            else:
                merge[-1].end = max(merge[-1].end, interval.end)

        return merge
