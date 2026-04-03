class binTree():
    def __init__(self,data):
        self.data = data
        self.l = None
        self.r = None
    def preorder(self):
        print(self.data)
        if self.l != None:
            self.l.preorder()
        if self.r != None:
            self.r.preorder()
    def inorder(self):
        if self.l != None:
            self.l.inorder()
        print(self.data)
        if self.r != None:
            self.r.inorder()
    def postorder(self):
        if self.l != None:
            self.l.postorder()
        if self.r != None:
            self.r.postorder()
        print(self.data)

tree = binTree(3)
tree.l = binTree(1)
tree.r = binTree(2)
tree.l.l = binTree(5)
tree.l.r = binTree(4)
tree.r.r = binTree(7)
tree.r.l = binTree(8)
tree.preorder()
print('\n')
tree.inorder()
print('\n')
tree.postorder()
