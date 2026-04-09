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
    def search(self,value):
        
        if value < self.data:
            if self.l == None:
                return False
            return self.l.search(value)
        elif value > self.data:
            if self.r == None:
                return False
            return self.r.search(value)
        elif value == self.data:
            return True
    def insersion(self,value):
        if value < self.data and self.l !=None:
            self.l.insersion(value)
        elif value < self.data and self.l == None:
            self.l = binTree(value)
        elif value > self.data and self.r !=None:
            self.r.insersion(value)
        elif value > self.data and self.r ==None:
            self.r = binTree(value)



tree = binTree(14)
tree.l = binTree(2)
tree.r = binTree(27)
tree.l.r = binTree(11)
tree.r.r = binTree(38)
tree.r.l = binTree(16)
tree.l.r.l = binTree(5)
tree.l.r.r = binTree(13)
tree.inorder()
tree.insersion(20)
tree.inorder()

print(tree.search(13))