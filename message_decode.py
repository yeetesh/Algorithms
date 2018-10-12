def decode(lengths,message,index):
    if index == len(message):
        return 1
    if message[index] == 0 or index > len(message):
        return 0
    total = 0
    for i in lengths:
        if i == 2 and len(message[index:index+i]) >= 2:
            if int(message[index:index+i]) > 26:
                return 0
        total += decode(lengths,message[index+i:],index)
    return total 

lengths = [1,2]
message = '111'
print(decode(lengths,message,0))