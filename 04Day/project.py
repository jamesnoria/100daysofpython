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

game_images = [rock, paper, scissors]

user_choice = int(input('What do you choose?\n[0] Rock\n[1] Paper\n[2]Scissors\n=> '))
computer_choice = random.randint(0,2)

while user_choice > 2 or user_choice < 0:
    user_choice = int(input('What do you choose?\n[0] Rock\n[1] Paper\n[2]Scissors\n=> '))
    int(user_choice)

print(f'User chose: {game_images[user_choice]}')
print(f'Computer chose: {game_images[computer_choice]}')

if user_choice == 0 and computer_choice == 2:
    print('WIN')
elif computer_choice == 0 and user_choice == 2:
    print('LOSE')
elif computer_choice > user_choice:
    print('LOSE')
elif user_choice > computer_choice:
    print('WIN')
elif computer_choice == user_choice:
    print('Es un empate!!')
else:
    print('NOT VALID, LOSER!')


