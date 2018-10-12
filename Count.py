import random

array = []

for i in range(10):
    array.append(random.randint(0,10))

k = max(array)

indices = [0]*(k+1)

print(array)

for i in range(len(array)):
    indices[array[i]] += 1

for i in range(1,k+1):
    indices[i] = indices[i-1] + indices[i]
print(indices)
        
final = [0]*len(array)

for i in range(len(array)):
    final[indices[array[i]] - 1] = array[i]
    indices[array[i]] -= 1
    
print(final)