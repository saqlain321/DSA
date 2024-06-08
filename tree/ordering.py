class Node:
    def __init__(self , value):
        self.val = value
        self.left = None
        self.right = None

    def preorder(self):
        print(self.val, end=' ')
        if self.left != None:
            self.left.preorder()
        if self.right != None:
            self.right.preorder()

    def inorder(self):
        
        if self.left != None:
            self.left.inorder()
        print(self.val, end=' ')
        if self.right != None:
            self.right.inorder()

    def postorder(self):
        if self.left != None:
            self.left.postorder()
        
        if self.right != None:
            self.right.postorder()

        print(self.val, end=' ')

# Drivers code for the above binary tree class  
root_node = Node(4)  
  
root_node.left = Node(5)  
root_node.right = Node(7)  
root_node.right.left = Node(2)  
root_node.right.left.right = Node(9)  
root_node.left.right = Node(0)  
root_node.left.left = Node(10)  
root_node.left.left.right = Node(1)  
  
# Transferring the tree  
print("Pre-order traversal of the tree: ", end = "")  
root_node.preorder()  
print("\nIn-order traversal of the tree: ", end = "")  
root_node.inorder()  
print("\nPost-order traversal of the tree: ", end = "")  
root_node.postorder()  