# 🔹 Problem: Binary Tree Postorder Traversal
# 🔗 Link: https://leetcode.com/problems/binary-tree-postorder-traversal/description/?utm_source=chatgpt.com
# 🧠 Approach: Use DFS algorithm with recursion (Base Case + Recursive Case)
# 💡 Status: Solved ✅

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        # We initialize an empty list to store the traversal result
        arr = []

        # Define a helper function for recursive postorder DFS
        def PostOrder(root):
            # Base Case: if the current node is None, we return
            if root is None:
                return
            # Recursive Case: traverse left subtree
            PostOrder(root.left)
            # Then traverse right subtree
            PostOrder(root.right)
            # Finally, process the current node (append its value)
            arr.append(root.val)

        # Start the recursive traversal from the root node
        PostOrder(root)

        # Return the postorder traversal result
        return arr
