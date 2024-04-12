import math
import string


def separate_characters(my_string: str) -> tuple:
    ascii_string = ""
    punctuation_string = ""
    other_string = ""

    for i in range(len(my_string)):
        if my_string[i] in string.ascii_letters:
            ascii_string = ascii_string + my_string[i]
            continue

        if my_string[i] in string.punctuation:
            punctuation_string = punctuation_string + my_string[i]
            continue

        other_string = other_string + my_string[i]

    return ascii_string, punctuation_string, other_string



if __name__ == "__main__":
    print(string.ascii_letters)