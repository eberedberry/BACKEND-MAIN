####### GUESS GAME

import random as rd

num = list(range(63,74))
rd.shuffle(num)
print("""Welcome to Guess Game
        How many times do you want to play?
       """)
max_trial = int(input("Max is 5 trials > "))
if max_trial > 5:
    max_trial = 5


while max_trial > 0:
    print(f"you have {max_trial} left")
    print(num)
    gamer_choice = int(input("Please pick a number > "))
    comp_choice = rd.choice(num)
    # comp_choice = 67

    if gamer_choice in num:
        if gamer_choice == comp_choice: 
            print("You Win!\n")
            max_trial += 2
            
        elif gamer_choice > comp_choice:
                print("Too High!")
                print(f"{comp_choice}\n")
                max_trial -= 1

        else:
                print("Too Low!\n")
                print(f"{comp_choice}\n")
                max_trial -= 1
    else:
        print("Invalid Input\n")
       
    max_trial -= 1

    if max_trial <= 0:
        print("""OUT OF TRIALS
        Do you want to keep playing?
            """)
        gamer_decision = (input("Choose Yes or No > ")).lower()
        if gamer_decision == "yes":
            new_max_trial = int(input("How many times do you want to play? Max is 4 trials > "))
            if new_max_trial > 4:
                max_trial = 4
            else:
                max_trial = new_max_trial
        else:
            print("Bye")
            break



