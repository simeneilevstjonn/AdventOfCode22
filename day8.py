matrix = open("data8.txt","r").read().split("\n")
maxScenic = 0

for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        treeHeight = matrix[y][x]
        left = matrix[y][:x][::-1]
        right = matrix[y][x+1:]
        top = [i[x] for i in matrix[:y]][::-1]
        bottom = [i[x] for i in matrix[y+1:]]
        #print(left, right, top, bottom, sep="\n", end="\n\n")

        a = 1
        if len(left) == 0 or len(right) == 0 or len(top) == 0 or len(bottom) == 0:
            continue
        i = 0
        while i < len(left) and left[i] < treeHeight:
            i+=1
        a*=i + (0 if i == len(left) else 1)
        
        i = 0
        while i < len(right) and right[i] < treeHeight:
            i+=1
        a*=i + (0 if i == len(right) else 1)

        i = 0
        while i < len(top) and top[i] < treeHeight:
            i+=1
        a*=i + (0 if i == len(top) else 1)

        i = 0
        while i < len(bottom) and bottom[i] < treeHeight:
            i+=1
        a*=i + (0 if i == len(bottom) else 1)
        
        maxScenic = max(maxScenic, a)

print(maxScenic)