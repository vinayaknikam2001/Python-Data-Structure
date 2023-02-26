from array import array
class Queue:
    def __init__(self,maxsize):
        self.q = []
        self.front = -1
        self.rear = -1
        self.count = 0


    def enqueue(self,value,maxsize):
        if(self.count == maxsize):
            print('Queue is full \n')
        else:
            if(self.front == -1):
                self.front = 0
                self.rear = 0
            else:
                self.rear = (self.rear+1) % maxsize
            self.q[self.rear] = value
            self.count += 1
            print('Element successfully inserted in a queue \n')

    def dequeue(self,maxsize):
        if(self.front == -1):
            print('Queue is empty \n')
        else:
            if(self.count == 1):
                val = self.q[front]
                self.front = -1
                self.rear = -1
            else:
                val = self.q[front]
                self.front = (self.front+1)%maxsize
            print('Value is : ',val,'\n')
            count -= 1

    def display_queue(self,maxsize):
        if(self.front == -1):
            print('Queue is empty \n')
            return
        else:
            print('Elements of queue are : \n')
            start = self.front
            while(start != self.rear+1):
                print(self.q[start])
                start = (start+1)%maxsize


maxsize = int(input('Enter maximum size of queue \n')) 
Q = Queue(maxsize)
ch = int(input('Enter choice 0>Terminate program    1>Enqueue   2>Dequeue   3>Display_queue  \n'))
while(ch):
    if(ch == 0):
        print('Program terminated \n')
    if(ch == 1):
        value = int(input('Enter the value to insert \n'))
        Q.enqueue(value,maxsize)
    if(ch == 2):
        Q.dequeue(maxsize)
    if(ch == 3):
        Q.display_queue(maxsize)
        
    
                
            
            
            
    
                        
        
                    
               
