print('Enter a sorted list: ')
lst = list(map(int,input().split()))
val = int(input('Enter value to search : \n'))
start = 0
end = len(lst)-1
flag = 1 
while(start <= end):
    mid = (start + end)//2
    print(lst[mid])
    
    if(lst[mid] == val):
        print('Element found at ',mid+1,' position. \n')
        flag = 0
        break
    elif(val > lst[mid]):
        start = mid+1
    elif(val < lst[mid]):
        end = mid-1

if (flag):
    print('Element not found! ')
    

        
    
