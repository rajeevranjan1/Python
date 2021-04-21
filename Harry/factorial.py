def factorialI(number):
    '''fact(n)=1*2*3*....*n
    fact(0)=1
    '''
    fact=1
    for i in range(number):
        fact=fact*(i+1)
    return fact

n=int(input("Enter a number: "))
factorial=factorialI(n)
print(f"Factorial of {n} is {factorial}")


    