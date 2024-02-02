"""
File: testAVLtree.py

Tests the AVL tree building algorithm
"""

        
#import random, math

outputdebug = True 

def debug(msg):
    if outputdebug:
        print (msg)

class Node():
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None 




class AVLTree():
    def __init__(self, *args):
        self.node = None 
        self.height = -1  
        self.balance = 0; 
        
        if len(args) == 1: 
            for i in args[0]: 
                self.insert(i)
                
    def height(self):
        if self.node: 
            return self.node.height 
        else: 
            return 0 
    
    def is_leaf(self):
        return (self.height == 0) 
    
    def insert(self, key):
        tree = self.node
        
        newnode = Node(key)
        
        if tree == None:
            self.node = newnode 
            self.node.left = AVLTree() 
            self.node.right = AVLTree()
            debug("Inserted key [" + str(key) + "]")
        
        elif key < tree.key: 
            self.node.left.insert(key)
            
        elif key > tree.key: 
            self.node.right.insert(key)
        
        else: 
            debug("Key [" + str(key) + "] already in tree.")
            
        self.rebalance() 
    # Return True if the element is in the tree
    def search(self, e):
        current = self # Start from the root

        while current.node != None:
            if e < current.node.key:
                current = current.node.left
            elif e > current.node.key:
                current = current.node.right
            else: 
                return True # Element is found

        return False

    def delete(self, key):
        tree = self.node
        if tree is None:
            return None
        if key < tree.key:
            self.node.left.delete(key)
        elif key > tree.key:
            self.node.right.delete(key)
        elif key == tree.key:
            # Case I: There are no children
            if self.node.left.node is None and self.node.right.node is None:
                self.node = None
            # Case II: There is only a left child
            elif self.node.right.node is None:
                self.node = self.node.left
            # Case III: There is only a right child
            elif self.node.left.node is None:
                self.node = self.node.right
            # Case IV: There are both left and right children present
            else:
                logical_successor = self.logical_successor(self.node)
                self.node = logical_successor
                debug("Deleted key: ["+ str(key)+ "]")
            self.rebalance()
        else:
            debug("The key [",str(key),"] does not exist in Tree.")

        
    def rebalance(self):
        ''' 
        Rebalance a particular (sub)tree
        ''' 
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:
                if self.node.left.balance < 0:  
                    self.node.left.lrotate() # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()
                
            if self.balance < -1:
                if self.node.right.balance > 0:  
                    self.node.right.rrotate() # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()


            
    def rrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' right') 
        A = self.node 
        B = self.node.left.node 
        T = B.right.node 
        
        self.node = B 
        B.right.node = A 
        A.left.node = T 

    
    def lrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' left') 
        A = self.node 
        B = self.node.right.node 
        T = B.left.node 
        
        self.node = B 
        B.left.node = A 
        A.right.node = T 
        
            
    def update_heights(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()
            
            self.height = max(self.node.left.height,
                              self.node.right.height) + 1 
        else: 
            self.height = -1 
            
    def update_balances(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height 
        else: 
            self.balance = 0 


    def logical_predecessor(self, node):
        ''' 
        Find the biggest valued node in LEFT child
        ''' 
        node = node.left.node 
        if node != None: 
            while node.right != None:
                if node.right.node == None: 
                    return node 
                else: 
                    node = node.right.node  
        return node 
    
    def logical_successor(self, node):
        ''' 
        Find the smallese valued node in RIGHT child
        ''' 
        node = node.right.node  
        if node != None: # just a sanity check  
            
            while node.left != None:
                debug("LS: traversing: " + str(node.key))
                if node.left.node == None: 
                    return node 
                else: 
                    node = node.left.node  
        return node 

    def check_balanced(self):
        if self == None or self.node == None: 
            return True
        
        # We always need to make sure we are balanced 
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())  
        
    def inorder_traverse(self):
        if self.node == None:
            return [] 
        
        inlist = [] 
        l = self.node.left.inorder_traverse()
        for i in l: 
            inlist.append(i) 

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l: 
            inlist.append(i) 
    
        return inlist 
    
    def postorder_traverse(self):
        if self.node == None:
            return []
        inlist = []
        l = self.node.left.postorder_traverse()
        for i in l:
            inlist.append(i)
        r = self.node.right.postorder_traverse()
        for i in r:
            inlist.append(i)
        inlist.append(self.node.key)
        return inlist
    
    def preorder_traverse(self):
        if self.node == None:
            return []
        inlist = []
        inlist.append(self.node.key)
        l = self.node.left.preorder_traverse()
        for i in l:
            inlist.append(i)
        r = self.node.right.preorder_traverse()
        for i in r:
            inlist.append(i)
        return inlist 
    
    def display(self, level=0, pref=''):
        '''
        Display the whole tree (but turned 90 degrees counter-clockwisely). Uses recursive def.
        '''        
        self.update_heights()  # Must update heights before balances 
        self.update_balances()  
        if(self.node != None): 
            if self.node.left != None:
                self.node.right.display(level + 2, '>')
            print (' ' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(self.balance) + "]", 'L' if self.is_leaf() else ' ')    
            if self.node.left != None: 
                self.node.left.display(level + 2, '<')

         
    def printTreeNoHB(self):            ##  https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
        def display(root):              ##  AUTHOR: Original: J.V.     Edit: BcK
            #   No child.
            if root.node.right.node is None and root.node.left.node is None:
                line = str(root.node.key)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            #   Only left child.
            if root.node.right.node is None:
                lines, n, p, x = display(root.node.left)
                nodeOutput = (str(root.node.key) )
                keyLength = len(nodeOutput)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + nodeOutput
                second_line = x * ' ' + '/' + (n - x - 1 + keyLength) * ' '
                shifted_lines = [line + keyLength * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + keyLength, p + 2, n + keyLength // 2

            #   Only right child.
            if root.node.left.node is None:
                lines, n, p, x = display(root.node.right)
                nodeOutput = str(root.node.key)
                keyLength = len(nodeOutput)
                first_line = nodeOutput + x * '_' + (n - x) * ' '
                second_line = (keyLength + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [keyLength * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + keyLength, p + 2, keyLength // 2

            #   Two children.
            left, n, p, x = display(root.node.left)
            right, m, q, y = display(root.node.right)
            nodeOutput = str(root.node.key)
            keyLength = len(nodeOutput)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + nodeOutput + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + keyLength + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + keyLength * ' ' + b for a, b in zipped_lines]
            return lines, n + m + keyLength, max(p, q) + 2, n + keyLength // 2

        lines = []
        if self.node != None:
            lines, *_ = display(self)
            print("\t\t== AVL Tree ==")
            print()
        if lines == []:
            print("No tree found, please rebuild a new Tree.\n")
            return -1
        for line in lines:
            print(line)
        print()     

    def getNodes(self, nodes):
        if self.height == -1:
            return
        if self.height == 0:
            return None
        else:
            nodes.append(self.node.key)
            self.node.left.getNodes(nodes)
            self.node.right.getNodes(nodes)
        return nodes
    
    def getLeaves(self, leaves):
        if self.height == -1:
            return 
        if self.height == 0:
            leaves.append(self.node.key)
        else:
            self.node.left.getLeaves(leaves)
            self.node.right.getLeaves(leaves)
        return leaves
    
    def getLeavesAndNodes(self):
        leaves = []
        nodes = []
        leaves = self.getLeaves(leaves)
        nodes = self.getNodes(nodes)
        return (leaves, nodes)
    



def main_menu():

    exit_condition = False

    while (not exit_condition):
        print("============= Build and AVL Tree ==============")
        print("1. Preload a sequence of integers to build an AVL Tree")
        print("2. Manually enter integer keys one by one to build an AVL Tree")
        print("3. Exit")
        try:
            user_input = int(input("Choose one of the above options: "))

            match (user_input):
                case 1:
                    print("Entering the sequence [60, 80, -30, 19, 41, 76, 30, 6, 0, -1, 98, 94, 44, 85, 54, 47, 48, 49, 45, 75, 91]")
                    sequence = [60, 80, -30, 19, 41, 76, 30, 6, 0, -1, 98, 94, 44, 85, 54, 47, 48, 49, 45, 75, 91]
                    avl = AVLTree()
                    for i in sequence:
                        avl.insert(i)
                    while (True):
                        print("1. Display the AVL Tree, showing the height and balance factor for each node")
                        print("2. Print pre-order, in-order and post-order traversal sequences of the AVL tree")
                        print("3. Print all leaf nodes of the AVL Tree, and non leaf nodes")
                        print("4. Insert a new integer into the AVL Tree")
                        print("5. Delete an integer key from the AVL Tree")
                        print("6. Return to main menu")
                        user_input = int(input("Choose one of the above options: "))
                        match (user_input):
                            case 1:
                                avl.display()
                                avl.printTreeNoHB()
                            case 2:
                                print("in-order traversal: ", avl.inorder_traverse())
                                print("pre-order traversal: ", avl.preorder_traverse())
                                print("post-order traversal: ", avl.postorder_traverse())
                            case 3:
                                (leaves, nodes) = avl.getLeavesAndNodes()
                                print("leaves: ", leaves)
                                print("nodes: ", nodes)
                                leaves = []
                                nodes = []
                            case 4:
                                num = int(input("Enter a number to insert into the AVL tree: "))
                                found = avl.search(num)
                                if found:
                                    print ("Node already present in the tree")
                                else:
                                    avl.insert(num)
                                    print("=== Updated Tree ===")
                                    avl.printTreeNoHB()
                            case 5:
                                num = int(input("Enter a number to delete from the Integer tree: "))
                                found = avl.search(num)
                                if found:
                                    avl.delete(num)
                                    print("== Updated tree after deleting ", num, " ==")
                                    avl.printTreeNoHB()
                                else:
                                    print("Node not present in the Tree")
                            case 6:
                                break
                                
                case 2:
                    print("Enter the numbers you want to insert one by one:")
                    avl = AVLTree()
                    #finish_entering_nums = False
                    while(True):
                        user_input = input("Enter the number to insert into the AVL tree(press e to finish): ")
                        if user_input == "e" or user_input == "E":
                            break
                        else:
                            num = int(user_input.strip())
                            avl.insert(num)
                            print("=== Updated Tree ===")
                            avl.printTreeNoHB()
                    # Prompt menu after finish inserting values
                    while (True):
                        print("1. Display the AVL Tree, showing the height and balance factor for each node")
                        print("2. Print pre-order, in-order and post-order traversal sequences of the AVL tree")
                        print("3. Print all leaf nodes of the AVL Tree, and non leaf nodes")
                        print("4. Insert a new integer into the AVL Tree")
                        print("5. Delete an integer key from the AVL Tree")
                        print("6. Return to main menu")
                        user_input = int(input("Choose one of the above options: "))
                        match (user_input):
                            case 1:
                                avl.display()
                                avl.printTreeNoHB()
                            case 2:
                                print("in-order traversal: ", avl.inorder_traverse())
                                print("pre-order traversal: ", avl.preorder_traverse())
                                print("post-order traversal: ", avl.postorder_traverse())
                            case 3:
                                (leaves, nodes) = avl.getLeavesAndNodes()
                                print("leaves: ", leaves)
                                print("nodes: ", nodes)
                                leaves = []
                                nodes = []
                            case 4:
                                num = int(input("Enter a number to insert into the AVL tree: "))
                                avl.insert(num)
                                print("=== Updated Tree ===")
                                avl.printTreeNoHB()
                            case 5:
                                num = int(input("Enter a number to delete from the Integer tree: "))
                                avl.delete(num)
                                print("== Updated tree after deleting ", num, " ==")
                                avl.printTreeNoHB()
                            case 6:
                                break
                case 3:
                    exit_condition
                    break
        except ValueError:
            print("Please enter a valid option: ")


# Usage example
if __name__ == "__main__": 

    ####        Test the functionality using the given data set         ###

    # a = AVLTree()
    # inlist = [60, 80, -30, 19, 41, 76, 30, 6, 0, -1, 98, 94, 44, 85, 54, 47, 48, 49, 45, 75, 91]
    # print ("\n\n----- Inserting (step-by-step):\n", end =" \t")
    # print(inlist, end ="\n\n")
    # for i in inlist: 
    #     a.insert(i)
    #     #a.printTreeNoHB()
    # print ("\nInorder traversal:", a.inorder_traverse())
    # print("\nPost order traverse: ", a.postorder_traverse())
    # print("\npreorder traversal: ", a.preorder_traverse())
    # #print("\n == AVL tree (printed left-side down, with [hights, balance_factors] & an \'L\' for each leaf node) ==\n")     
    # #a.display()
    # print("\n == AVL tree shape (in BFS traversal order) ==\n")
    # a.printTreeNoHB()
    # a.delete(17)
    # print("Deleting, 17")
    # a.printTreeNoHB()
    # leaves, nodes = a.getLeavesAndNodes()
    # print("leaves: ", leaves)
    # print("nodes: ", nodes)

    # testarrays = [[73, 22, 65, 52, 97, 50, 90, 37],
    # [96, 89, 82, 51, 12, 55, 27, 91, 40, 79, 83, 4, 10, 3],
    # [60, 95, 98],
    # [73],
    # []]

    # for i in testarrays:
    #   avl = AVLTree()
    #   for item in i:
    #       avl.insert(item)
    #   avl.printTreeNoHB()

    main_menu()
