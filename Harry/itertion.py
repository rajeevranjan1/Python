class IterClass:
    def __init__(self,stop):
        self.num=1
        self.stop=stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=self.stop:
            val = self.num
            self.num+=1
            return val
        else:
            raise StopIteration

it=IterClass(50)

for i in it:
    print(i)



# num=[x+3 for x in range(5) ]

# it=iter(num)
# print(it.__next__())
# print(next(it))

# # print(num)