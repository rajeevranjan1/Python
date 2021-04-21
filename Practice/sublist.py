# from itertools import combinations
# l=[1,2,3]
# x=[]
# for i in range(1,len(l)+1):
#     x.append(list(combinations(l,i)))
# print(x)
##--------ABOVE CODE USES LIBRARY FUNCTION--------##

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield list(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield list(pool[i] for i in indices)

# x=[]
# for i in range(1,len(l)+1):
#     x.append(list(combinations(l,i)))
# print(x)

# function to generate all the sub lists
def sub_lists (l):
    # base = []  
    lists = [[],]
    for i in range(len(l)):
        orig = lists[:]
        new = l[i]
        for j in range(len(lists)):
            lists[j] = lists[j] + [new]
        lists = orig + lists
          
    return lists

# driver code
l1 = [1, 2, 3]
print(sub_lists(l1))
