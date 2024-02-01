class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    # Return True if the element is in the tree
    def search(self, e):
        current = self.root # Start from the root

        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            elif e == current.element: # element matches current.element
                return True # Element is found

        return False

    # Calculate the depth of a given node in the BST
    def depth_nodeBST(self, N):
        depth = self.depth_nodeBSTHelper(N.element)  # Use the search method to find the depth
        return depth


     # Return True if the element is in the tree
    def depth_nodeBSTHelper(self, e):
        current = self.root # Start from the root
        depth = 0
        while current != None:
            if e < current.element:
                current = current.left
                depth += 1
            elif e > current.element:
                current = current.right
                depth += 1
            else: # element matches current.element
                return depth # Element is found


    # Insert element e into the binary search tree
    # Return True if the element is inserted successfully
    def insert(self, e):
        if self.root == None:
          self.root = self.createNewNode(e) # Create a new root
        else:
          # Locate the parent node
          parent = None
          current = self.root
          while current != None:
            if e < current.element:
              parent = current
              current = current.left
            elif e > current.element:
              parent = current
              current = current.right
            else:
              return False # Duplicate node not inserted

          # Create the new node and attach it to the parent node
          if e < parent.element:
            parent.left = self.createNewNode(e)
          else:
            parent.right = self.createNewNode(e)

        self.size += 1 # Increase tree size
        return True # Element inserted

    # Create a new TreeNode for element e
    def createNewNode(self, e):
      return TreeNode(e)
    """
    # Return the size of the tree
    def getSize(self):
      return self.size"""

    # Inorder traversal from the root
    def inorder(self):
      self.inorderHelper(self.root)

    # Inorder traversal from a subtree
    def inorderHelper(self, root):
      if root != None:
        self.inorderHelper(root.left)
        print(root.element, end = " ")
        self.inorderHelper(root.right)

     # Inverse inorder traversal from the root
    def inverse_inorder(self):
      self.inverse_inorderHelper(self.root)

    
    # Inverse inorder traversal from a subtree
    def inverse_inorderHelper(self, root):
      if root != None:
        self.inverse_inorderHelper(root.right)
        print(root.element, end = " ")
        self.inverse_inorderHelper(root.left)
        
    #Leaf nodes    
    def leaf_BST(self):
        self.leaf_BST_helper(self.root)

    def leaf_BST_helper(self, root):
        if root != None:
            if root.left == None and root.right == None:
                print(root.element, end = " ")
            else:
                self.leaf_BST_helper(root.left)
                self.leaf_BST_helper(root.right)
                
    #Non leaf nodes
    def non_leaf_BST(self):
        self.non_leaf_BST_helper(self.root)

    def non_leaf_BST_helper(self, root):
        if root != None:
            if root.left != None or root.right != None:
                print(root.element, end = " ")
            self.non_leaf_BST_helper(root.left)
            self.non_leaf_BST_helper(root.right)
        

    # Postorder traversal from the root
    def postorder(self):
      self.postorderHelper(self.root)

    # Postorder traversal from a subtree
    def postorderHelper(self, root):
      if root != None:
        self.postorderHelper(root.left)
        self.postorderHelper(root.right)
        print(root.element, end = " ")



    # Preorder traversal from the root
    def preorder(self):
      self.preorderHelper(self.root)

    # Preorder traversal from a subtree
    def preorderHelper(self, root):
      if root != None:
        print(root.element, end = " ")
        self.preorderHelper(root.left)
        self.preorderHelper(root.right)

    def total_nodesBST(self, N):
        return self.total_nodesBST_helper(N)

    def total_nodesBST_helper(self, root):
        if root is None:
            return 0
        else:
            return 1 + self.total_nodesBST_helper(root.left) + self.total_nodesBST_helper(root.right)

    
    # Return true if the tree is empty
    def isEmpty(self):
      return self.size == 0

    # Remove all elements from the tree
    def clear(self):
      self.root = None
      self.size = 0

    # Return the root of the tree
    def getRoot(self):
      return self.root
    

    
# Find the depth of a subtree starting with a user provided node

def find_subtree_depth(root, root_key):
    subtree_root = find_node(root, root_key)
    if subtree_root:
        return max(find_height(subtree_root.left), find_height(subtree_root.right))
    else:
        return -1  # Subtree root not found in the tree

def find_height(root):
    if root is None:
        return 0
    left_height = find_height(root.left)
    right_height = find_height(root.right)
    return max(left_height, right_height)
         


def find_depth(root, key, depth=0):
    if root is None:
        return -1  # Node not found
    if root.element == key:
        return depth
    elif root.element < key:
        return find_depth(root.right, key, depth + 1)
    else:
        return find_depth(root.left, key, depth + 1)

