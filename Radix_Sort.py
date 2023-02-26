#Radix sort and counting sort doesn't work on the -ve numbered list.
def radix_sort(lst,n):
    maxx = max(lst)
    place = 1
    while(maxx//place>0):
        counting_sort(lst,n,place)
        print('Bucket ',lst)
        place*=10


def counting_sort(lst,n,place):
    count = [0]*10
    ans = [0]*n
    for i in range(n):
        digit = (lst[i]//place)%10
        count[digit]+=1
    for j in range(1,10):
        count[j]+=count[j-1]
    i=n-1
    while(i>=0):
        digit = (lst[i]//place)%10
        count[digit]-=1
        ans[count[digit]] = lst[i]
        i-=1
    for i in range(n):
        lst[i]= ans[i]
    
    

lst = [int(x) for x in input().split()]
size = len(lst)
radix_sort(lst,size)
print('answer ',lst)
