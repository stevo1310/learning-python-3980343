# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = [0,1,"two", 3.0, True]
print (len(mylist))  # length of the list



# to access a member of a sequence type, use []
print (mylist[2])
print (mylist[-1])  # get a slice of the list
mylist[0] = 100  # change a value in the list
print(mylist)


# add a list to another list
another_list = [4, 5, 6]
mylist = mylist + another_list
print(mylist)

#strings are also list just cannot be changed


# use slices to get parts of a sequence
print(mylist[1:4:2])  # get a slice of the list

# you can use slices to reverse a sequence
print(mylist[::-1])  # reverse the list

# Tuples are like lists, but they are immutable
mytuple = (0, 1, "two", 3.0, True)
print(mytuple[1])  # length of the tuple

# Sets are also sequences, but they contain unique values
myset = {0, 1, 2,2, 3.0, True}
print(myset)  # print the set



# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
print(1 in myset)  # check if a value is in the set
print(3 not in mytuple)  # check if a value is not in the set
print("two" in mylist)  # check if a value is in the tuple