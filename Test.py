def fun():
    try:
        print(x)
        print("try inside function")
    except NameError:
        print("Except inside the function")
    print("Inside the function")
try:
    fun()
    print("Main")
except NameError:
    print("Name Error is captured")