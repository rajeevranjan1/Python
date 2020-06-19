y=int(input("Enter number of Row (Odd number between 7 and 101: "))
x=y*3
count=3
fill='.|.'
for i in range(y):
    if i<y//2:
        print('-'*((x-count)//2)+fill*(2*i+1)+'-'*((x-count)//2))
        count +=6
        filltemp=2*i+1
    elif i==y//2:
        print('-'*((x-7)//2) + 'WELCOME' + '-'*((x-7)//2))
    else:
        count -=6
        print('-'*((x-count)//2)+fill*(filltemp)+'-'*((x-count)//2))
        filltemp -=2
        

        
