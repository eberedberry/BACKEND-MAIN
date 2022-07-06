# ### rock paper scissor game
# import random
# def play_game(user:str, computer:str):
#     """This function plays the rock paper scissors gmae with the rules that:
#     scissors wins paper
#     rock wins scissor
#     paper wins rock

# Rock is represented as R
# Paoer  is represented as P
# Scissors  is represented as S

# Args:
#     user (str): This is the user's choice.
#     Computer(str): This is the computer's choice

#     Returns:
#     (str): This is the result of the game 
# """

#     if user  == "s" and computer =="p":
#         return "You Win"

#     elif user  == "p" and computer =="r":
#         return "You Win"

#     elif user  == "r" and computer =="s":
#         return "You Win"

#     elif user == computer:
#         return "Its a tie"
#     else:
#         "You Lose"



# print("welcome to to the rock paper scissor game ")
# print("Enter R for rock, s fo siccors  and p for paper")

# user = input("> :" ).lower()
# options = "rps"
# computer = random.choice(options)

# if user in options:
#     print(play_game(user, computer))
# else: 
#     print("invalid input")

# print(computer)

####INBUILT FUNCTIONS

# first_data = [2, 3, 4, 5,6 ,7 ]
# second = [5,6,7,8]

# zipped = zip(first_data, second)
# print(list(zipped))

# print(list(enumerate(first_data)))


# # array_of_salary, give a 10% raise
# arr = [50000, 435460, 675758, 4353, 5636]
# pay_raise = list(map(lambda x: x + (x * 0.1), arr))
# print(pay_raise)




# user = input("enter your numbers seperated by comma: ")
# answer = (user.split(","))
# # answer = list(map(lambda x: float(x), answer)) ### or use line 72
# answer = list(map(int, answer))
# result = sum(answer)/len(answer)
# print(answer)
# print(result)
# print(" ".join(a)) #USE SPACE TO JOIN THEM TOGETHER 

####### FILTER FUNCTION
a = range(1, 10)

odd = list(filter(lambda x: x % 2 == 1, a))
print(odd)
even = list(filter(lambda x: x % 2 == 0, a))
print(even)


my_set = {1,2,3,4,5,6,7,8,9}
my_set2 = {1,2,3,4,16,7,12,24}
my_set.discard(5)
print(my_set)

my_set.discard(100)
print(my_set)

my_set.remove(2)
print(my_set)

# my_set.remove(100)
print(my_set)

my_set.add(13)
print(my_set)



