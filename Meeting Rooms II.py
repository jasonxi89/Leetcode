# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from heapq import *
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x:x.start)
        h = []
        for interval in intervals:
            if not h:
                heappush(h, interval.end)
            else:
                earliest = heappop(h)
                if earliest <= interval.start:
                    heappush(h, interval.end)
                else:
                    heappush(h,earliest)
                    heappush(h,interval.end)
        return len(h)
#开始时间排序
#heapq记录结束时间
#如果有
