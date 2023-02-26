#This program is dependent on another tree program!!!!!
#Postfix_Evaluation_BST





import Postfix_Evaluation_BST as p
class BST:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        
    def insert(self,val):
        if(self.data == None):
            self.data = val
            return
        if(self.data == val):
            print('Duplicate nodes are not allowed. ')
            return
        if(val < self.data):
            if(self.left != None):
                self.left.insert(val)
            else:
                self.left = BST(val)
        elif(val > self.data):
            if(self.right != None):
                self.right.insert(val)
            else:
                self.right = BST(val)
                
    def search(self,val):
        if(self.data == val):
            print(f'Value {val} is present in a tree.')
            return
        if(val <self.data):
            if(self.left):
                self.left.search(val)
            else:
                print('Value is not present in the tree.')
        else:
            if(self.right):
                self.right.search(val)
            else:
                print('Value is not present in the tree.')

    def delete(self,val,curr):
        if(self.data==None):
            print('Tree is empty! ')
            return
        if(val < self.data):
            if(self.left!=None):
                self.left = self.left.delete(val,curr)
            else:
                print('Value is not present in tree. ')
        elif(val > self.data):
            if(self.right!=None):
                self.right = self.right.delete(val,curr)
            else:
                print('Value is not present in tree. ')
        else:
            if(self.left==None):
                temp = self.right
                if(val == curr):
                    self.data = temp.data
                    self.left = temp.left
                    self.right = temp.right
                self = None
                return temp
            if(self.right==None): 
                temp = self.left
                if(val == curr):
                    self.data = temp.data
                    self.left = temp.left
                    self.right = temp.right
                self = None
                return temp
            node = self.right 
            while (node.left):
                node = self.left
            self.data = node.data
            self.right = self.right.delete(node.data,curr)
        return self

    def smallest(self):
        if(self.data == None):
            print('Tree is empty! ')
            return
        else:
            if(self.left != None):
                self.left.smallest()
            else:
                print('Minimum(smallest) value in tree is: ',self.data)
                return self.data

    def largest(self):
        if(self.data == None):
            print('Tree is empty! ')
            return
        else:
            if(self.right != None):
                self.right.largest()
            else:
                print('Maximum(largest) value in tree is: ',self.data)
                return self.data




def size(root):
    if(root == None):
        s = 0
        return s
    else:
        s = 1+size(root.left)+size(root.right)
        return s

tree1 = BST(None)
print('Enter a list to be inserted in Binary search tree. \n')
lst = [int(x) for x in  input().split()]
for i in lst:
    tree1.insert(i)

obj = p.bst()
print('\npost: ')
obj.postorder(tree1)
print('\n\npre: ')
obj.preorder(tree1)
print('\n\nino: ')
obj.inorder(tree1)
ch = 1
while(ch):
    ch = int(input('\nEnter your choice 0>Quit 1>Insert 2>Search 3>Delete 4>Pre 5>Post 6>Ino 7>Smallest 8>Largest 9>Size :'))
    if(ch ==0):
        print('\n Program terminated! ')
    elif(ch ==1):
        val = int(input('\n Enter the value to insert : '))
        tree1.insert(val)
    elif(ch==2):
        val = int(input('\n Enter the value to search : '))
        tree1.search(val)
    elif(ch==3):
        if(size(tree1)==1):
            print('Tree has only one node it can not be deleted! ')
        else:
            val = int(input('\n Enter the value to delete : '))        
            tree1.delete(val,tree1.data)
    elif(ch==4):
        print('\n Preorder traversal is :\n')
        obj.preorder(tree1)
    elif(ch==5):
        print('\n Postorder traversal is :\n')
        obj.postorder(tree1)
    elif(ch==6):
        print('\n Inorder traversal is :\n')
        obj.inorder(tree1)
    elif(ch==7):
        tree1.smallest()
    elif(ch==8):
        tree1.largest()
    elif(ch==9):
        print('Size of BST is : ',size(tree1))
        
                
            
        
        
