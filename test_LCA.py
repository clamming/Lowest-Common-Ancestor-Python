import unittest
import LCA

class test_node(unittest.TestCase):

# Basic Binary Tree For Test No.1
#                     1
#                   /  \
#                  /    \
#                 2      3
#                / \    / \
#               4   5  6   7
#
# Test No.1 - Basic test case

    def test_basicTree(self):
        root = LCA.Node(1)
        root.left = LCA.Node(2)
        root.right = LCA.Node(3)
        root.left.left = LCA.Node(4)
        root.left.right = LCA.Node(5)
        root.right.left = LCA.Node(6)
        root.right.right = LCA.Node(7)
        self.assertEqual(1, LCA.lowestCommonAncestor(root, 4, 3))
        self.assertEqual(1, LCA.lowestCommonAncestor(root, 2, 7))
        self.assertEqual(3, LCA.lowestCommonAncestor(root, 6, 7))

# Test No.2 - Null Tree

    def test_nullTree(self):
        root = None
        self.assertEqual(-1, LCA.lowestCommonAncestor(root, 4, 5), 'Empty tree returns -1')

#Test No.3 - Invalid Node

    def test_InvalidNode(self):
        root = LCA.Node(1)
        root.left = LCA.Node(2)
        root.right = LCA.Node(3)
        root.left.left = LCA.Node(4)
        root.left.right = LCA.Node(5)
        root.right.left = LCA.Node(6)
        root.right.right = LCA.Node(7)
        self.assertEqual(-1, LCA.lowestCommonAncestor(root, 4, 9), "Unfound node returns -1")

#Test No.4 Common Ancestor is the Node

    def test_commonAncestorIsNode(self):
        root = LCA.Node(1)
        root.left = LCA.Node(2)
        root.right = LCA.Node(3)
        root.left.left = LCA.Node(4)
        root.left.right = LCA.Node(5)
        root.right.left = LCA.Node(6)
        root.right.right = LCA.Node(7)
        self.assertEqual(2, LCA.lowestCommonAncestor(root, 2, 4))
        self.assertEqual(2, LCA.lowestCommonAncestor(root, 2, 2))
        self.assertEqual(2, LCA.lowestCommonAncestor(root, 4, 2))


#Test No.5 Root is only node

    def test_rootIsNodeOnly(self):
        root = LCA.Node(1)
        self.assertEqual(1, LCA.lowestCommonAncestor(root, 1, 1))

#Test No.6 Both nodes invalid

    def test_bothNodesInvalid(self):
        root = LCA.Node(1)
        root.left = LCA.Node(2)
        root.right = LCA.Node(3)
        root.left.left = LCA.Node(4)
        root.left.right = LCA.Node(5)
        root.right.left = LCA.Node(6)
        root.right.right = LCA.Node(7)
        self.assertEqual(-1, LCA.lowestCommonAncestor(root, 8, 9))

#Test No.7 Duplicated Nodes
    def test_duplicatedNodes(self):
        root = LCA.Node(1)
        root.left = LCA.Node(2)
        root.right = LCA.Node(3)
        root.left.left = LCA.Node(4)
        root.left.right = LCA.Node(6)
        root.right.left = LCA.Node(6)
        root.right.right = LCA.Node(7)
        self.assertEqual(1, LCA.lowestCommonAncestor(root, 6, 7))
            #1 is the common route of both 6's



if __name__ == '__main__':
   unittest.main()