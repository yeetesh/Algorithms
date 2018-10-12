import copy
def find_max_gold(matrix,i,j,path,max_path,gold,max_gold):
    if i == len(matrix) or j == len(matrix) or matrix[i][j] == -1:
        return 
    path.append([i,j])
    if i == len(matrix) - 1 and j == len(matrix)- 1:
        if gold > max_gold[0]:
            max_path[0] = path
            if matrix[i][j] == 1:
                print(gold + 1,path)
                max_gold[0] = gold + 1
            else:
                print(gold,path)
                if gold > max_gold:
                    max_gold[0] = gold
    find_max_gold(matrix,i+1,j,path,max_path,gold + matrix[i][j],max_gold)
    find_max_gold(matrix,i,j+1,path,max_path,gold + matrix[i][j],max_gold)
            
    if(len(path) > 0):
        path.pop()

matrix = [[0,1,-1],[1,0,-1],[1,1,1]]
max_gold = [0]
max_path = [0]
find_max_gold(matrix,0,0,[],max_path,0,max_gold)
print(max_path,max_gold)




