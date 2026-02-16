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

outcomes = [rock, paper, scissors]

x = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

if x >= 0 and x<=2:
    print(outcomes[x])

computer_choice = random.randint(0,2)
print("Computer chose:")
print(outcomes[computer_choice])

if x == computer_choice:
    print("It's a tie!")
elif x == 0 and computer_choice == 2:
    print("You win!")
elif x == 1 and computer_choice == 0:
    print("You win!")
elif x == 2 and computer_choice == 1:
    print("You win")
else:
    print("You lose")

