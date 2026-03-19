class Queue():
    def __init__(self,size):
        self.size = size
        self.list = []
    def enqueue(self,value):
        if len(self.list) < self.size:
            self.list.append(value)
        else:
            print('Error,\n Maximum values in queue.')

    def dequeue(self):
        if len(self.list) > 0:
            self.list.pop(0)
        else:
            print('Error,\n no values in queue.')

    def get(self,index):
        return self.list[index]
    
    def print_queue(self):
        print('')
        for i in range(len(self.list)):
            print(self.list[i])
        

queue = Queue(10)
queue.enqueue(1)
queue.print_queue()
queue.enqueue(2)
queue.print_queue()
queue.dequeue()
queue.print_queue()
queue.enqueue(3)
queue.print_queue()
print('\n',queue.get(0))