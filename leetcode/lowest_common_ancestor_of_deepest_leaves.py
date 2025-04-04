'''
Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

    The node of a binary tree is a leaf if and only if it has no children
    The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
    The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest leaf-nodes of the tree.
Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of nodes 7 and 4 is 3.

Example 2:

Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree, and it's the lca of itself.

Example 3:

Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest leaf node in the tree is 2, the lca of one node is itself.
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return 0, None
            left = dfs(root.left)
            right = dfs(root.right)
            if left[0] > right[0]:
                return left[0] + 1, left[1]
            if left[0] < right[0]:
                return right[0] + 1, right[1]
            return left[0] + 1, root
        return dfs(root)[1]

# ---------- Test Case 1 ----------
# Input: root = [1]
# Expected Output: [1]
root1 = TreeNode(1)
sol = Solution()
result1 = sol.lcaDeepestLeaves(root1)
print("Input: root = [1]")
print("Output:", [result1.val])  # [1]

# ---------- Test Case 2 ----------
# Input: root = [0,1,3,null,2]
# Tree:
#       0
#      / \
#     1   3
#      \
#       2
# Expected Output: [2]
root2 = TreeNode(0)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(2)
result2 = sol.lcaDeepestLeaves(root2)
print("\nInput: root = [0,1,3,null,2]")
print("Output:", [result2.val])  # [2]

# ---------- Test Case 3 ----------
# Input: root = [3,5,1,6,2,0,8,null,null,7,4]
# Expected Output: [2]
root3 = TreeNode(3)
root3.left = TreeNode(5)
root3.right = TreeNode(1)
root3.left.left = TreeNode(6)
root3.left.right = TreeNode(2)
root3.right.left = TreeNode(0)
root3.right.right = TreeNode(8)
root3.left.right.left = TreeNode(7)
root3.left.right.right = TreeNode(4)
result3 = sol.lcaDeepestLeaves(root3)
print("\nInput: root = [3,5,1,6,2,0,8,null,null,7,4]")
print("Output:", [result3.val])  # [2]