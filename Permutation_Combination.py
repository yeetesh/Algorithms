def permute(res,original):
    if len(original) == 0:
        print(res)
    for i in range(len(original)):
        permute(res + original[i],original[:i] + original[i+1:])
        

 
def subsets(index,solution,array):
    if index >= len(array):
        print(solution)
        return
    solution.append(array[index])
    subsets(index + 1,solution,array)
    solution.pop()
    subsets(index + 1,solution,array)
    
subsets(0,[],[1,2,3,4])
permute('','hel')