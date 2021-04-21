import pickle
l=[12,3,4,5,6,7,8,9,10]
with open("abc.txt",'ab') as f:
    pickle.dump(l,f)
    
with open('abc.txt','rb') as f:
    l2=pickle.load(f)
print(l2)