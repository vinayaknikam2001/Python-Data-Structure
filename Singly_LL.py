class node():
    def __init__ (self,data):
        self.data = data
        self.next = None

class Linked_list():
    def __init__ (self):
        self.head = None
        self.tail = None
        self.size = 0
 
    def insert_from_head(self,data):
        newnode = node(data)
        if (self.head == None):
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head 
            self.head = newnode
        print('Newnode inserted at head position. ')
        self.size += 1

    def insert_from_tail(self,data):
        newnode = node(data)
        if (self.tail == None):
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
        print('Newnode inserted at tail position. ')
        self.size += 1

    def delete_from_head(self,value):
            if(self.head == None):
                print('Linked list is empty  \n')
            else:
                current = self.head
                while(current != None and current.data  != value):
                    prev = current
                    current = current.next
                if (current  == None):
                    print('Element is not present in the linked list. ')
                    return
                elif(self.head == current):
                    self.head = current.next
                elif(self.tail == current):
                    prev.next = current.next
                    self.tail = prev
                else :
                    prev.next = current.next
                self.size -= 1
                print('Element is succesfully deleted from the linked list. ')
                
            
        
    def show_LL(self):
        current = self.head
        if (current == None):
            print('Linked list is empty. ')
            return
            
        while(current != None):
            print(current.data)
            current = current.next
        print('size of  list is : ',self.size)
        print('end')
    


def func(ob):
    newnode = node(5)
    if(ob == None):
        ob.head = newnode
        ob.tail = newnode
    else:
        newnode.next = ob.head
        ob.head = newnode.next
    return ob

ob = Linked_list()
ob = func(ob)
print(ob.head.data)

'''obj = Linked_list()
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
            obj.delete_from_head(value)'''
            
    



                                                                                                                             
  
                
         
