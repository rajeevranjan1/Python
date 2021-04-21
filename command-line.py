import sys
print(f"The program's name is {sys.argv[0]}")
print(f"There are {len(sys.argv)} command line arguments: {sys.argv[1:-1]} and {sys.argv[-1]} ")
