class circularqueue:
    def __init__(self):
        self.items = []
        self.front = -1
        self.rear = -1
        self.max = 20
    def enqueue(self,item):
        if (self.front == 0 and self.rear == (self.max-1))or (self.rear == self.front - 1):
                 print("queue full")
        else :
            if self.front == -1 :
                self.front = 0
                self.rear = 0
                self.items.insert(self.rear,item)
            else:
                 if(self.rear == (self.max-1) and self.front != 0):
                     self.rear = 0
                     self.items.insert(self.rear,item)
                 else:
                     self.rear = self.rear+1
                     self.items.insert(self.rear,item)
                
           
    def dequeue(self):
        if self.front == -1 :
            return "empty queue"
        temp = self.items[self.front]
        self.items[self.front] = -1
        if self.front == self.rear:
            self.rear = self.front = -1
        else:
            if self.front == self.max-1:
                self.front = 0
            else:
                self.front+=1
        return temp




c = circularqueue()
c.enqueue(4)
c.enqueue(5)
c.enqueue(6)
print(c.items)
print(c.dequeue())

                
            
            
           
                
