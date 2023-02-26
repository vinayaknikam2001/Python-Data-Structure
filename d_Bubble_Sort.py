print('Enter a list to be sorted. \n')
lst = list(map(int,input().split()))
size = len(lst)
for i in range(size-1):
    for j in range(size-1):
        if(lst[j]>lst[j+1]):
            lst[j] = lst[j]+lst[j+1]
            lst[j+1] = lst[j]-lst[j+1]
            lst[j] = lst[j]-lst[j+1]

print(lst)
