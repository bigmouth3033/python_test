def most_common_character(string):
    most_common_char = string[0]

    for char in string:
        if string.count(char) > string.count(most_common_char):
            most_common_char = char

    return most_common_char


def no_shouting(list):
    new_list = []

    for string in list:
        if not string.isupper():
            new_list.append(string)

    return new_list


def longest_series_of_neighbours(list: list) -> list:
    longest_length = 0

    temp_count = 0
    for i in range(len(list)):
        if i + 1 < len(list) and abs(list[i + 1] - list[i]) == 1:
            temp_count += 1
            continue

        if longest_length < temp_count:
            longest_length = temp_count

        temp_count = 0

    if longest_length > 0:
        return longest_length + 1

    return longest_length


def main():
    return None


if __name__ == "__main__":
    main()
