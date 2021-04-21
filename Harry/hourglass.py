l=[]
for i in range(6):
    l.append([j for j in range(i*6,6*(i+1))])

# for i in l:
#     print(i)
listOFhg=[]
for i in range(4):
    for j in range(4):
        hgSum=(l[i][j]+l[i][j+1]+l[i][j+2]
        +l[i+1][j+1]
        +l[i+2][j]+l[i+2][j+1]+l[i+2][j+2])
        listOFhg.append(hgSum)
    
# print(listOFhg)
print(max(listOFhg))




