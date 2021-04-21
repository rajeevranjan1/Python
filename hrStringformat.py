def print_formatted(n):
    width = len("{0:b}".format(n))
    for i in range(1,n+1):
      print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))
    # width=len(str(bin(number)))-2
    # print(width)
    # for i in range(1,number+1):
    #     print(i,oct(i)[2:].rjust(width,' '),hex(i)[2:].upper().rjust(width,' '), bin(i)[2:].rjust(width,' '))
    
print()