class Node:
    def __init__(self,data):
        self.left = None            #Defining the nodes in a Tree
        self.right = None
        self.data = data


#insertion of data into a Binary tree

    def insertt(self,data):
        if(self.data):
            if data<=self.data:
                if(self.left==None):
                    self.left = Node(data)
                else:
                    self.left.insertt(data)
            else:
                if(self.right==None):
                    self.right = Node(data)
                else:
                    self.right.insertt(data)
                    
        else:
            self.data = data


#Inorder Traversal in a binary Tree
    def print_inorder(self):
      if self.left:
         self.left.printt()
      print( self.data),
      if self.right:
         self.right.printt()

#Preorder Traversla in a binary tree
    def print_preorder(self):
        print( self.data)
        if self.left:
            self.left.printt()

        if self.right:
            self.right.printt()


#Postorder Traversal in a binary tree
    def print_postorder(self):
        if self.left:
            self.left.printt()

        if self.right:
            self.right.printt()

        print( self.data)

x = Node(20)
for _ in range(int(input())):       #Enter the Number of Elements that u want to insert in a Binary tree
    x.insertt(int(input()))

print("Printing inorder")
x.print_inorder()
print("Printing preorder")
x.print_preorder()
print("Printing postorder")
x.print_postorder()


