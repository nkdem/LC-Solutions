# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root, low, high):
        total = 0
        if low <= (v := root.val) <= high:
            total += v
        if root.left:
            total += self.rangeSumBST(root.left, low,high)
        if root.right:
            total += self.rangeSumBST(root.right, low, high)
        return total



# s = Solution()
# t = TreeNode(10)

# l = TreeNode(5)
# l.left = (lr := TreeNode(5))
# lr.left = TreeNode(3)
# lr.right = TreeNode(7)

# r = TreeNode(15)
# r.right = TreeNode(18)

# t.left = l
# t.right = r

# print(s.rangeSumBST(t, low=7, high=15))
