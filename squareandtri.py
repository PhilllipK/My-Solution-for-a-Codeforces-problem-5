t = int(input())

for z in range(t):
    n = int(input())
    grid = []
    for i in range(n):
        row = input()
        grid.append(row)
    
    rowc = [0] * n
    for i in range(n):
        count = 0
        for l in range(n):
            if grid[i][l] == "1":
                count += 1
        rowc[i] += count
    torem = 0
    
    for i in range(n):
        if rowc[i] == 0:
            torem += 1
    
    for i in range(torem):
        rowc.remove(0)
    
    rowc.sort()
    triangle = True
    for i in range(1,len(rowc)):
        if rowc[i]-2 != rowc[i-1]:
            triangle = False
    
    if triangle == True:
        print("TRIANGLE")
    else:
        print("SQUARE")
        
            
            