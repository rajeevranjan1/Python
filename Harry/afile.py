def kw(**kwargs):
    print(type(kwargs))
    for i,k in kwargs.items():
        print(i,k)

kw(rajeev=5,shivam=10)

def add(*args):
    print(type(args))

add(1,2,3,4)





