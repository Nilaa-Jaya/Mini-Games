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

game_images = [rock, paper, scissors]

print("What do you choose? Enter 0 for Rock, 1 for Papers and 2 for Scissors     ")
user_choice = int(input())
if user_choice > 2 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])
    print("\nComputer chose:")
    import random

    comp_choice = random.randint(0, 2)
    print(game_images[comp_choice])

    if user_choice == comp_choice:
        print("Its a draw")
    elif user_choice == 0 and comp_choice == 2:
        print("You win")
    elif user_choice == 2 and comp_choice == 0:
        print("You lose")
    elif user_choice < comp_choice:
        print("You lose")
    elif user_choice > comp_choice:
        print("You win")
