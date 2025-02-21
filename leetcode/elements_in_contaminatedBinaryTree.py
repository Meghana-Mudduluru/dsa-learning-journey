# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class FindElements:
    def __init__(self, root: TreeNode):
        self.seen = set()
        self.recover_tree(root)

    def find(self, target: int) -> bool:
        return target in self.seen

    def recover_tree(self, root):
        if not root:
            return
        stack = [(root, 0)]
        while stack:
            node, value = stack.pop()
            self.seen.add(value)
            if node.right:
                stack.append((node.right, value * 2 + 2))
            if node.left:
                stack.append((node.left, value * 2 + 1))

# Example Execution
root = TreeNode(-1)
root.right = TreeNode(-1)
find_elements = FindElements(root)
print(find_elements.find(1))  # Output: False
print(find_elements.find(2))  # Output: True
