# CREATE A FUNCTION TO TAKE IN CERTAIN VARIABLES 

def remove_string(new_string , n):
    print(new_string[0: n])

remove_string("DEVELOPMENT", 7)
remove_string("SCHOOLBUS", 3)

def remove_char(word , n):
    x = word[n:]
    print(x)

remove_char("chidiebere", 5)

# CONDITIONAL STATEMENTS
num = 37

if num > 32:
    print(5)

elif num > 23:
    print(10)

else:
    print(4)

if num > 23:
    print(10)

# INPUT 
data = input("Enter your name: ")
print(type(data))
print(data.upper())

data = int(input("Enter your age:"))
if data >= 18:
    print("You can vote")
else:
    print("Go back to your house. No be small children ")