class node():
    def __init__(self,coeff,degree):
        self.coeff =  coeff
        self.degree = degree
        self.next = None


class Linked_list():
    def __init__(self):
        self.head = None
        self.size = 0

    def create_list(self): 
        print('Enter degree equal to -1 to terminate entering values. \n')
        coeff = int(input('Enter the coefficient value. \n'))
        degree = int(input('Enter the degree. \n'))
        while (degree != -1):
            newnode = node(coeff,degree)
            current = self.head
            if (current == None):
                self.head = newnode
            else :
                current = self.head
                while(current.next != None):
                    current = current.next
                current.next = newnode
            coeff = int(input('Enter the coefficient value. \n'))
            degree = int(input('Enter the degree. \n'))

    def show_LL(self):
        current = self.head
        while(current != None):
            if (current.degree != 0):
                print('coefficient: ',current.coeff,'degree: ',current.degree,'\n')
            else:
                print('coefficient: ',current.coeff,'\n')
            current = current.next

    def add_poly(self,p2):
        temp1 = self.head
        temp2 = p2.head
        while(temp1 != None and temp2 != None):
            if (temp1.degree == temp2.degree):
                coeff = temp1.coeff + temp2.coeff
                degree = temp1.degree
                temp1 = temp1.next
                temp2 = temp2.next

            elif (temp1.degree > temp2.degree):
                coeff = temp1.coeff
                degree = temp1.degree
                temp1 = temp1.next

            else:
                coeff = temp2.coeff
                degree = temp2.degree
                temp2 = temp1.next
                
            if(coeff != 0):
                result.add_node(coeff,degree)

            if (temp1 == None):
                while(temp2 != None):
                    result.add_node(temp2.coeff,temp2.degree)
                    temp2 = temp2.next
            elif(temp2 == None):
                while(temp1 != None):
                    result.add_node(temp1.coeff,temp1.degree)
                    temp1 = temp1.next


    def add_node(self,coeff,degree):
        newnode  = node(coeff,degree)
        if (self.head == None):
            self.head = newnode
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = newnode


p1 = Linked_list()
p2 = Linked_list()
result = Linked_list()
print('Enter 1st polynomial expression. \n')
p1.create_list()
print('\nEnter 2nd polynomial expression. \n')
p2.create_list()
p1.add_poly(p2)
print('\nResult is : \n')
result.show_LL()

            
    
