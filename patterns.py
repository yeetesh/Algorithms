for i in range(5,0,-1):
    for j in range(i-1):
        print(' ',end='')
    for i in range(i-1,5):
        print('* ',end='')
    print()
print()
for i in range(0,-6,-1):
    for j in range(-5,i):
        print(' ',end=' ')
    for j in range(i,i*-1 + 1):
        print(abs(j),end=' ')
    print()
print()
data = 1
for i in range(1,6):
    for j in range(1,i+1):
        print(data,end=' ')
        data += 1
    print()
print()
for i in range(1,6):
    for j in range(6,i,-1):
        print(' ',end = ' ')
    for j in range(1,2*i):
        print(j,end=' ')
    print()

print()
for i in range(1,6):
    for j in range(5,i-1,-1):
        print(i,end='')
    print()
print()
for i in range(5,0,-1):
    for j in range(1,i):
        print(' ',end = '')
    count = 1
    for j in range(i,6):
        print(count,end='')
        count += 1
    print()
print()
for i in range(1,6):
    for j in range(1,6):
        if j <= i:
            print(j,end='')
        else:
            print(' ',end='')
    for j in range(5,0,-1):
        if j > i:
            print(' ',end='')
        else:
            print(j,end='')
    print()
print()
for i in range(1,5):
    for j in range(i*2-1):
        if j%2 == 0:
            print(i,end='')
        else:
            print('*',end='')
    print()

#pascal's triangle
for i in range(0,5):
    for j in range(4,i,-1):
        print(' ',end='')
    print(' '.join(list(str(11**i))))