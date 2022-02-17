from curses import COLOR_MAGENTA
import sys
import colorama
colorama.init(autoreset=True)

Number_of_tries = 10
word = "kochamnie"
used_letters = []

user_word = []

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    



    return indexes

###

for _ in word:
    user_word.append("")

while True:
    print("")
    letter = input(colorama.Fore.BLUE + "Give me letter: ")
    used_letters.append(letter)
    print("")

    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print(colorama.Fore.GREEN + "No letter in this word")
        Number_of_tries -=1
        print(colorama.Fore.RED + "Number_of_tries:", Number_of_tries)
        print(colorama.Back.CYAN + "You word still looks that:")
        print(user_word)

        if Number_of_tries == 0:
            print("Game over :-(")
            sys.exit(0)

    else:
        for index in found_indexes:
            user_word[index] = letter
        print(user_word)

        if "".join(user_word) == word:
            print(colorama.Fore.YELLOW + colorama.Back.GREEN + "Bravo You Win, This is this word")
            sys.exit(0)
            
    print("")
    print(colorama.Fore.CYAN + "Used letters:", used_letters)
    print("")




