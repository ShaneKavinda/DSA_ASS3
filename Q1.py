import math
seq = [9, -1, 45, 6, 8, 21, 34, 5, 55, 65, 543, 18, 90, 122, 132, 0, 66, 100, -12, 17]

class Node:
    # Initialize a node with no children
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
class BST:
    def __init__(self) -> None:
        self.root = None
    def __insert__(self, value):
        # find the proper parent node
            if self.root is None:
                self.root = Node(value)
            else:
                parent = None
                current = self.root
                while current is not None:
                    if value < current.value:
                        parent = current
                        current = current.left
                    else:
                        parent = current
                        current = current.right
                # Create the new node and attach it to the BST
                if value < parent.value:
                    parent.left = Node(value)
                else:
                    parent.right = Node(value)


bst = BST()

for i in seq:
    bst.__insert__(i)

def inOrderTraversal(root):
    result = []
    if root is not None:
        result = inOrderTraversal(root.left)
        result.append(root.value)
        result += inOrderTraversal(root.right)

    return result

# Inserting into a BST and traversing in-order will give sorted version of the sequence
sorted_seq = inOrderTraversal(bst.root)
print(sorted_seq)

# Take the mid point as the new node 
# call the function recursively till you end up with an empty node

def createBalancedBST(arr):
    if (len(arr) == 0):
        return None
    mid = len(arr) // 2
    root = Node(arr[mid])
    root.left = createBalancedBST(arr[0:mid])
    root.right = createBalancedBST(arr[mid+1:])
    return root


depth = math.ceil(math.log(len(sorted_seq), 2))



## Print function taken from https://www.geeksforgeeks.org/print-binary-tree-2-dimensions/
def print_space(n, removed):
    for i in range(n):
        print(" ", end="")
    if removed is None:
        print(" ", end="")
    else:
        print(removed.value, end="")
 
 
def height_of_tree(root):
    if root is None:
        return 0
    return 1 + max(height_of_tree(root.left), height_of_tree(root.right))
 
 
def print_binary_tree(root):
    tree_level = []
    temp = []
    tree_level.append(root)
    counter = 0
    height = height_of_tree(root) - 1
    number_of_elements = 2 ** (height + 1) - 1
    while counter <= height:
        removed = tree_level.pop(0)
        if len(temp) == 0:
            print_space(int(number_of_elements /
                            (2 ** (counter + 1))), removed)
        else:
            print_space(int(number_of_elements / (2 ** counter)), removed)
        if removed is None:
            temp.append(None)
            temp.append(None)
        else:
            temp.append(removed.left)
            temp.append(removed.right)
        if len(tree_level) == 0:
            print("\n")
            tree_level = temp
            temp = []
            counter += 1


balancedBST = createBalancedBST(sorted_seq)

print_binary_tree(balancedBST)
