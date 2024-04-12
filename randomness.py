from random import randint
from random import shuffle
from random import choice
import string


def create_random_list_of_number(list_length: int) -> list:
    random_list = []

    for i in range(list_length):
        random_list.append(randint(0, 100))

    return sorted(random_list)


def binary_search(sorted_list: list, value: int) -> int:
    start = 0
    end = len(sorted_list) - 1

    while start <= end:
        guess = (start + end) // 2

        if sorted_list[guess] < value:
            start = guess + 1

        if sorted_list[guess] > value:
            end = guess - 1

        if sorted_list[guess] == value:
            return guess

    return -1


def filter_duplicate(list_int: list) -> list:
    filter_list = []

    for i in range(len(list_int)):
        if list_int[i] not in filter_list:
            filter_list.append(list_int[i])

    return filter_list


def lottery_numbers(amount: int, lower: int, upper: int) -> list:
    lottery_list = []
    for i in range(amount):
        lottery_list.append(randint(lower, upper))

    return lottery_list


def generate_password(length: int) -> str:
    possible_string = string.ascii_lowercase

    password = ""
    for i in range(length):
        password = password + possible_string[randint(0, len(possible_string) - 1)]

    return password


def shuffle_string(string: str) -> str:
    to_list = list(string)

    shuffle(to_list)

    return ''.join(to_list)


def check_existence(origin_str : str, dest_str: str) -> bool:
    for char in origin_str:
        if char in dest_str:
            return True
        
    return False



def generate_strong_password(length: int, is_number: bool, is_special_char: bool) -> str:

    possible_string = string.ascii_lowercase

    if is_number:
        possible_string = possible_string + string.digits

    if is_special_char:
        possible_string = possible_string + "!?=+-()#"

    
    while True:
        possible_string = shuffle_string(possible_string)

        if not check_existence(possible_string[0:7], string.ascii_lowercase):
            continue

        if  is_number == True and not check_existence(possible_string[0:7], string.digits):
            continue

        if is_special_char == True and not check_existence(possible_string[0:7], "!?=+-()#"):
            continue

        return possible_string[0:7]
    


if __name__ == "__main__":


    print("______")
