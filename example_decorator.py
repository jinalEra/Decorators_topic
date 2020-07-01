def func1(func):
    def wrapper(*args, **kwargs):
        print("it works")
    return wrapper

@func1
def func2(name):
    print(f"{name}")

func2("jinal")