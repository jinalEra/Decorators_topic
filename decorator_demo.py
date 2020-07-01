#function in function
def func():
    print("base function...")
    def func1():
        print("first inner function")
    def func2():
        print("second inner function")

    func1()
    func2()

func()