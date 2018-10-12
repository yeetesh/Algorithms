def find_steps(steps,total,selected):
    if total < 0:
        return
    if total == 0:
        print(selected)
        return
    for i in steps:
        selected.append(i)
        find_steps(steps,total - i,selected)
        selected.pop()

steps = [1,2,5]
total = 4
find_steps(steps,total,[])
