def decorator(func):
    def wrapper():
        print("A wrapper function is running")
        func()
        print("Function executed inside wrapper. Coming out of wrapper")
    return wrapper

@decorator
def myName():
    print("Rajeev Ranjan")

myName()
