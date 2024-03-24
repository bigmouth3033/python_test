def list_of_star(list_integer):
    for number in list_integer:
        str = ""
        for i in range(number):
            str = str + "*"
        print(str)


def anagrams(first_str, second_str):
    sorted_first_list = sorted(list(first_str))
    sorted_second_list = sorted(list(second_str))

    if sorted_first_list == sorted_second_list:
        return "They are anagrams"
    else:
        return "They are not anagrams"


def palindromes(str):
    if str == str[::-1]:
        return True
    return False


def sum_of_positives(list):
    sum = 0
    for number in list:
        if number > 0:
            sum += number

    return sum


def even_numbers(list):
    new_list = []

    for number in list:
        if number % 2 == 0:
            new_list.append(number)

    return new_list


def list_sum(first_list, second_list):
    new_list = []
    for i in range(len(first_list)):
        new_list.append(first_list[i] + second_list[i])

    return new_list


def distinct_numbers(list):
    new_list = []

    for number in list:
        if number not in new_list:
            new_list.append(number)

    return sorted(new_list)


def length_of_longest(list):
    max_length = 0

    for string in list:
        if len(string) > max_length:
            max_length = len(string)

    return max_length


def shortest(list):
    shortest_string = list[0]

    for string in list:
        if len(string) < len(shortest_string):
            shortest_string = string

    return shortest_string


def all_the_longest(list):
    new_list = []
    max_length = 0

    for string in list:
        if len(string) > max_length:
            max_length = len(string)

    for string in list:
        if len(string) == max_length:
            new_list.append(string)

    return new_list


def formatted(list):
    for i in range(len(list)):
        list[i] = f"{list[i]:.2f}"

    return list


def everything_reversed(list):
    new_list = []
    for i in range(len(list) -1, -1, -1):
        new_list.append(list[i][::-1]) 

    return new_list

