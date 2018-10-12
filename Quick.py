import random

array = []

for i in range(25):
    array.append(random.randint(-100,1000))

def partition(array,l,h):
    pivot = array[h]
    i = l
    j = h - 1
    while(i < j):
        while(i < h and array[i] < pivot):
            i += 1
        while(j > l and array[j] >= pivot):
            j -= 1
        if i < j:
            array[i],array[j] = array[j],array[i]
    array[i],pivot = pivot,array[i]
    return i

def sort(array,l,h):
    if l >= h:
        return 
    pivot_index = partition(array,l,h)
    sort(array,l,pivot_index-1)
    sort(array,pivot_index + 1,h)

sort(array,0,len(array) - 1)

print(array)