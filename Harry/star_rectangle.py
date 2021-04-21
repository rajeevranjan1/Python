'''File for printing star pattern'''

def starRectangle(n):
    print('* ' * n,'\b','*',sep='')
    for i in range(2,n):
        print('*',' '*(2*n-4),'*')
    print('* ' * n,'\b','*',sep='')

starRectangle(18)
    