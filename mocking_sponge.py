##
# mocking_sponge.py
# Turns input into mock case. Not more than 3 continous of the same case
# Dago
# 2021-03-26
from random import randint


def uppercase(char):
    """
    Turn a character into upper or lower and return corresp bool
    """
    if randint(0, 1):
        new_char = char.upper()
        upper = True

    else:
        new_char = char.lower()
        upper = False

    return new_char, upper


def split_2d(string):
    """
    Returns a list. Items are the words (space split) that have been
    also split into a list.
    e.g. "how are ya" -> [["h", "o", "w"], ["a", "r", "e"], ["y", "a"]]
    """
    first_split = string.split(" ")

    # Go through each
    big_split = []
    for word in first_split:
        big_split.append(list(word))

    return big_split


def mock_case(word, prev_case=None):
    """
    Turns a iterable into mOcK CasE. Best output when input is a word
    e.g. "Hello" -> "hELlO"
    """
    # Set how many times a case can repeat
    LIMIT = 2

    # Counter will be used to check that the case doesnt repeat
    # consecutively more than the LIMIT
    counter = 0

    new_word = []

    for char in word:
        # Check that the character is a letter. Looking for A-Z || a-z
        if not char.isalpha():
            new_word.append(char)
            continue

        new_char, is_upper = uppercase(char)

        # Add to the counter if current and last case are the same
        if is_upper == prev_case:
            counter += 1

        if counter >= LIMIT:
            # Insert opposite case
            prev_case = not is_upper

            if is_upper:
                new_word.append(new_char.lower())

            else:
                new_word.append(new_char.upper())

        else:
            new_word.append(new_char)

            # Update
            prev_case = is_upper

    return ''.join(new_word), is_upper


def main():
    sentence = input("Give a sentence: ")
    split_sentence = sentence.split()

    # Passed to function to account for spaces
    prev_case = None

    # Process each word
    new_sentence = []
    for word in split_sentence:
        new_word, prev_case = mock_case(word, prev_case)
        new_sentence.append(new_word)

    print(' '.join(new_sentence))

    # spongebob
    spongebob = []
    print("""         *
          *
     ----//-------
     \..C/--..--/ \   `A
      (@ )  ( @) \  \// |w
       c          \  \---/
        HGGGGGGG   \    /`
        V `---------`--'
            <<    <<
           ###   ###""")

if __name__ == "__main__":
    main()
