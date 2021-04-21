'''The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.'''

n,m=list(map(int,input().split()))
n_list=list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))
# print(n,m,'\n',n_list,'\n',A,'\n',B)

hc=0
for i in n_list:
    if i in A:
        hc+=1
    elif i in B:
        hc-=1
print(hc)



