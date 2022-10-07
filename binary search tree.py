class bsttree:
    def __init__(self,data):
        self.info=data
        self.lchild=None
        self.rchild=None
    def insert(self,item):
        if(item==self.info):
            return 0
        if item<self.info:
            if self.lchild is None:
                self.lchild=bsttree(item)

            else:
                self.lchild.insert(item)
        else:
            if self.rchild is None:
                self.rchild=bsttree(item)

            else:
                self.rchild.insert(item)
   
    
                                   
    def postorder(self,root):
        if root!=None:
            self.postorder(root.lchild)
            self.postorder(root.rchild)
            print(root.info,end=" ")
    def count_leaf_nodes(self,root):
        if root==None:
            return 0
        elif root.lchild==None and root.rchild==None:
            return 1
        else:
            return(self.count_leaf_nodes(root.lchild)+self.count_leaf_nodes(root.rchild))
    def  min_value(self,root):
        if root==None or root.lchild==None:
            return root
        else:
            return self.min_value(root.lchild)
                   
        


if __name__=="__main__":
    x=int(input("Enter the value of root: "))
    tree=bsttree(x)
    tree.insert(37)
    tree.insert(49)
    tree.insert(12)
    tree.insert(72)
    tree.insert(102)
    tree.insert(65)
    tree.insert(97)
    tree.insert(21)
    print("postorder traversal of binary search tree")

    tree.postorder(tree)
    
    
    r2=tree.count_leaf_nodes(tree)
    print("\n Total number of leaf_node in the Binary Search tree",r2)
    r3=tree.min_value(tree)
    print("\n Minimum value of the Binary search tree",r3.info)
            
