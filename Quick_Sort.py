def partition(lst,start,end):
    pivot = lst[start]
    p_index = start
    start+=1
    switch = True
    while(switch):
        while(start <= end and lst[start] <= pivot):
            start+=1
        while(start <= end and lst[end] >= pivot):
            end-=1
        if(start>end):
            switch = False
        else:
            lst[start],lst[end] = lst[end],lst[start]
    lst[p_index],lst[end] = lst[end],lst[p_index]
    return end


def quick_sort(lst,start,end):
    if(start<end):
        pivot_loc = partition(lst,start,end)
        quick_sort(lst,start,pivot_loc)
        quick_sort(lst,pivot_loc+1,end)


print('Enter a list to be sorted. ')
lst = list(map(int,input().split()))
start = 0
end = len(lst)-1
quick_sort(lst,start,end)
print(lst)
