import random
import hangman_art
import words


chosen_word = random.choice(words.word_list)
print(chosen_word)
lives = 6
placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
win = False
correct_letters = []


while not game_over:
    guess = input("Guess a letter ").lower()

    display = ""

    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print("\n")
        print("You lose a life")
        if lives == 0:
            game_over = True
            print("You lose!")

    if "_" not in display:
        game_over = True
        win = True
        print("You win")

    if not win:
        print(hangman_art.stages[lives])
        print("Lives left: ", lives)