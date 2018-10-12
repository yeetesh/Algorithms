import random

array = []

for i in range(25):
    array.append(random.randint(1,1000))

def merge(array,left,right,l,r):
    i,j,k = 0,0,0
    while i < l and j < r:
        if left[i] < right[j]:
            array[k] = left[i]
            k += 1
            i += 1
        else:
            array[k] = right[j]
            k += 1
            j += 1
    while i < l:
        array[k] = left[i]
        i += 1
        k += 1
    while j < r:
        array[k] = right[j]
        j += 1
        k += 1
        
def sort(array,n):
    if n <= 1:
        return
    mid = n // 2
    left = array[:mid]
    right = array[mid:]
    sort(left,mid)
    sort(right,n - mid)
    merge(array,left,right,len(left),len(right))
    
sort(array,len(array))
print(array)