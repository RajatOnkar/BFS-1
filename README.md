# BFS-1
# Problem 1
Binary Tree Level Order Traversal (https://leetcode.com/problems/binary-tree-level-order-traversal/)

# Initialize a list to store the list of elements at each level and a stack to iterate the elements. If 
# root is 'Null' then we return an empty list (edge case).
# Implement a First IN First OUT stack which will ensure the nodes at each level are accumulated. 
# We start with the root node, pop and store in a temp list and then gather left and right nodes. Iterate
# over the size of this temp list so that all the level elements are returned.
# Return the result list which contains lists at each level. 

# Problem 2
Course Schedule (https://leetcode.com/problems/course-schedule/)

# Edge case - check for prerequisites, if empty return True
# Iterate over the courses and store courses in an array with its prerequisite count and 
# course & corresponding prerequisutes in a map.
# Start with the independent courses and get "All" courses as all independent courses should be 
# completed.
# Once the prerequisites are complete we decrement the count of the dependent courses until we go over
# all the courses.
# If the course array still has an element with count - all courses cannot be finished ELSE all courses
# can be finished.

