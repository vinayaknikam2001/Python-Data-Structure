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
        
    def reverse(self,string):
        rev = ''
        for i in string :
            if (i == '('):
                self.push(')')
            elif(i== ')'):
                self.push('(')
            else:
                self.push(i)
        for i in string:
            rev += self.pop()
        return rev

    def to_prefix(self,infix):
        infix = self.reverse(infix)
        if(len(infix)%2 ==0):
            print('invalid expression ! ')
            return 
        prefix = ''
        for i in infix:
            if(self.is_num(i)):
                prefix += i
                
            elif(i in ('+-*/^')):
                while(self.size != -1 and self.precedence[i] <= self.precedence[self.peek()]):
                    prefix += self.pop()
                self.push(i)

            elif(i == '('):
                self.push(i)
            elif(i == ')'):
                temp = self.pop()
                while(temp != '('):
                    prefix += temp
                    temp = self.pop()
                    
        while(self.size != -1):
            prefix += self.pop()

        return self.reverse(prefix)
    
    #Expression having 2 digit numbers can not be evaluated    
    def evaluate_prefix(self,prefix):
        for i in self.reverse(prefix):
            if (self.is_num(i)):
                self.push(i)
            else:
                operand1 = self.pop()
                operand2 = self.pop()
                result = self.calculate(operand1,i,operand2)
                self.push(result)
        return result

    def calculate(self,op1,i,op2):
        if (i == '+'):
            return (int(op1)+int(op2))
        if (i == '-'):
            return (int(op1)-int(op2))
        if (i == '*'):
            return (int(op1)*int(op2))
        if (i == '/'):
            return (int(op1)//int(op2))
        if (i == '^'):
            return (int(op1)**int(op2))
        
                
     
        
s = stack_class()
infix = input('Enter infix expresssion \n')
print('Reversed expression is: ',s.reverse(infix))
prefix = s.to_prefix(infix)
print('\nPrefix expression is: ',prefix)
print('\nAnswer is :',s.evaluate_prefix(prefix))




        
        
        











