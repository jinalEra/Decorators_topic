def function1(func):
    def wrapper():
        print("hello")
        func()
        print("Welcome, on python edureka....\n --------------")
    return wrapper

@function1
def function2():
    print("pythoninsta")


# function2 = function1(function2)
#
function2()

#exa : 2
def base(argu):
    def derive():
        print("amount ")
        argu()
        print("your total amount")
    return derive

@base
def child():
    print("30000")

child()