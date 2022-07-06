# # write a program to check if a number is even number 

# person = input("Nationality ").lower()

# if person == "french" or person == "francais" :
#     name = input("comment tu t'appelle? ").title()
#     going_to_school = input("Allez-vous a l'ecole? ")

#     if going_to_school == "yes" :
#         print(f"Bienvenue chez au Univelcity, {name}.")
#     else:
#         print(f"Au revoir, {name}. Bonne Journee.")

# elif person == "italian":
#     print("Preferisci Parlare Italiano?")
# else:
#     print("You are neither French nor Italian.")
#     print("So, let us speak English!")

### RECURSION

# def factorial(n): 
#     if n == 1:
#         return 1

#     return n * factorial(n-1)

# print(factorial(7))

####INBUILT MODULES

import random as rd
# name = ["desmond", 3, 4, 7, 65, 21] 
# rd.shuffle(name)
# print(name)

# name = "Desmond"
# print(rd.choice(name))

#OR
##justs importing only the method you need so you dont need to add random or rd in front of choice
# from random import choice 
# name = "Desmond"
# print(choice(name))


###INBUILT FUNCTIONS
### range(start, stop, step)
###slicing    [start: stop: steps]
# print(list(range(2, 10, 2)))

#####LIST
# my_list = [4, 3, 5, 7, 36, 7]
# print(my_list[2:5])
# print(my_list)

# my_list[3] = 90  ##reassigning element at index 3 from 7 to 90
# print(my_list)

# num = list(range(50,53805))
# rd.shuffle(num)
# min(num)
# max(num)
# print(sorted(num, reverse=True)[:5])
# print(sorted(num)[-5:])

####### GUESS GAME
# num = list(range(63,74))
# rd.shuffle(num)
# print("Welcome to Guess Game")
# for i in range(1,4):
#     print(num)
#     gamer_choice = int(input("Please pick a number > "))
#     comp_choice = rd.choice(num)
#     # comp_choice = 67

#     if gamer_choice in num:
#         if gamer_choice == comp_choice:
#             print("You Win!")
#             break
#         else:
#             if gamer_choice > comp_choice:
#                 print("Too High!")
#                 print(comp_choice)
#             else:
#                 print("Too Low!")
#                 print(comp_choice)
#     else:
#         print("Invalid Input")

###### LIST OPERATIONS
# list1 = [4, 3

###### ROCK, PAPER, SCISSORS

print("Welcome to Rock , Paper , Scissor Game!!")

gamer_choice =  input("Choose one: ROCK , PAPER or SCISSORS :").lower()
comp_choice = ["rock", "paper", "scissors"]
# rd.shuffle(comp_choice)
comp_choice = rd.choice(comp_choice)
print(f"comp_choice {comp_choice}")
print(gamer_choice)

if gamer_choice == "rock" and comp_choice == "scissors":
    print("You win")

elif gamer_choice == "scissors" and comp_choice == "paper":
    print("You win")

elif gamer_choice == "paper" and comp_choice == "rock":
    print("You win")

elif gamer_choice == "paper" and comp_choice == "scissors":
    print("You Lose!")

elif gamer_choice == "scissors" and comp_choice == "rock":
    print("You Lose") 

elif gamer_choice == "rock" and comp_choice == "paper":
    print("You Lose!")      

elif gamer_choice == comp_choice:
    print("It's a Draw")
else:
    "Invalid input"

    