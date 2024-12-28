### HANGMAN GAME ####
import string

# import all lowercase letters
chars = string.ascii_lowercase

# initialize the total lives
lives = 6
FINAL_LIVES = 6

# initialize a counter so if the player guesses all the correct letters to end the game
count = 0

# empty list to store all the letters
letters = []
for char in chars:
    letters.append(char)

# initialize the word
word = "olympiakos"
split_word = list(word)

# create the secret word based on the length of the given word
secret_word = ""
for i in range(len(word)):
    secret_word += "_"

# convert it to list
secret_word_list = list(secret_word)
# print(secret_word_list)
# check if the length of the secret word is correct
if len(secret_word) == len(word):
    print('OK')

else:
    print("NOT")

over = True
# begin the game
while over:
    print(f'Word to guess: {''.join(secret_word_list)}')
    players_guess = input("Guess a letter: ")
    if players_guess not in letters:
        print('Invalid character, please try again')
    else:
        if players_guess not in word:
            print(f'You guessed {players_guess}, that is not in word. You lose a life.')
            lives -= 1
            print(f'{lives}/{FINAL_LIVES} LIVES LEFT')
            # print(lives)
            if lives == 0:
                print('Game Over!')
                over = False
        elif players_guess in split_word:
            index = 0
            for char in split_word:
                if char == players_guess:
                    secret_word_list[index] = players_guess
                    if "_" not in secret_word_list:
                        print('You Won!')
                        over = False
                index = index + 1
print('End of Game!')
print(f'The word was: {word}')
