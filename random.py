import time

def genRand(high):
    return int(time.time()%high)

print(genRand(10))

rnum=[]
for i in range(10):
    rnum.append(genRand(10))

print(rnum)

    
