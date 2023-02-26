print('Enter a space separated list to be sorted. ')
lst = list(map(int,input().split()))
size = len(lst)
i = 0
while(i<size):
    j = i+1
    while(j<size):
        if(lst[i] > lst[j]):
            lst[i] = lst[j]+lst[i]
            lst[j] = lst[i]-lst[j]
            lst[i] = lst[i]-lst[j]
        j += 1
    i += 1
print(lst)
