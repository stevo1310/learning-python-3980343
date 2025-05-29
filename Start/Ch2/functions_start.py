# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function
# def hello_func():
#   print("hello world!")
#   name = input("What is your name? ")
#   print("Nice to meet you,", name)

# function that takes parameters
# hello_func()

# function that returns a value
# def cube(x):
#   return x * x * x

# result = cube(3)
# print("The cube of 3 is:", result)

# function with default value for an parameter
# def hello_func(greeting, name=None):
#   print("hello world!")
#   if name == None:
#     name = input("What is your name? ")
#   print(greeting,name)

# hello_func("Hi")  # calling the function with a default name
  # calling the function with a default name
  # hello_func(greeting="Hi", name="Steven")

# function with variable number of parameters
def multi_add(start,*args):
    total = 0
    for a in args:
        total = total + a
    return total

print(multi_add(10,1, 2, 3, 4, 5))  # prints 15