# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int, input().split())
mid1 = (m-3)//2
mid2 = mid1+3
cent = (n-1)//2
i = 0
while(i<cent):
    j = 0
    while(j<m):
        if(j<mid1 or j>=mid2):
            print('-',end='')
            j+=1
        else:
            print('.|.',end='')
            j+=3
    print('')
    mid1 -= 3
    mid2 += 3
    i+=1
i = 0
mid = (m-7)//2
while(i<m):
    if(i<mid or i>=mid+7):
        print('-',end='')
        i+=1
    else:
        print('WELCOME',end='')
        i+=7
print('')
i = 0
mid1 += 3
mid2 -= 3
while(i<cent):
    j = 0
    while(j<m):
        if(j<mid1 or j>=mid2):
            print('-',end='')
            j+=1
        else:
            print('.|.',end='')
            j+=3
    print('')
    mid1 += 3
    mid2 -= 3
    i+=1
    
        
        
