#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def func1():
    print("I am a function")

# TODO: function that takes arguments
def func2(arg1,arg2):
    print(arg1," ",arg2)

# TODO: function that returns a value
def cube(x):
    return x*x*x
# TODO: function with default value for an argument
def power(num, X=1):
    result=1
    for i in range(X):
        result=result*num
        #result*=num
    return result

# TODO: function with variable number of arguments
def multi_add(*args):
    result =0
    for x in args:
        result = result + x
    return result

def multi_add1(arg1,*args):
    result =0
    for x in args:
        result = result + x
    result=result+arg1
    return result

# func1()
# print(func1())
# print(func1)

# func2(10,20)
# print(func2(10,20))
#print(func2)

#print(cube(3))
# print(power(2))
# print(power(2,3))

# print(power(X=3,num=2))
# print(multi_add(4,5,10,10))
print(multi_add(4,5,10,4,10))
print(multi_add1(4,5,10,4,10))
