import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# This list contains the ASCII art for each game object
game_images = [rock, paper, scissors]

# Prompt the user to choose rock, paper or scissors
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))

# Check if user input is valid
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!") 
else:
    # Print the ASCII art for the user's chosen object
    print(game_images[user_choice])

    # Generate a random choice for the computer
    computer_choice = random.randint(0,2)
    
    # Print the ASCII art for the computer's chosen object
    print("Computer chose: ")
    print(game_images[computer_choice])
    
    # Determine the winner based on the game logic
    if user_choice == 0 and computer_choice ==2:
        print("You Win!")
    elif computer_choice == 0 and user_choice ==2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You Win!")
    elif computer_choice == user_choice:
        print("It's a draw")
        
