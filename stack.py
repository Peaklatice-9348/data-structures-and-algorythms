
class Stack():
    def __init__(self,size):
        self.list = []
        self.size = size
    def push(self,value):
        if len(self.list)<self.size:
            self.list.append(value)
        else:
            print('Error!\n Maximum values in stack.')
    def pop(self):
        if len(self.list) > 0:
            self.list.pop(-1)
        else:
            print('Error!\n No values in stack to remove.')
    def print_all(self):
        if len(self.list) > 0:
            for i in range(len(self.list)):
                print(self.list[i])            
        else:
            print('Error!\n No values in stack to print.')
        
    def get(self,index):
        return self.list[index]
    



stack1 = Stack(0)
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
print(stack1.get(2))
stack1.print_all()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.print_all()
