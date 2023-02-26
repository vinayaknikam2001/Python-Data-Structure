class node:
    def __init__(self,value):
        self.data = value
        self.next = None
        self.prev = None

class doubly_LL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_from_head(self,value):
        newnode = node(value)
        if (self.size == 0):
            self.head = newnode
            self.tail = newnode
        else :
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        print('Newnode inserted at head position. \n')
        self.size += 1

    def insert_from_tail(self,value):
        newnode = node(value)
        if(self.size
           == 0):
            self.tail = newnode
            self.head = newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
        print('Newnode inserted at tail position. \n')
        self.size += 1

    def delete_node(self,value):
        current = self.head
        if (self.size == 0):
            print('Doubly linked list is empty : \n')
        else:
            while(current != None and current.data != value):
                prev_node = current
                current = current.next

            if(current == None):
                print('Element is not present in the linked list \n')
                return
            if(current == self.head):
                current = current.next
                self.head = current
            elif(current == self.tail):
                prev_node.next = None
                self.tail = prev_node
            else:
                current = current.next
                current.prev = prev_node
                prev_node.next = current
            print('Node is successfully deleted from doubly linked list \n ')
            self.size -= 1
            
    def show_LL(self):
        current = self.head
        if (self.size == 0):
            print('Linked list is empty \n')
        else:
            print('Linked list is : \n')
            while(current != None):
                print(current.data)
                current = current.next


obj = doubly_LL()
flag = 1 
while(flag):
    choice = int(input('Enter choice  0>Quit  1>Insert from head    2>Insert from tail    3>Display linked list  4>Delete the element:  '))
    if(choice == 0):
        flag = 0
        print('Program terminated')
        
    if(choice == 1):
        value = int(input('Enter value to insert at head : '))
        obj.insert_from_head(value)

    if(choice == 2):
        value = int(input('Enter value to insert at tail : '))
        obj.insert_from_tail(value)
        
    if(choice == 3):
        obj.show_LL()

    if(choice == 4):
            value = int(input('Enter value to delete from list  : '))
            obj.delete_node(value)

    































        
        
            
