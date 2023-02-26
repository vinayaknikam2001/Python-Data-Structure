class node:
    def __init__(self,val):
        self.data = val
        self.next = None

class circular_LL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_node(self,val):
        newnode = node(val)
        if(self.size == 0):
            self.head = newnode
            self.tail = newnode
            self.tail.next = newnode
        else:
            newnode.next = self.head
            self.head = newnode
            self.tail.next = newnode
        self.size += 1

    def delete_node(self,val):
        if (self.size == 0):
            print('Circular linked list is empty. \n')
            return
        current = self.head
        if (current.data == val):
            self.head = current.next
            self.tail.next = current.next
            print('Element',val,' successfully deleted. \n')
            return
        else :
            current = current.next
            while(current.data != val and current != self.head):
                prev_node = current
                current = current.next
            if(current == self.head):
                print('Element is not present in circular linked list. \n')
            elif(current == self.tail):
                self.tail = prev_node
                prev_node.next = self.head
                
            else:
                prev_node.next = current.next
        print('Element',val,' successfully deleted. \n')
        self.size -= 1

    def show_LL(self):
        if(self.size == 0):
            print('Circular linked list is empty.\n')
        else:
            print('Circular linked list is. \n')
            current = self.head
            print(current.data)
            current = current.next
            while(current != self.head):
                print(current.data)
                current = current.next
            
obj = circular_LL()
choice = 1 
while(choice):
    choice = int(input('Enter choice  0>Quit  1>Insert from head    2>Display circular linked list  3>Delete the element:  '))
    if(choice == 0):
        print('Program terminated')
        
    if(choice == 1):
        val = int(input('Enter value to insert at head : '))
        obj.add_node(val)

    if(choice == 2):
        obj.show_LL()
        
    if(choice == 3):
        val = int(input('Enter value to be deleted : '))
        obj.delete_node(val)

   
