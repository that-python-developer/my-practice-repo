# ####################################### 1 #####################################
# Python program to illustrate functions can be treated as objects

# def shout(text):
#     return text.upper()
#
#
# print(shout('Hello'))
#
# yell = shout
#
# print(yell('Hello'))


# ####################################### 2 #####################################
# Python program to illustrate functions can be passed as arguments to other functions

# def shout(text):
#     return text.upper()
#
#
# def whisper(text):
#     return text.lower()
#
#
# def greet(func):
#     # storing the function in a variable
#     greeting = func("""Hi, I am created by a function passed as an argument.""")
#     print(greeting)
#
#
# greet(shout)
# greet(whisper)


# ####################################### 3 #####################################
# Python program to illustrate functions can return another function

# def create_adder(x):
#     def adder(y):
#         return x + y
#
#     return adder
#
#
# add_15 = create_adder(15)
#
# print(add_15(10))

# ####################################### 3 #####################################

# # defining a decorator
# def hello_decorator(func):
#     # inner1 is a Wrapper function in
#     # which the argument is called
#
#     # inner function can access the outer local
#     # functions like in this case "func"
#     def inner1():
#         print("Hello, this is before function execution")
#
#         # calling the actual function now
#         # inside the wrapper function.
#         func()
#
#         print("This is after function execution")
#
#     return inner1
#
#
# # defining a function, to be called inside wrapper
# def function_to_be_used():
#     print("This is inside the function !!")
#
#
# # passing 'function_to_be_used' inside the
# # decorator to control its behaviour
# function_to_be_used = hello_decorator(function_to_be_used)
#
# # calling the function
# function_to_be_used()

# ####################################### 4 #####################################


# def hello_decorator(func):
#     def inner1(*args, **kwargs):
#         print("before Execution")
#
#         # getting the returned value
#         returned_value = func(*args, **kwargs)
#         print("after Execution")
#
#         # returning the value to the original frame
#         return returned_value
#
#     return inner1
#
#
# # adding decorator to the function
# @hello_decorator
# def sum_two_numbers(a, b):
#     print("Inside the function")
#     return a + b
#
#
# a, b = 1, 2
#
# # getting the value through return of the function
# print("Sum =", sum_two_numbers(a, b))

# ####################################### 4 #####################################

def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner


def decor(func):
    def inner():
        x = func()
        return x + x
    return inner


@decor1
@decor
def num():
    return 10


print(num())
