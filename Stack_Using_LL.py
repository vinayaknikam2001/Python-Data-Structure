class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack_list:
    def __init__(self):
        self.top = None
        self.size = 0
        
    def push_stack(self,data):
        newnode = node(data)
        newnode.next = self.top
        self.top = newnode
        self.size += 1
            
            
    def show_stack(self):
        current = self.top
        if (current == None):
            print('Stack is empty. ')
            return
        else:
            print('Stack is: \n')
            while(current != None):
                print(current.data)
                current = current.next
            print('\nsize:  ',self.size)

    def pop_stack(self):
        if (self.size == 0):
            print('Stack is empty. \n')
        else :
            val = self.top.data
            self.top = self.top.next
            self.size -= 1
            print('Element popped is: ',val,'\n')

        
        
    

s = stack_list()
choice = 1
while (choice):
    choice = int(input('Enter choice : 0>Quit_program    1>push    2>show_stack    3>pop. \n'))
    if (choice == 0):
        print('Program terminated.')
    if (choice == 1):
        data = int(input('Enter element to push into stack. \n'))
        s.push_stack(data)
    if (choice == 2):
        s.show_stack()
    if (choice == 3):
        s.pop_stack()
    
