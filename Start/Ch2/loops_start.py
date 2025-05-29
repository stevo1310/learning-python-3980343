# LinkedIn Learning Python course by Joe Marini
# Example file for working with loops


x = 0

# define a while loop
#while x < 5:
  #  print("x is currently:", x)
   # x += 1  # increment x by 1

# answer = input("Do you want to continue? (yes/no)")
# while answer != "yes":
#      print(answer)
#      answer = input("Do you want to continue? (yes/no)")
   
# define a for loop
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# for day in days:
#     print("Today is:", day) 

# use a for loop over a collection
# for day in days:
#    if(day == "Wednesday"):
#       break
#    print(day)

# for day in days:
#  if(day == "Thursday"):
#     continue
#  print(day)


# use the break and continue statements
for i,d in enumerate(days):
  print(i, d)

# using the enumerate() function to get an index and an item
