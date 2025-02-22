class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal):
        stack = []  # Stack to maintain the path of nodes
        i = 0  # Pointer to traverse the input string

        while i < len(traversal):
            depth = 0  # Count the depth (number of dashes)
            while i < len(traversal) and traversal[i] == '-':
                depth += 1
                i += 1

            num_start = i  # Store the starting index of the number
            while i < len(traversal) and traversal[i].isdigit():  # Extract the number value
                i += 1
            value = int(traversal[num_start:i])  # Convert extracted substring to an integer

            node = TreeNode(value)  # Create a new TreeNode

            while len(stack) > depth:  # Adjust stack to maintain correct depth level
                stack.pop()

            if stack:  # If there is a parent node in the stack
                if stack[-1].left is None:  # Assign node as the left child if empty
                    stack[-1].left = node
                else:  # Otherwise, assign node as the right child
                    stack[-1].right = node

            stack.append(node)  # Push the current node onto the stack

        return stack[0]  # Return the root of the tree


# Function to convert tree to list format
def tree_to_list(root):
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


solution = Solution()
traversal = "1-2--3---4-5--6---7"
traversal1="1-401--349---90--88"
root = solution.recoverFromPreorder(traversal)
root1 = solution.recoverFromPreorder(traversal1)

# Print the reconstructed tree
print(tree_to_list(root))
print(tree_to_list(root1))

