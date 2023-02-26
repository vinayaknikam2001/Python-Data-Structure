import Infix_To_Postfix as p
class node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


class bst:
    def __init__(self):
        self.stack = []
        self.size = -1

    def push_stack(self,val):
        self.stack.append(val)
        self.size+=1

    def pop_stack(self):
        if(self.size == -1):
            return None
        self.size -= 1
        return self.stack.pop()
    
    def inorder(self,temp):
        if(temp!=None):
            self.inorder(temp.left)
            print(temp.data,' ',end='')
            self.inorder(temp.right)

    def preorder(self,temp):
        if(temp!=None):
            print(temp.data,' ',end='')
            self.preorder(temp.left)
            self.preorder(temp.right)

    def postorder(self,temp):
        if(temp!=None):
            self.postorder(temp.left)
            self.postorder(temp.right)
            print(temp.data,' ',end='')

    def evaluate(self,temp):
        if(temp.left!=None and temp.right!=None):
            temp.left.data = self.evaluate(temp.left)
            temp.right.data = self.evaluate(temp.right)
            temp.data = self.calculate(temp.left.data,temp.right.data,temp.data)
            return temp.data
        else:
            return temp.data

    def calculate(self,l,r,op):
        if(op == '+'):
            ans = int(l)+int(r)
        elif(op == '-'):
            ans = int(l)-int(r)
        elif(op == '*'):
            ans = int(l)*int(r)
        else:
            ans = int(l)/int(r)
        return ans
        
    
                
if(__name__ == '__main__'):
    infix = input()
    obj = p.stack_class()
    post = obj.to_postfix(infix)
    print(post)
    tree = bst()
    for i in post:
        if(i in '+-*/'):
            r = tree.pop_stack()
            l = tree.pop_stack()
            newnode = node(i)
            newnode.left = l
            newnode.right = r
            tree.push_stack(newnode)
        else:
            newnode = node(i)
            tree.push_stack(newnode)
    root = tree.pop_stack() 
    print(root.data)
    print('\nTree using inorder :\n')
    tree.inorder(root)
    print('\nTree using preorder :\n')
    tree.preorder(root)
    print('\nTree using postorder :\n')
    tree.postorder(root)
    print('Answer is :')
    print(tree.evaluate(root))
