from collections import deque

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false

    615. 课程表
    现在你总共有 n 门课需要选，记为 0 到 n - 1.
    一些课程在修之前需要先修另外的一些课程，比如要学习课程 0 你需要先学习课程 1 ，表示为[0,1]
    给定n门课以及他们的先决条件，判断是否可能完成所有课程？

    样例
    给定 n = 2，先决条件为 [[1,0]] 返回 true
    给定 n = 2，先决条件为 [[1,0],[0,1]] 返回 false
    [目标，先学]
    """

    def canFinish(self, numCourses, prerequisites):
        # Write your code here
        edges = {i: [] for i in range(numCourses)}
        degrees = [0 for i in range(numCourses)]
        for i, j in prerequisites:
            edges[j].append(i)
            degrees[i] += 1

        queue, count = deque([]), 0

        for i in range(numCourses):
            if degrees[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            count += 1

            for x in edges[node]:
                degrees[x] -= 1
                if degrees[x] == 0:
                    queue.append(x)

        return count == numCourses

