# nums=list(map(int,input("Enter numbers to add: ").split()))
nums=input("Enter numbers to add: ").split()
sum=0
errorFlag=0
for i in nums:
    try:
        sum+=int(i)
    except:
        errorFlag=1
if errorFlag==1:
    print(f"Sum of {nums} is {sum} skipping Non-Integers")
else:
    print(f"Sum of {nums} is {sum}")
input("Done...")
