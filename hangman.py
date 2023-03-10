import random
from words import words
MAX_HINTS = 2  # set maximum number of hints allowed

def choose_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = choose_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set('abcdefghijklmnopqrstuvwxyz'.upper())
    used_letters = set()  # what the user has guessed
    hint_used = 0  # counter for number of hints used

    lives = 6 # total number of chance to guess the word

    # getting user input
    while len(word_letters) > 0 and lives > 0:

        print('Lives remaining:', lives,
              ' You have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_input = input('Guess a letter or type "hint" for a hint: ').upper()
        if user_input == "HINT":
            print('You can used only two hints.')
            if hint_used < MAX_HINTS:
                hint_used += 1
                hint_letter = random.choice(list(word_letters))
                print(f"Hint: the word contains the letter '{hint_letter}'")
            else:
                print("Sorry, you have used up all your hints.")
                continue  # go back to the beginning of the loop

        elif user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
                print('')

            else:
                lives -= 1  # takes away a life if wrong
                print('\nYour letter,', user_input, 'is not in the word.')

        elif user_input in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\n Invalid character.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('Congrats! You guessed the word', word, '!')


hangman()