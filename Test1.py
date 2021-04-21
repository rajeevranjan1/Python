from itertools import combinations
s,k=input().split()
l=list(combinations(s,range(1,(int(k)+1))))
print(s,k)