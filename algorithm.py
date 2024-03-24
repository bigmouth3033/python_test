def binary_search(list_item, value: int):
    low = 0
    high = len(list_item) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list_item[mid]

        if value == guess:
            return mid

        if value > guess:
            low = mid + 1

        if value < guess:
            high = mid - 1

    return None


def main() -> None:
    # my_list = sorted([4,5,6,5,6,2,2,45,56])

    # print(my_list)

    # print(binary_search(my_list, 46))

    print(5 // 3)

    return


if __name__ == "__main__":
    main()
