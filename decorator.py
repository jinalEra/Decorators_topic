# #decorators
# def func1(name):
#     return f"hello {name}"
#
# def func2(name):
#     return f"{name} , How you doin?"
#
#
# #here func4 is argument and we are put the any function in a place of func4
# def func3(func4):
#     return func4('jinal')
#
# print(func3(func1))
# print(func3(func2))

def greeting1(person):
    return f"Hiii, {person} Good Morning"

def greeting2(person):
    return f"hello, {person} Good AFternoon"

# print(greeting1('jinal'))
# print(greeting2('rubby'))

def outer(inner_argu):
    return inner_argu("jinal")

print(outer(greeting1))
print(outer(greeting2))
