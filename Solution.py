'''
// Time Complexity :
Problem 1: O(n) as we traverse the entire tree
Problem 2: O(courses + prerequisites) = O(v + e) to iterate over courses and prerequisites
// Space Complexity :
Problem 1: O(n) as we store all the tree elements
Problem 2: O(courses + prerequisites) = O(v + e) as we store both the courses and prerequisites
// Did this code successfully run on Leetcode :
Yes the code ran successfully.
// Any problem you faced while coding this :

// Your code here along with comments explaining your approach
'''
## Problem 1 - Binary Tree Level Order Traversal
# Initialize a list to store the list of elements at each level and a stack to iterate the elements. If 
# root is 'Null' then we return an empty list (edge case).
# Implement a First IN First OUT stack which will ensure the nodes at each level are accumulated. 
# We start with the root node, pop and store in a temp list and then gather left and right nodes. Iterate
# over the size of this temp list so that all the level elements are returned.
# Return the result list which contains lists at each level. 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        result = []

        if root == None: return result
        queue1 = deque([root])

        while(len(queue1) > 0):
            size = len(queue1)
            li = []
            for i in range(size):
                element = queue1.popleft()
                li.append(element.val)
                if element.left != None:
                    queue1.append(element.left)
                if element.right != None:
                    queue1.append(element.right)
            result.append(li)
        return result  

## Problem 2 - Course Schedule
# Edge case - check for prerequisites, if empty return True
# Iterate over the courses and store courses in an array with its prerequisite count and 
# course & corresponding prerequisutes in a map.
# Start with the independent courses and get "All" courses as all independent courses should be 
# completed.
# Once the prerequisites are complete we decrement the count of the dependent courses until we go over
# all the courses.
# If the course array still has an element with count - all courses cannot be finished ELSE all courses
# can be finished.

from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if prerequisites == 0 or len(prerequisites) == 0: return True
        indegree = [0 for i in range(numCourses)]
        map1 = { i : [] for i in range(numCourses) }
        # Iterate over the array and store courses in an array and course & prerequisute in a map
        for i in prerequisites:
            indegree[i[0]] += 1
            map1[i[1]].append(i[0])
        # Store the courses in a queue starting with independent courses
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        # Now we go over the dependent courses
        while len(queue) > 0:
            ccourse = queue.popleft()
            # Decrement the value of the dependent courses
            for c in map1[ccourse]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    queue.append(c)
        # If the queue is empty and the indegree is zero - All courses can be finished
        for c in range(numCourses):
            if indegree[c] != 0:
                return False
        return True