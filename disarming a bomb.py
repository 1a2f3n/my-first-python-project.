
import random
print("welcome to the battle ship arena".capitalize())
mission = "your mission is to find the armor store and disarm the bomb!!"
print(mission)
print("you've arrive at the enemy camp!!".upper())
objective_1 = input("choose 'left' or right:\n").lower()
if objective_1 == "left":
    while True:
        objective_2 = input("you've entered the main building,choose a door to enter"
                            " blue door,yellow door or red door\n ").lower()
        if objective_2 == "yellow door":
            print("wrong door")
        elif objective_2 == "red door":

            print("you've arrive at the armor room!!."
                  "there is a password generator device,"
                  "enter the random code to generate password ")
            while True:
                p = random.randint(5, 10)
                print(f"use this {p} Random number to generate the password")
                random_num = int(input("enter generated random code: "))
                if random_num == p:
                    print("correct!!")
                    print(f"the password is: {random_num ** 5}")
                    break
                else:
                    print("wrong")
            generated_password = int(input("enter the generated password "
                                           "to disarm the bomb: "))
            if generated_password == random_num ** 5:
                print("bomb disarmed successfully".upper())
            else:
                print("wrong password..game over bomb exploded".upper())
                break
        else:
            print("game over!!.. you woke the dogs!".upper())
            break
else:
    print("game over..you where seen on camera".capitalize())
