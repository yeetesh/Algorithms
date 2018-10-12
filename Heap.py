import random

array = []

for i in range(20):
    array.append(random.randint(1,500))

def heapify(array,i,n):
    left = 2*i + 1
    right = 2*i + 2
    largest = i
    if left < n and array[left] > array[largest]:
        largest = left
    if right < n and array[right] > array[largest]:
        largest = right
    if largest != i:
        array[i],array[largest] = array[largest],array[i]
        heapify(array,largest,n)
            
def make_heap(array):
    for i in range(len(array)//2,-1,-1):
        heapify(array,i,len(array))

def sort(array,n):
    make_heap(array) 
    for i in range(n,-1,-1):
        array[0],array[i] = array[i],array[0]
        heapify(array,0,i)
    
sort(array,len(array) - 1)
print(array)