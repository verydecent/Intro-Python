# Write a function is_even that will return true if the passed in number is even.
def is_even(x):
  if x % 2 == 0:
    print("{} is Even!".format(x))
  else:
    print("{} is Odd!".format(x))
# Read a number from the keyboard
num = input("Enter a number: ")
# Print out "Even!" if the number is even. Otherwise print "Odd"
is_even(int(num))


# Write a function is_even that will return true if the passed in number is even.
def is_even(x):
    return (x % 2) == 0

# Read a number from the keyboard
num = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"
# ternary
num = int(num)

if is_even(num):
    print("Even!")
else:
    print("Odd")