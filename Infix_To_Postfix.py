#Expression having 2 digit numbers can not be evaluated
class stack_class:
    def __init__(self):
        self.stack = []
        self.size = -1
        self.precedence = {'^':3,'*':2,'/':2,'+':1,'-':1,'(':0,')':0}

    def push(self,value):
        self.stack.append(value)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.stack.pop()
    
    def peek(self):
        if(self.size == -1):
            return False
        else:
            return self.stack[self.size]
    #Expression having 2 digit numbers can not be evaluated
    def is_num(self,val):
        numbers = ['1','2','3','4','5','6','7','8','9','0']
        if val in numbers:
            return True
        else:
            return False

    def to_postfix(self,infix):
        length = len(infix)
        postfix = ''
        if (length % 2 == 0):
            return 'Incorrect expression! \n'
        
        else:
            for i in infix :
                if (self.is_num(i)):
                    postfix += i
                    
                if(i in '+-*/^'):
                    while(self.size != -1 and self.precedence[i] <= self.precedence[self.peek()]):
                        postfix += self.pop()
                    self.push(i)
                    
                if (i == '('):
                    self.push(i)
                    
                elif (i == ')'):
                    temp = self.pop()
                    while (temp != '('):
                        postfix += temp
                        temp = self.pop()
                        
            while(self.size != -1):
                postfix += self.pop()
            return postfix

    #Expression having 2 digit numbers can not be evaluated    
    def evaluate_postfix(self,postfix):
        for i in postfix:
            if (self.is_num(i)):
                self.push(i)
            else :
                operand2 = self.pop()
                operand1 = self.pop()
                result = self.calculate(operand1,i,operand2)
                self.push(result)
        return result

    def calculate(self,op1,i,op2):
        if (i == '+'):
            return (int(op1) + int(op2))
        if (i == '-'):
            return (int(op1) - int(op2))
        if (i == '*'):
            return (int(op1) * int(op2))
        if (i == '/'):
            return (int(op1) / int(op2))
        if (i == '^'):
            return (int(op1) ** int(op2))



def main():
    s = stack_class()
    choice = 1
    while(choice):
        infix = input('\nEnter infix expression \n')
        postfix = s.to_postfix(infix)
        print('\nPostfix is: ',postfix)
        print('\nAnswer is : ',s.evaluate_postfix(postfix))
        choice = int(input('Do you wish to continue 1 for yes and 0 for no '))
                
if(__name__ == '__main__'):
    main()
        
                        
                        
            