def find_node(root, key):
    if root is None:
        return None
    if root.element == key:
        return root
    elif root.element < key:
        return find_node(root.right, key)
    else:
        return find_node(root.left, key)
    


   
    
def printTree(root, element="element", left="left", right="right"):                                 ##  https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    def display(root, element=element, left=left, right=right):                                     ##  AUTHOR: Original: J.V.     Edit: BcK
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, element)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, element)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, element)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, element)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
    
    lines = []
    if root != None:
        lines, *_ = display(root, element, left, right)
    print("\t== Binary Tree: shape ==")
    print()
    if lines == []:
        print("\t  No tree found")
    for line in lines:
        print("\t", line)
    print()

class TreeNode:
    def __init__(self, e):
      self.element = e
      self.left = None # Point to the left node, default None
      self.right = None # Point to the right node, default None

    ####################### Main test binary tree

def print_menu():
    print("\n\n1. Pre-load a sequence of integers to build BST")
    print("2. Manually enter integer keys one by one to build BST")
    print("3. Exit")

def menu_two():
    print("\nMain Menu:")
    print("1. Display the tree shape, pre-order, in-order, post-order, and inverse-in-order traversal sequences")
    print("2. Display all leaf nodes and non-leaf nodes")
    print("3. Display a sub-tree and count the number of nodes")
    print("4. Display the depth of a given node in the BST")
    print("5. Display the depth of a subtree of the BST")
    print("6. Insert a new integer key into the BST")
    print("7. Delete an integer key from the BST")
    print("8. Exit")
    

   

def main():

   
    numbers =[58, 84, 68, 23, 38, 82, 26, 17, 24, 106, 95, 48, 88, 54, 50, 51, 53, 49, -6, -46]
    print ("\n\nInserting the following values into an initially empty BST:\n")
    # for i in numbers:
    #     print(i, end=" ")
    # print()   
    intTree = BinaryTree()
    for e in numbers:
      intTree.insert(e)
    root_node = intTree.getRoot()
    printTree(intTree.root)
    depth = find_depth(intTree.root, 54)
    print("depth of node 54: ", depth)
    subtree_node = 38
    subtree_depth = find_subtree_depth(intTree.root, subtree_node)
    print("depth of the subtree: ", subtree_depth)
    
    
    



    # print("\nInorder traversal:")
    # intTree.inorder()
    # print("\npostorder traversal: ")
    # intTree.postorder()
    # print("\n preorder traversal: ")
    # intTree.preorder()    All 3 works


       
    # choice = 0
    # while choice != 3:
    #     print_menu()
    #     try:
    #         choice = int(input("Enter your choice (1-3): "))
    #     except ValueError:
    #         print("Invalid input. Please enter a number.")
    #         continue

    #     if choice == 1:
    #         print("1")
    #     elif choice == 2:
    #         print("2")

    #     elif choice == 3:
    #         print("Exiting the program.")
    #     else:
    #         print("Invalid choice. Please enter a number between 1 and 3.")


    # choice = 0
    # while choice != 8:
    #     menu_two()
    #     try:
    #         choice = int(input("Enter your choice (1-8): "))
    #     except ValueError:
    #         print("Invalid input. Please enter a number.")
    #         continue

    #     if choice == 1:
    #         print("\nPreorder traversal:")
    #         intTree.preorder()
    #         print("\n\nInorder traversal:")
    #         intTree.inorder()
    #         print("\n\nInverse Inorder traversal:")
    #         intTree.inverse_inorder()
    #         print("\n\nPostorder traversal:")
    #         intTree.postorder()
    #     elif choice == 2:
    #         print("\n\nLeaf node:")
    #         intTree.leaf_BST()
    #         print("\nNon Leaf node:")
    #         intTree.non_leaf_BST()
    #     elif choice == 3:
    #         print("3")
    #     elif choice == 4:
            
    #         search_value = int(input("\n\nEnter search value"))
    #         search_value = TreeNode(search_value)
    #         found = intTree.search(search_value)
            
          
    #         if found:
    #             print("\nDepth of the root node:", intTree.depth_nodeBST(search_value))
    #         else:
    #             print("\nNode not found in the tree")
    #     elif choice == 5:
    #         print("5")
    #     elif choice == 6:
    #         print("6")
    #     elif choice == 7:
    #         print("7")
    #     elif choice == 8:
    #         print("Exiting the program.")
    #     else:
    #         print("Invalid choice. Please enter a number between 1 and 8.")











    

      
if __name__ == "__main__":
    main() 
