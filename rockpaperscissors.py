import random 

while 1:
    print("---------Users Turn---------")
    choice = (input("Enter rock/paper/scissors: ")).lower
    if choice != 'rock' or 'paper' or 'scissors':
        print("Invalid Choice!")
        again = input("Play Again? (y/n): ")
        if again == 'n' or again == 'N':
            break
            
    
    print("---------Computer's Turn---------")
    robot_choice = random.randint(1,3)

    if robot_choice == 1:
        robot_choice = "rock"
    elif robot_choice == 2:
        robot_choice = "paper"
    elif robot_choice == 3:
        robot_choice = "scissors"
    

    if choice == robot_choice:
        print("That round ended in a tie!")
        again = input("Play Again? (y/n): ")
        if again == 'n' or again == 'N':
            break
    elif choice == 'rock' and robot_choice == 'paper':
        loser = choice
    elif choice == 'paper' and robot_choice == 'rock':
        loser = robot_choice
    elif choice == 'scissors' and robot_choice == 'paper':
        loser = robot_choice
    elif choice == 'paper' and robot_choice == 'scissors':
        loser = choice
    elif choice == 'rock' and robot_choice == 'scissors':
        loser = robot_choice
    elif choice == 'scissors' and robot_choice == 'rock':
        loser = choice
    
    if loser == choice:
        print("The Computer Wins! You chose: " + choice + " and Computer Chose: " + robot_choice)
        again = input("Play Again? (y/n): ")
        if again == 'n' or again == 'N':
            exit
    if loser == robot_choice: 
        print("The User Wins! Computer chose: " + robot_choice + " and You Chose: " + choice)
        again = input("Play Again? (y/n): ")
        if again == 'n' or again == 'N':
            exit
