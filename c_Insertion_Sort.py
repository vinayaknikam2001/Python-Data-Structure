print('Enter a list to be sorted. ')
lst = list(map(int,input().split()))
size = len(lst)
for i in range(1,size):
    switch = 0
    j = i-1
    key = lst[i]

    #Process of insering a key in sorted list
    while(j>= 0 and lst[j]>key):
        lst[j+1] = lst[j]
        switch = 1
        j -= 1
    #Adding key to j+1 position because j is already reduced
    if(switch):    
        lst[j+1] = key
                                                                        
print(lst)
