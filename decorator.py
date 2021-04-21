def decorate(fun):
    def wrap(a):
      print('*'*20)
      fun(a)
      print('*'*20)
    return wrap


@decorate
def hello(name):
    print(f"Hello, {name}!")


print(hello.__name__)
hello("Rajeev")

def add(*args):
    sum=0
    print(type(args))
    for i in args:
        sum+=i
    print(sum)

add(2,3,4,5,6,7,8)
