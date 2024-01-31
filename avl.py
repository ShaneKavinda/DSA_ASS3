# Tree Node object
class TreeNode():
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.height = 0
    def getHeight(self):
        return self.height


class AVLTree():

    # Insert a node
    def insert(self, root, value):
        # Traverse and insert in the correct position
        if not root:    # If the root is empty
            return TreeNode(value)
        elif value < root.value:
            return self.insert(root.left, value)
        else:
            return self.insert(root.rifht, value)
        # Update the height of the root
        root.height = 1 + max(self.getHeight(root.left) , self.getHeight(root.right))
